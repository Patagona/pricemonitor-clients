# pricemonitor_api_client.InternalApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company**](InternalApi.md#add_company) | **POST** /controlpanel/api/companies | 
[**add_company_user**](InternalApi.md#add_company_user) | **PUT** /controlpanel/companies/{id}/users/{email} | 
[**add_pricing_strategy_scenario**](InternalApi.md#add_pricing_strategy_scenario) | **POST** /api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/scenarios | 
[**add_user**](InternalApi.md#add_user) | **POST** /controlpanel/users | Add a new user
[**authenticate**](InternalApi.md#authenticate) | **POST** /login | 
[**change_password**](InternalApi.md#change_password) | **PUT** /api/account/password | 
[**check_user_confirmation**](InternalApi.md#check_user_confirmation) | **HEAD** /api/account/confirm/{token} | Check if a specific confirmation token exists
[**confirm_user**](InternalApi.md#confirm_user) | **POST** /api/account/confirm/{token} | Confirm an unconfirmed user
[**create_alert_settings**](InternalApi.md#create_alert_settings) | **POST** /api/1/{contractId}/settings/alerts | 
[**create_auth_token**](InternalApi.md#create_auth_token) | **POST** /controlpanel/users/{email}/authtokens | 
[**create_task**](InternalApi.md#create_task) | **POST** /api/1/{contractId}/tasks | 
[**create_task_manufacturer_v2**](InternalApi.md#create_task_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/tasks | 
[**create_task_vendor_v2**](InternalApi.md#create_task_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/tasks | 
[**delete_alert_settings**](InternalApi.md#delete_alert_settings) | **DELETE** /api/1/{contractId}/settings/alerts/{alertId} | 
[**delete_auth_token**](InternalApi.md#delete_auth_token) | **DELETE** /controlpanel/users/{email}/authtokens/{token} | 
[**delete_callback_settings_manufacturer_v2**](InternalApi.md#delete_callback_settings_manufacturer_v2) | **DELETE** /api/2/m/contracts/{contractId}/settings/callbacks | 
[**delete_callback_settings_vendor_v2**](InternalApi.md#delete_callback_settings_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/settings/callbacks | 
[**delete_contract_vendor_v2**](InternalApi.md#delete_contract_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId} | 
[**delete_dynamic_monitoring_settings**](InternalApi.md#delete_dynamic_monitoring_settings) | **DELETE** /api/1/{contractId}/settings/dynamicmonitoring | 
[**delete_feed_vendor_v2**](InternalApi.md#delete_feed_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/feeds/{feedId} | 
[**delete_import_settings_vendor_v2**](InternalApi.md#delete_import_settings_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/settings/import | 
[**delete_monitoring_schedule_manufacturer_v3**](InternalApi.md#delete_monitoring_schedule_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Delete a monitoring schedule for a given contract.
[**delete_monitoring_schedule_vendor_v3**](InternalApi.md#delete_monitoring_schedule_vendor_v3) | **DELETE** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Delete a monitoring schedule for a given contract.
[**delete_products_manufacturer_v3**](InternalApi.md#delete_products_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/products | 
[**delete_repricing_strategy_vendor_v2**](InternalApi.md#delete_repricing_strategy_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/settings/repricingstrategy | 
[**delete_user_role**](InternalApi.md#delete_user_role) | **DELETE** /api/2/users/{userId}/role/{roleName} | 
[**delete_vendor_shop_mapping_manufacturer_v3**](InternalApi.md#delete_vendor_shop_mapping_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/vendors/{vendorId} | Delete a vendor and associated shops for a given contract.
[**execute_monitoring_schedule_manufacturer_v3**](InternalApi.md#execute_monitoring_schedule_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId}/execute | Trigger a monitoring pipeline task for manufacturer for configured monitoring schedule
[**execute_monitoring_schedule_vendor_v3**](InternalApi.md#execute_monitoring_schedule_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId}/execute | Trigger a monitoring pipeline task for vendor for configured monitoring schedule
[**get_active_ebay_token_vendor_v2**](InternalApi.md#get_active_ebay_token_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/ebay/token | 
[**get_alert_settings**](InternalApi.md#get_alert_settings) | **GET** /api/1/{contractId}/settings/alerts | 
[**get_all_companies**](InternalApi.md#get_all_companies) | **GET** /controlpanel/api/companies | Get a list of all companies
[**get_all_contracts**](InternalApi.md#get_all_contracts) | **GET** /controlpanel/api/contracts | Get a list of all contracts
[**get_all_domains_control_panel_v3**](InternalApi.md#get_all_domains_control_panel_v3) | **POST** /controlpanel/api/v3/domains | Add a new domain
[**get_all_ebay_authorizations_vendor_v2**](InternalApi.md#get_all_ebay_authorizations_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/ebay/authorizations | 
[**get_all_ebay_tokens_vendor_v2**](InternalApi.md#get_all_ebay_tokens_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/ebay/tokens | 
[**get_all_portals**](InternalApi.md#get_all_portals) | **GET** /controlpanel/api/portals | Get a list of all portals
[**get_all_scenarios_metadata**](InternalApi.md#get_all_scenarios_metadata) | **GET** /api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/scenarios | Get a list of all strategy scenarios metadata for a contract
[**get_all_tasks**](InternalApi.md#get_all_tasks) | **GET** /controlpanel/api/tasks | 
[**get_all_users**](InternalApi.md#get_all_users) | **GET** /controlpanel/api/users | Get a list of all users
[**get_authorization_status_vendor_v3**](InternalApi.md#get_authorization_status_vendor_v3) | **GET** /api/v3/companies/{companyId}/amazon/authorization/status | Get OAuth authorization status for customer&#39;s Amazon seller central account. For setting up OAuth authorization, have a look at the endpoint POST /api/v3/companies/{companyId}/amazon/authorization. 
[**get_callbacks**](InternalApi.md#get_callbacks) | **GET** /api/2/m/contracts/{contractId}/settings/callbacks | Get callbacks
[**get_callbacks_vendor_v2**](InternalApi.md#get_callbacks_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/callbacks | 
[**get_cheapest_vendors_manufacturer_v2**](InternalApi.md#get_cheapest_vendors_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/vendors/cheapest | 
[**get_company**](InternalApi.md#get_company) | **GET** /controlpanel/api/companies/{companyId} | 
[**get_complex_offer_filters_vendor_v2**](InternalApi.md#get_complex_offer_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/complex | Get all complex filters for the given contract.
[**get_contracts_vendor_v2**](InternalApi.md#get_contracts_vendor_v2) | **GET** /api/2/v/contracts | 
[**get_currency_vendor_v2**](InternalApi.md#get_currency_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/currency | 
[**get_customer_contract_settings_manufaturer_v3**](InternalApi.md#get_customer_contract_settings_manufaturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/customer | 
[**get_customer_contract_settings_vendor_v3**](InternalApi.md#get_customer_contract_settings_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/customer | 
[**get_domains_vendor_v2**](InternalApi.md#get_domains_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/domains | 
[**get_dynamic_monitoring_settings**](InternalApi.md#get_dynamic_monitoring_settings) | **GET** /api/1/{contractId}/settings/dynamicmonitoring | 
[**get_ebay_authorizations_vendor_v2**](InternalApi.md#get_ebay_authorizations_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/ebay/authorizations/{authIds} | 
[**get_extended_tags_manufacturer_v3**](InternalApi.md#get_extended_tags_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/products/{productId}/extendedtags | 
[**get_feed_export_delta_vendor_v2**](InternalApi.md#get_feed_export_delta_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/feeds/{feedId}/export/delta | 
[**get_feed_export_vendor_v2**](InternalApi.md#get_feed_export_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/feeds/{feedId}/export | 
[**get_import_settings_vendor_v2**](InternalApi.md#get_import_settings_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/import | 
[**get_manufacturer_manufacturer_v2**](InternalApi.md#get_manufacturer_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId} | 
[**get_manufacturer_v3**](InternalApi.md#get_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId} | Get the contract information
[**get_mappings_vendor_v2**](InternalApi.md#get_mappings_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/productidentifiermapping | 
[**get_marketplace_activation_status**](InternalApi.md#get_marketplace_activation_status) | **GET** /api/v3/companies/{companyId}/amazon/marketplace/{marketplaceCountryCode}/contracts/{contractId} | Get marketplace activation status of a customer in our system. 
[**get_monitoring_schedules_manufacturer_v3**](InternalApi.md#get_monitoring_schedules_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules | Get all the monitoring schedules for a specified contract.
[**get_monitoring_schedules_vendor_v3**](InternalApi.md#get_monitoring_schedules_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules | Get all the monitoring schedules for a specified contract.
[**get_monitoring_settings_manufacturer_v2**](InternalApi.md#get_monitoring_settings_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/settings/monitoring | 
[**get_monitoring_settings_manufacturer_v3**](InternalApi.md#get_monitoring_settings_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/monitoring | 
[**get_monitoring_settings_vendor_v2**](InternalApi.md#get_monitoring_settings_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/monitoring | 
[**get_monitoring_settings_vendor_v3**](InternalApi.md#get_monitoring_settings_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/monitoring | 
[**get_offer_filters_vendor_v2**](InternalApi.md#get_offer_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/vendors | Get all the vendor filters for the given contract.
[**get_offer_retention_settings_manufacturer_v3**](InternalApi.md#get_offer_retention_settings_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/offerretention | 
[**get_offer_retention_settings_vendor_v3**](InternalApi.md#get_offer_retention_settings_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/offerretention | 
[**get_offer_statistics_manufacturer_v3**](InternalApi.md#get_offer_statistics_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers/stats | Get offer statistics per product of a contract
[**get_offers_shops_manufacturer_v3**](InternalApi.md#get_offers_shops_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers/shops | Get shops with offers for time range
[**get_offers_shops_vendor_v3**](InternalApi.md#get_offers_shops_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/offers/shops | Get shops with offers for time range per domain
[**get_orders_count_by_portal_by_contract**](InternalApi.md#get_orders_count_by_portal_by_contract) | **GET** /api/1/{contractId}/products/orderscountbyportal | Get orders count by portal
[**get_price_cutters_manufacturer_v2**](InternalApi.md#get_price_cutters_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/pricecutters | 
[**get_price_cutters_vendor_v2**](InternalApi.md#get_price_cutters_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/pricecutters | 
[**get_price_recommendation_stats_vendor_v2**](InternalApi.md#get_price_recommendation_stats_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/result/pricerecommendationstats | 
[**get_product_filters_by_id_vendor_v2**](InternalApi.md#get_product_filters_by_id_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/offerfilters/:listType/products/query | 
[**get_product_filters_by_range_vendor_v2**](InternalApi.md#get_product_filters_by_range_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products | Get all the filters product-wise for the given contract.
[**get_product_filters_vendor_v2**](InternalApi.md#get_product_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products/{productId} | Get all the filters of a given product for the given contract.
[**get_product_metrics_by_contract**](InternalApi.md#get_product_metrics_by_contract) | **GET** /api/1/{contractId}/products/articlescountbyportal | 
[**get_product_monitoring_status_stats_vendor_v3**](InternalApi.md#get_product_monitoring_status_stats_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/monitoringstatus/stats | 
[**get_product_price_violations_manufacturer_v2**](InternalApi.md#get_product_price_violations_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/priceviolations | 
[**get_product_price_violations_vendor_v2**](InternalApi.md#get_product_price_violations_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/result/priceviolations | 
[**get_repricing_strategy_vendor_v2**](InternalApi.md#get_repricing_strategy_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/repricingstrategy | 
[**get_scenario_by_id**](InternalApi.md#get_scenario_by_id) | **GET** /api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/scenarios/{scenarioId} | Get a strategy scenario with the provided scenario Id
[**get_settings**](InternalApi.md#get_settings) | **GET** /api/1/{contractId}/settings | 
[**get_tag_values_manufacturer_v2**](InternalApi.md#get_tag_values_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/products/tags/{key} | 
[**get_tag_values_vendor_v2**](InternalApi.md#get_tag_values_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/products/tags/{key} | 
[**get_tags_manufacturer_v2**](InternalApi.md#get_tags_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/products/tags | 
[**get_tags_vendor_v2**](InternalApi.md#get_tags_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/products/tags | 
[**get_task**](InternalApi.md#get_task) | **GET** /api/1/{contractId}/tasks/{taskId} | 
[**get_task_data_manufacturer_v2**](InternalApi.md#get_task_data_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/tasks/{taskId}/data | 
[**get_task_data_vendor_v2**](InternalApi.md#get_task_data_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/tasks/{taskId}/data | 
[**get_task_manufacturer_v2**](InternalApi.md#get_task_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/tasks/{taskId} | 
[**get_task_state**](InternalApi.md#get_task_state) | **GET** /api/1/{contractId}/tasks/{taskId}/state | 
[**get_tasks**](InternalApi.md#get_tasks) | **GET** /api/1/{contractId}/tasks | 
[**get_tasks_manufacturer_v2**](InternalApi.md#get_tasks_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/tasks | 
[**get_tasks_stats**](InternalApi.md#get_tasks_stats) | **GET** /controlpanel/api/tasks/stats | 
[**get_time_stamps**](InternalApi.md#get_time_stamps) | **GET** /api/1/{contractId}/products/analysis/timestamps | 
[**get_user**](InternalApi.md#get_user) | **GET** /controlpanel/api/users/{email} | 
[**get_users**](InternalApi.md#get_users) | **GET** /controlpanel/api/companies/{companyId}/users | 
[**get_vendor_settings_v2_vendor_v2**](InternalApi.md#get_vendor_settings_v2_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/repricing | 
[**get_vendor_shop_mapping_manufacturer_v3**](InternalApi.md#get_vendor_shop_mapping_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/vendors/{vendorId} | Get vendor along with their associated shop for given vendor id and contract.
[**get_vendor_shop_mappings_manufacturer_v3**](InternalApi.md#get_vendor_shop_mappings_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/vendors | Get all the vendors along with their associated shops for a specified contract.
[**get_vendor_v3**](InternalApi.md#get_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId} | 
[**get_vendor_vendor_v2**](InternalApi.md#get_vendor_vendor_v2) | **GET** /api/2/v/contracts/{contractId} | 
[**get_vendors_by_domain_manufacturer_v2**](InternalApi.md#get_vendors_by_domain_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/vendors/list | 
[**list_vendors**](InternalApi.md#list_vendors) | **GET** /controlpanel/vendors | 
[**login_by_auth_token**](InternalApi.md#login_by_auth_token) | **GET** /api/login/token/{token} | 
[**logout**](InternalApi.md#logout) | **POST** /logout | 
[**monitoring_pipeline_post_request_manufacturer_v3**](InternalApi.md#monitoring_pipeline_post_request_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/monitoringpipeline/{path} | 
[**monitoring_pipeline_post_request_vendor_v3**](InternalApi.md#monitoring_pipeline_post_request_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/monitoringpipeline/{path} | 
[**monitoring_pipeline_upsert_search_attempts_manufacturer_v3**](InternalApi.md#monitoring_pipeline_upsert_search_attempts_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/monitoringpipeline/v1/searchattempts | 
[**monitoring_pipeline_upsert_search_attempts_vendor_v3**](InternalApi.md#monitoring_pipeline_upsert_search_attempts_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/monitoringpipeline/v1/searchattempts | 
[**patch_product_manufacturer_v3**](InternalApi.md#patch_product_manufacturer_v3) | **PATCH** /api/v3/manufacturer/contracts/{contractId}/products/{productId} | 
[**patch_product_vendor_v3**](InternalApi.md#patch_product_vendor_v3) | **PATCH** /api/v3/vendor/contracts/{contractId}/products/{productId} | 
[**position_distribution**](InternalApi.md#position_distribution) | **POST** /api/1/{contractId}/vendors/{vendor}/positions | 
[**post_account_v3**](InternalApi.md#post_account_v3) | **POST** /api/v3/account | Create a new user account
[**post_activate_marketplace_vendor_v3**](InternalApi.md#post_activate_marketplace_vendor_v3) | **POST** /api/v3/companies/{companyId}/amazon/marketplace | Activate marketplace of a customer in our system. By activation, it means that our system can write prices back into the customer&#39;s Amazon shop. 
[**post_authorize_seller_vendor_v3**](InternalApi.md#post_authorize_seller_vendor_v3) | **POST** /api/v3/companies/{companyId}/amazon/authorization | Set up an OAuth authorization for a customer&#39;s Amazon Seller Central account. It establishes a connection between our system and the customer&#39;s Amazon shop using the Amazon SP-API. Once connected, our system can write prices back to the customer&#39;s Amazon shop, allowing them to benefit from our price recommendations. 
[**post_ebay_authorization_vendor_v2**](InternalApi.md#post_ebay_authorization_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/settings/ebay/authorizations | 
[**post_embed_sso_url_manufacturer**](InternalApi.md#post_embed_sso_url_manufacturer) | **POST** /api/v3/manufacturer/contracts/{contractId}/looker/sso/embed/url | Retrieve an embed SSO url for Looker.
[**post_embed_sso_url_vendor**](InternalApi.md#post_embed_sso_url_vendor) | **POST** /api/v3/vendor/contracts/{contractId}/looker/sso/embed/url | Retrieve an embed SSO url for Looker.
[**post_feed_vendor_v2**](InternalApi.md#post_feed_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/feeds | 
[**post_mappings_vendor_v2**](InternalApi.md#post_mappings_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/productidentifiermapping | 
[**post_monitoring_schedule_manufacturer_v3**](InternalApi.md#post_monitoring_schedule_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules | Add a monitoring schedule for a given contract.
[**post_monitoring_schedule_vendor_v3**](InternalApi.md#post_monitoring_schedule_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules | Add a monitoring schedule for a given contract.
[**post_offer_statistics_vendor_query**](InternalApi.md#post_offer_statistics_vendor_query) | **POST** /api/v3/vendor/contracts/{contractId}/offers/stats/query | 
[**post_vendor_shop_mapping_manufacturer_v3**](InternalApi.md#post_vendor_shop_mapping_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/vendors | Add a new vendor for a given contract and associate shops with the given vendor.
[**prices_by_day_by_product_id_manufacturer_v2**](InternalApi.md#prices_by_day_by_product_id_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/pricesbyday/productid/{productId} | 
[**publish_preprocessing_task_vendor_v3**](InternalApi.md#publish_preprocessing_task_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/tasks/preprocessing | Publish a preprocessing task for vendor.
[**put_callbacks**](InternalApi.md#put_callbacks) | **PUT** /api/2/m/contracts/{contractId}/settings/callbacks | Set callbacks
[**put_callbacks_vendor_v2**](InternalApi.md#put_callbacks_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/callbacks | 
[**put_complex_offer_filters_vendor_v2**](InternalApi.md#put_complex_offer_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/complex | Add the complex filters for the given contract.
[**put_currency_vendor_v2**](InternalApi.md#put_currency_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/currency | 
[**put_customer_contract_settings_manufacturer_v3**](InternalApi.md#put_customer_contract_settings_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/customer | 
[**put_customer_contract_settings_vendor_v3**](InternalApi.md#put_customer_contract_settings_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/customer | 
[**put_dynamic_monitoring_settings**](InternalApi.md#put_dynamic_monitoring_settings) | **PUT** /api/1/{contractId}/settings/dynamicmonitoring | 
[**put_feed_vendor_v2**](InternalApi.md#put_feed_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/feeds/{feedId} | 
[**put_image_tag_manufacturer_v2**](InternalApi.md#put_image_tag_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/settings/imagetag | 
[**put_image_tag_vendor_v2**](InternalApi.md#put_image_tag_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/imagetag | 
[**put_import_settings_vendor_v2**](InternalApi.md#put_import_settings_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/import | 
[**put_monitoring_schedule_manufacturer_v3**](InternalApi.md#put_monitoring_schedule_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Update a monitoring schedule for a given contract.
[**put_monitoring_schedule_vendor_v3**](InternalApi.md#put_monitoring_schedule_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Update a monitoring schedule for a given contract.
[**put_monitoring_settings_manufacturer_v2**](InternalApi.md#put_monitoring_settings_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/settings/monitoring | 
[**put_monitoring_settings_manufacturer_v3**](InternalApi.md#put_monitoring_settings_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/monitoring | 
[**put_monitoring_settings_vendor_v2**](InternalApi.md#put_monitoring_settings_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/monitoring | 
[**put_monitoring_settings_vendor_v3**](InternalApi.md#put_monitoring_settings_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/monitoring | 
[**put_offer_filters_vendor_v2**](InternalApi.md#put_offer_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/vendors | Store the vendor filters for the given contract.
[**put_offer_retention_settings_manufacturer_v3**](InternalApi.md#put_offer_retention_settings_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/offerretention | 
[**put_offer_retention_settings_vendor_v3**](InternalApi.md#put_offer_retention_settings_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/offerretention | 
[**put_product_filters_vendor_v2**](InternalApi.md#put_product_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products/{productId} | Store the filters of a given product for the given contract.
[**put_products_csv_manufacturer_v2**](InternalApi.md#put_products_csv_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/products/csv | 
[**put_products_vendor_v2**](InternalApi.md#put_products_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/products | 
[**put_repricing_strategy_vendor_v2**](InternalApi.md#put_repricing_strategy_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/repricingstrategy | 
[**put_settings**](InternalApi.md#put_settings) | **PUT** /api/1/{contractId}/settings | 
[**put_vendor_settings_vendor_v2**](InternalApi.md#put_vendor_settings_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/repricing | 
[**put_vendor_shop_mapping_manufacturer_v3**](InternalApi.md#put_vendor_shop_mapping_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/vendors/{vendorId} | Update an existing vendor for a given contract and associate shops with the given vendor.
[**query_offers_manufacturer_v3**](InternalApi.md#query_offers_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/query | 
[**query_offers_shop_manufacturer_v3**](InternalApi.md#query_offers_shop_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/shop/query | 
[**query_offers_shop_vendor_v3**](InternalApi.md#query_offers_shop_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/offers/shop/query | 
[**query_offers_stats_manufacturer_v3**](InternalApi.md#query_offers_stats_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/stats/query | 
[**query_price_recommendations_vendor_v2**](InternalApi.md#query_price_recommendations_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/pricerecommendations/query | 
[**query_products_by_filter_manufacturer_v3**](InternalApi.md#query_products_by_filter_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/products/query | 
[**query_products_by_filter_vendor_v3**](InternalApi.md#query_products_by_filter_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/products/query | 
[**raw_offers**](InternalApi.md#raw_offers) | **GET** /api/1/{contractId}/products/offers | 
[**remove_user**](InternalApi.md#remove_user) | **DELETE** /controlpanel/api/companies/{companyId}/users/{userId} | 
[**request_new_password**](InternalApi.md#request_new_password) | **POST** /api/account/password/reset | Request a new password
[**reset_password**](InternalApi.md#reset_password) | **PUT** /api/account/password/reset | Reset the password
[**save_include_delivery_costs**](InternalApi.md#save_include_delivery_costs) | **POST** /api/1/{contractId}/settings/include_delivery_costs | 
[**scheduler_delete_request_manufacturer_v3**](InternalApi.md#scheduler_delete_request_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/scheduler/{path} | 
[**scheduler_delete_request_vendor_v3**](InternalApi.md#scheduler_delete_request_vendor_v3) | **DELETE** /api/v3/vendor/contracts/{contractId}/scheduler/{path} | 
[**scheduler_get_request_manufacturer_v3**](InternalApi.md#scheduler_get_request_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/scheduler/{path} | 
[**scheduler_get_request_vendor_v3**](InternalApi.md#scheduler_get_request_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/scheduler/{path} | 
[**scheduler_post_request_manufacturer_v3**](InternalApi.md#scheduler_post_request_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/scheduler/{path} | 
[**scheduler_post_request_vendor_v3**](InternalApi.md#scheduler_post_request_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/scheduler/{path} | 
[**scheduler_put_request_manufacturer_v3**](InternalApi.md#scheduler_put_request_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/scheduler/{path} | 
[**scheduler_put_request_vendor_v3**](InternalApi.md#scheduler_put_request_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/scheduler/{path} | 
[**segment_offers_manufacturer_v2**](InternalApi.md#segment_offers_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/offersegmentation | 
[**segment_offers_vendor_v2**](InternalApi.md#segment_offers_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/offersegmentation | 
[**shop_integration_get_request**](InternalApi.md#shop_integration_get_request) | **GET** /api/2/v/contracts/{contractId}/shop-integration/{path} | 
[**shop_integration_post_request**](InternalApi.md#shop_integration_post_request) | **POST** /api/2/v/contracts/{contractId}/shop-integration/{path} | 
[**shop_integration_post_request_vendor_v2**](InternalApi.md#shop_integration_post_request_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/products/import | 
[**stats_manufacturer_v2**](InternalApi.md#stats_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/contract/stats | 
[**timestamps_manufacturer_v2**](InternalApi.md#timestamps_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/timestamps | 
[**update_alert_settings**](InternalApi.md#update_alert_settings) | **PUT** /api/1/{contractId}/settings/alerts/{alertId} | 
[**update_auth_token**](InternalApi.md#update_auth_token) | **PUT** /controlpanel/users/{email}/authtokens/{token} | 
[**update_task_manufacturer_v2**](InternalApi.md#update_task_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/tasks/{taskId} | 
[**update_task_vendor_v2**](InternalApi.md#update_task_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/tasks/{taskId} | 
[**update_user_role**](InternalApi.md#update_user_role) | **PUT** /api/2/users/{userId}/role/{roleName} | 
[**user_info**](InternalApi.md#user_info) | **GET** /api/account | Details of the current user
[**user_signup**](InternalApi.md#user_signup) | **POST** /api/account | Create a new user account in the system
[**validate_offers_manufacturer_v2**](InternalApi.md#validate_offers_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/validation | 
[**validate_offers_vendor_v2**](InternalApi.md#validate_offers_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/validation | 
[**vendor_data**](InternalApi.md#vendor_data) | **GET** /controlpanel/vendorexport/{vendor} | 
[**version**](InternalApi.md#version) | **GET** /version | Get the current application version


# **add_company**
> object add_company()



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        api_response = api_instance.add_company()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->add_company: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        api_response = api_instance.add_company()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->add_company: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_company_user**
> object add_company_user(id, email, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    id = 56 # int | 
email = 'email_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.add_company_user(id, email, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->add_company_user: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    id = 56 # int | 
email = 'email_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.add_company_user(id, email, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->add_company_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **email** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pricing_strategy_scenario**
> PostScenarioStrategyResponseApiResponse add_pricing_strategy_scenario(contract_id, post_scenario_strategy_request=post_scenario_strategy_request)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
post_scenario_strategy_request = pricemonitor_api_client.PostScenarioStrategyRequest() # PostScenarioStrategyRequest | The scenario strategy to be stored. Including the necessary metadata. (optional)

    try:
        api_response = api_instance.add_pricing_strategy_scenario(contract_id, post_scenario_strategy_request=post_scenario_strategy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->add_pricing_strategy_scenario: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
post_scenario_strategy_request = pricemonitor_api_client.PostScenarioStrategyRequest() # PostScenarioStrategyRequest | The scenario strategy to be stored. Including the necessary metadata. (optional)

    try:
        api_response = api_instance.add_pricing_strategy_scenario(contract_id, post_scenario_strategy_request=post_scenario_strategy_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->add_pricing_strategy_scenario: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **post_scenario_strategy_request** | [**PostScenarioStrategyRequest**](PostScenarioStrategyRequest.md)| The scenario strategy to be stored. Including the necessary metadata. | [optional] 

### Return type

[**PostScenarioStrategyResponseApiResponse**](PostScenarioStrategyResponseApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new scenario strategy was added |  -  |
**400** | Strategy must be valid and consistent with the schema version. Required fields need to be filled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user**
> add_user(new_user=new_user)

Add a new user

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    new_user = pricemonitor_api_client.NewUser() # NewUser | The new user to be added (optional)

    try:
        # Add a new user
        api_instance.add_user(new_user=new_user)
    except ApiException as e:
        print("Exception when calling InternalApi->add_user: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    new_user = pricemonitor_api_client.NewUser() # NewUser | The new user to be added (optional)

    try:
        # Add a new user
        api_instance.add_user(new_user=new_user)
    except ApiException as e:
        print("Exception when calling InternalApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_user** | [**NewUser**](NewUser.md)| The new user to be added | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new user was added |  -  |
**400** | A new user was not added |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate**
> object authenticate()



### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        api_response = api_instance.authenticate()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->authenticate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authenticate with the API and create a session |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_password**
> object change_password()



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        api_response = api_instance.change_password()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->change_password: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        api_response = api_instance.change_password()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->change_password: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Change the current user&#39;s password. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_user_confirmation**
> check_user_confirmation(token)

Check if a specific confirmation token exists

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    token = 'token_example' # str | 

    try:
        # Check if a specific confirmation token exists
        api_instance.check_user_confirmation(token)
    except ApiException as e:
        print("Exception when calling InternalApi->check_user_confirmation: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    token = 'token_example' # str | 

    try:
        # Check if a specific confirmation token exists
        api_instance.check_user_confirmation(token)
    except ApiException as e:
        print("Exception when calling InternalApi->check_user_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |
**204** | Confirmation token was found |  -  |
**404** | No such confirmation token was found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_user**
> confirm_user(token, body)

Confirm an unconfirmed user

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    token = 'token_example' # str | 
body = 'body_example' # str | The password that should be set on the confirmed user

    try:
        # Confirm an unconfirmed user
        api_instance.confirm_user(token, body)
    except ApiException as e:
        print("Exception when calling InternalApi->confirm_user: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    token = 'token_example' # str | 
body = 'body_example' # str | The password that should be set on the confirmed user

    try:
        # Confirm an unconfirmed user
        api_instance.confirm_user(token, body)
    except ApiException as e:
        print("Exception when calling InternalApi->confirm_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **body** | **str**| The password that should be set on the confirmed user | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |
**204** | User was confirmed &amp; logged in |  -  |
**400** | Unable to confirm the user because of bad request data |  -  |
**500** | Unable to confirm the user because of an unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_alert_settings**
> object create_alert_settings(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.create_alert_settings(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_alert_settings: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.create_alert_settings(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_alert_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_token**
> object create_auth_token(email, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    email = 'email_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.create_auth_token(email, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_auth_token: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    email = 'email_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.create_auth_token(email, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> object create_task(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_create_task_body_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCreateTaskBodyV2() # ComPatagonaPricemonitorShareApiCreateTaskBodyV2 | Create a new task (optional)

    try:
        api_response = api_instance.create_task(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_task: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_create_task_body_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCreateTaskBodyV2() # ComPatagonaPricemonitorShareApiCreateTaskBodyV2 | Create a new task (optional)

    try:
        api_response = api_instance.create_task(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_create_task_body_v2** | [**ComPatagonaPricemonitorShareApiCreateTaskBodyV2**](ComPatagonaPricemonitorShareApiCreateTaskBodyV2.md)| Create a new task | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task_manufacturer_v2**
> GenericTaskWithUrl create_task_manufacturer_v2(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)



Create a new task

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_create_task_body_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCreateTaskBodyV2() # ComPatagonaPricemonitorShareApiCreateTaskBodyV2 | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.create_task_manufacturer_v2(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_task_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_create_task_body_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCreateTaskBodyV2() # ComPatagonaPricemonitorShareApiCreateTaskBodyV2 | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.create_task_manufacturer_v2(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_task_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_create_task_body_v2** | [**ComPatagonaPricemonitorShareApiCreateTaskBodyV2**](ComPatagonaPricemonitorShareApiCreateTaskBodyV2.md)| This is a generated entry and needs to be described. | [optional] 

### Return type

[**GenericTaskWithUrl**](GenericTaskWithUrl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The new task was successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task_vendor_v2**
> object create_task_vendor_v2(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_create_task_body_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCreateTaskBodyV2() # ComPatagonaPricemonitorShareApiCreateTaskBodyV2 | Create a new task (optional)

    try:
        api_response = api_instance.create_task_vendor_v2(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_task_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_create_task_body_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCreateTaskBodyV2() # ComPatagonaPricemonitorShareApiCreateTaskBodyV2 | Create a new task (optional)

    try:
        api_response = api_instance.create_task_vendor_v2(contract_id, com_patagona_pricemonitor_share_api_create_task_body_v2=com_patagona_pricemonitor_share_api_create_task_body_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->create_task_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_create_task_body_v2** | [**ComPatagonaPricemonitorShareApiCreateTaskBodyV2**](ComPatagonaPricemonitorShareApiCreateTaskBodyV2.md)| Create a new task | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task has been created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_settings**
> object delete_alert_settings(contract_id, alert_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
alert_id = 'alert_id_example' # str | 

    try:
        api_response = api_instance.delete_alert_settings(contract_id, alert_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_alert_settings: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
alert_id = 'alert_id_example' # str | 

    try:
        api_response = api_instance.delete_alert_settings(contract_id, alert_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_alert_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **alert_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_token**
> object delete_auth_token(email, token)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    email = 'email_example' # str | 
token = 'token_example' # str | 

    try:
        api_response = api_instance.delete_auth_token(email, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_auth_token: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    email = 'email_example' # str | 
token = 'token_example' # str | 

    try:
        api_response = api_instance.delete_auth_token(email, token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **token** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_callback_settings_manufacturer_v2**
> object delete_callback_settings_manufacturer_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_callback_settings_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_callback_settings_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_callback_settings_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_callback_settings_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_callback_settings_vendor_v2**
> object delete_callback_settings_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_callback_settings_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_callback_settings_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_callback_settings_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_callback_settings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contract_vendor_v2**
> object delete_contract_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_contract_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_contract_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_contract_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_contract_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dynamic_monitoring_settings**
> object delete_dynamic_monitoring_settings(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_dynamic_monitoring_settings(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_dynamic_monitoring_settings: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_dynamic_monitoring_settings(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_dynamic_monitoring_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_feed_vendor_v2**
> object delete_feed_vendor_v2(contract_id, feed_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
feed_id = 'feed_id_example' # str | 

    try:
        api_response = api_instance.delete_feed_vendor_v2(contract_id, feed_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_feed_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
feed_id = 'feed_id_example' # str | 

    try:
        api_response = api_instance.delete_feed_vendor_v2(contract_id, feed_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_feed_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **feed_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import_settings_vendor_v2**
> object delete_import_settings_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_import_settings_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_import_settings_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_import_settings_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_import_settings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_monitoring_schedule_manufacturer_v3**
> ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse delete_monitoring_schedule_manufacturer_v3(contract_id, schedule_id)

Delete a monitoring schedule for a given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule

    try:
        # Delete a monitoring schedule for a given contract.
        api_response = api_instance.delete_monitoring_schedule_manufacturer_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule

    try:
        # Delete a monitoring schedule for a given contract.
        api_response = api_instance.delete_monitoring_schedule_manufacturer_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 

### Return type

[**ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse**](ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monitoring schedule has been deleted successfully. |  -  |
**404** | Specified monitoring schedule does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_monitoring_schedule_vendor_v3**
> ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse delete_monitoring_schedule_vendor_v3(contract_id, schedule_id)

Delete a monitoring schedule for a given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule

    try:
        # Delete a monitoring schedule for a given contract.
        api_response = api_instance.delete_monitoring_schedule_vendor_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_monitoring_schedule_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule

    try:
        # Delete a monitoring schedule for a given contract.
        api_response = api_instance.delete_monitoring_schedule_vendor_v3(contract_id, schedule_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 

### Return type

[**ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse**](ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monitoring schedule has been deleted successfully. |  -  |
**404** | Specified monitoring schedule does not exist. |  -  |
**503** | Monitoring schedule could not be deleted due to an internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_products_manufacturer_v3**
> object delete_products_manufacturer_v3(contract_id, updated_max=updated_max)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.delete_products_manufacturer_v3(contract_id, updated_max=updated_max)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_products_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
updated_max = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.delete_products_manufacturer_v3(contract_id, updated_max=updated_max)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_products_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **updated_max** | **datetime**|  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repricing_strategy_vendor_v2**
> object delete_repricing_strategy_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_repricing_strategy_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_repricing_strategy_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.delete_repricing_strategy_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_repricing_strategy_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete all strategy versions per provided contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_role**
> object delete_user_role(user_id, role_name)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    user_id = 56 # int | 
role_name = 'role_name_example' # str | 

    try:
        api_response = api_instance.delete_user_role(user_id, role_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_user_role: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    user_id = 56 # int | 
role_name = 'role_name_example' # str | 

    try:
        api_response = api_instance.delete_user_role(user_id, role_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **role_name** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor_shop_mapping_manufacturer_v3**
> ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse delete_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)

Delete a vendor and associated shops for a given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping

    try:
        # Delete a vendor and associated shops for a given contract.
        api_response = api_instance.delete_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping

    try:
        # Delete a vendor and associated shops for a given contract.
        api_response = api_instance.delete_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->delete_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **vendor_id** | **int**| ID of vendor shop mapping | 

### Return type

[**ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse**](ComPatagonaPricemonitorShareApiDeleteByNumericIdApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A vendor and associated shops have been deleted successfully. |  -  |
**404** | Specified vendor does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_monitoring_schedule_manufacturer_v3**
> EmptyApiResponse execute_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)

Trigger a monitoring pipeline task for manufacturer for configured monitoring schedule

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Trigger a monitoring pipeline task for manufacturer for configured monitoring schedule
        api_response = api_instance.execute_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->execute_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Trigger a monitoring pipeline task for manufacturer for configured monitoring schedule
        api_response = api_instance.execute_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->execute_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 
 **trigger_follow_up_task** | **bool**|  | [optional] 

### Return type

[**EmptyApiResponse**](EmptyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monitoring task was successfully created and is executing |  -  |
**404** | Couldn&#39;t find any monitoring schedules for given schedule id. No monitoring task was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_monitoring_schedule_vendor_v3**
> EmptyApiResponse execute_monitoring_schedule_vendor_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)

Trigger a monitoring pipeline task for vendor for configured monitoring schedule

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Trigger a monitoring pipeline task for vendor for configured monitoring schedule
        api_response = api_instance.execute_monitoring_schedule_vendor_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->execute_monitoring_schedule_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Trigger a monitoring pipeline task for vendor for configured monitoring schedule
        api_response = api_instance.execute_monitoring_schedule_vendor_v3(contract_id, schedule_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->execute_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 
 **trigger_follow_up_task** | **bool**|  | [optional] 

### Return type

[**EmptyApiResponse**](EmptyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monitoring task was successfully created and is executing |  -  |
**404** | Couldn&#39;t find any monitoring schedules for given schedule id. No monitoring task was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_ebay_token_vendor_v2**
> object get_active_ebay_token_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_active_ebay_token_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_active_ebay_token_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_active_ebay_token_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_active_ebay_token_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_settings**
> object get_alert_settings(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_alert_settings(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_alert_settings: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_alert_settings(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_alert_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_companies**
> ComPatagonaPricemonitorShareApiAdminCompanyV2 get_all_companies(start=start, limit=limit)

Get a list of all companies

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    start = 0 # int | Start of the pagination (optional) (default to 0)
limit = 100 # int | Number of elements per page (optional) (default to 100)

    try:
        # Get a list of all companies
        api_response = api_instance.get_all_companies(start=start, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_companies: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    start = 0 # int | Start of the pagination (optional) (default to 0)
limit = 100 # int | Number of elements per page (optional) (default to 100)

    try:
        # Get a list of all companies
        api_response = api_instance.get_all_companies(start=start, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start of the pagination | [optional] [default to 0]
 **limit** | **int**| Number of elements per page | [optional] [default to 100]

### Return type

[**ComPatagonaPricemonitorShareApiAdminCompanyV2**](ComPatagonaPricemonitorShareApiAdminCompanyV2.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of companies was loaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_contracts**
> get_all_contracts()

Get a list of all contracts

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        # Get a list of all contracts
        api_instance.get_all_contracts()
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_contracts: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        # Get a list of all contracts
        api_instance.get_all_contracts()
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_contracts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of contracts was loaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_domains_control_panel_v3**
> PostAdminAddDomainV3ApiResponse get_all_domains_control_panel_v3(com_patagona_pricemonitor_share_api_post_admin_add_domain_body_v3=com_patagona_pricemonitor_share_api_post_admin_add_domain_body_v3)

Add a new domain

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    com_patagona_pricemonitor_share_api_post_admin_add_domain_body_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3() # ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3 | The domain to be added and its offer sources (optional)

    try:
        # Add a new domain
        api_response = api_instance.get_all_domains_control_panel_v3(com_patagona_pricemonitor_share_api_post_admin_add_domain_body_v3=com_patagona_pricemonitor_share_api_post_admin_add_domain_body_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_domains_control_panel_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    com_patagona_pricemonitor_share_api_post_admin_add_domain_body_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3() # ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3 | The domain to be added and its offer sources (optional)

    try:
        # Add a new domain
        api_response = api_instance.get_all_domains_control_panel_v3(com_patagona_pricemonitor_share_api_post_admin_add_domain_body_v3=com_patagona_pricemonitor_share_api_post_admin_add_domain_body_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_domains_control_panel_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_post_admin_add_domain_body_v3** | [**ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3**](ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.md)| The domain to be added and its offer sources | [optional] 

### Return type

[**PostAdminAddDomainV3ApiResponse**](PostAdminAddDomainV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new domain was added |  -  |
**400** | - Offer sources must be valid and non-empty - Domain must be a valid internet domain and non-empty - Domain name must be unique and non-empty - Please refer to the request schema for what constitutes valid offer sources and a valid domain  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ebay_authorizations_vendor_v2**
> object get_all_ebay_authorizations_vendor_v2(contract_id, start, limit)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 

    try:
        api_response = api_instance.get_all_ebay_authorizations_vendor_v2(contract_id, start, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_ebay_authorizations_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 

    try:
        api_response = api_instance.get_all_ebay_authorizations_vendor_v2(contract_id, start, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_ebay_authorizations_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **int**|  | 
 **limit** | **int**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ebay_tokens_vendor_v2**
> object get_all_ebay_tokens_vendor_v2(contract_id, start, limit)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 

    try:
        api_response = api_instance.get_all_ebay_tokens_vendor_v2(contract_id, start, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_ebay_tokens_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 

    try:
        api_response = api_instance.get_all_ebay_tokens_vendor_v2(contract_id, start, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_ebay_tokens_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **int**|  | 
 **limit** | **int**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_portals**
> get_all_portals()

Get a list of all portals

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        # Get a list of all portals
        api_instance.get_all_portals()
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_portals: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        # Get a list of all portals
        api_instance.get_all_portals()
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_portals: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of portals was loaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_scenarios_metadata**
> list[ScenarioStrategyMetadataResponseApiResponse] get_all_scenarios_metadata(contract_id)

Get a list of all strategy scenarios metadata for a contract

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get a list of all strategy scenarios metadata for a contract
        api_response = api_instance.get_all_scenarios_metadata(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_scenarios_metadata: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get a list of all strategy scenarios metadata for a contract
        api_response = api_instance.get_all_scenarios_metadata(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_scenarios_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**list[ScenarioStrategyMetadataResponseApiResponse]**](ScenarioStrategyMetadataResponseApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all strategy scenarios metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tasks**
> object get_all_tasks(contract_id, task_id, task_type, task_state, limit, min_creation_date=min_creation_date, max_creation_date=max_creation_date)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = ['contract_id_example'] # list[str] | 
task_id = ['task_id_example'] # list[str] | 
task_type = ['task_type_example'] # list[str] | 
task_state = ['task_state_example'] # list[str] | 
limit = 56 # int | 
min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_all_tasks(contract_id, task_id, task_type, task_state, limit, min_creation_date=min_creation_date, max_creation_date=max_creation_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_tasks: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = ['contract_id_example'] # list[str] | 
task_id = ['task_id_example'] # list[str] | 
task_type = ['task_type_example'] # list[str] | 
task_state = ['task_state_example'] # list[str] | 
limit = 56 # int | 
min_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_all_tasks(contract_id, task_id, task_type, task_state, limit, min_creation_date=min_creation_date, max_creation_date=max_creation_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | [**list[str]**](str.md)|  | 
 **task_id** | [**list[str]**](str.md)|  | 
 **task_type** | [**list[str]**](str.md)|  | 
 **task_state** | [**list[str]**](str.md)|  | 
 **limit** | **int**|  | 
 **min_creation_date** | **datetime**|  | [optional] 
 **max_creation_date** | **datetime**|  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> get_all_users()

Get a list of all users

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        # Get a list of all users
        api_instance.get_all_users()
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_users: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        # Get a list of all users
        api_instance.get_all_users()
    except ApiException as e:
        print("Exception when calling InternalApi->get_all_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of users was loaded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_status_vendor_v3**
> GetAuthorizationStatusResponseV3ApiResponse get_authorization_status_vendor_v3(company_id)

Get OAuth authorization status for customer's Amazon seller central account. For setting up OAuth authorization, have a look at the endpoint POST /api/v3/companies/{companyId}/amazon/authorization. 

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company

    try:
        # Get OAuth authorization status for customer's Amazon seller central account. For setting up OAuth authorization, have a look at the endpoint POST /api/v3/companies/{companyId}/amazon/authorization. 
        api_response = api_instance.get_authorization_status_vendor_v3(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_authorization_status_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company

    try:
        # Get OAuth authorization status for customer's Amazon seller central account. For setting up OAuth authorization, have a look at the endpoint POST /api/v3/companies/{companyId}/amazon/authorization. 
        api_response = api_instance.get_authorization_status_vendor_v3(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_authorization_status_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 

### Return type

[**GetAuthorizationStatusResponseV3ApiResponse**](GetAuthorizationStatusResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorization status of a customer on Amazon. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_callbacks**
> Callbacks get_callbacks(contract_id)

Get callbacks

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get callbacks
        api_response = api_instance.get_callbacks(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_callbacks: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get callbacks
        api_response = api_instance.get_callbacks(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_callbacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**Callbacks**](Callbacks.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | - |  -  |
**404** | Settings for this contract don&#39;t exist yet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_callbacks_vendor_v2**
> object get_callbacks_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_callbacks_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_callbacks_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_callbacks_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_callbacks_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cheapest_vendors_manufacturer_v2**
> object get_cheapest_vendors_manufacturer_v2(contract_id, session, include_delivery_costs, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_cheapest_vendors_manufacturer_v2(contract_id, session, include_delivery_costs, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_cheapest_vendors_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_cheapest_vendors_manufacturer_v2(contract_id, session, include_delivery_costs, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_cheapest_vendors_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **session** | **datetime**|  | 
 **include_delivery_costs** | **bool**|  | 
 **com_patagona_pricemonitor_share_api_tag_filtered_vendors_request** | [**ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest**](ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest.md)| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company**
> object get_company(company_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company

    try:
        api_response = api_instance.get_company(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_company: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company

    try:
        api_response = api_instance.get_company(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_company: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_complex_offer_filters_vendor_v2**
> OfferFilterApiResponse get_complex_offer_filters_vendor_v2(contract_id, list_type)

Get all complex filters for the given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all complex filters for the given contract.
        api_response = api_instance.get_complex_offer_filters_vendor_v2(contract_id, list_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_complex_offer_filters_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all complex filters for the given contract.
        api_response = api_instance.get_complex_offer_filters_vendor_v2(contract_id, list_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_complex_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 

### Return type

[**OfferFilterApiResponse**](OfferFilterApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the filters to ignore the individual offers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts_vendor_v2**
> object get_contracts_vendor_v2(max_creation_date=max_creation_date, min_expiration_date=min_expiration_date)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_expiration_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_contracts_vendor_v2(max_creation_date=max_creation_date, min_expiration_date=min_expiration_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_contracts_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    max_creation_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
min_expiration_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.get_contracts_vendor_v2(max_creation_date=max_creation_date, min_expiration_date=min_expiration_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_contracts_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_creation_date** | **datetime**|  | [optional] 
 **min_expiration_date** | **datetime**|  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_vendor_v2**
> object get_currency_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_currency_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_currency_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_currency_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_currency_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_contract_settings_manufaturer_v3**
> GetCustomerContractSettingsApiResponse get_customer_contract_settings_manufaturer_v3(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_customer_contract_settings_manufaturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_customer_contract_settings_manufaturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_customer_contract_settings_manufaturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_customer_contract_settings_manufaturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetCustomerContractSettingsApiResponse**](GetCustomerContractSettingsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings for this contract. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_contract_settings_vendor_v3**
> GetCustomerContractSettingsApiResponse get_customer_contract_settings_vendor_v3(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_customer_contract_settings_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_customer_contract_settings_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_customer_contract_settings_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_customer_contract_settings_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetCustomerContractSettingsApiResponse**](GetCustomerContractSettingsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings for this contract. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domains_vendor_v2**
> object get_domains_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_domains_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_domains_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_domains_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_domains_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of configured domains is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dynamic_monitoring_settings**
> object get_dynamic_monitoring_settings(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_dynamic_monitoring_settings(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_dynamic_monitoring_settings: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_dynamic_monitoring_settings(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_dynamic_monitoring_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ebay_authorizations_vendor_v2**
> object get_ebay_authorizations_vendor_v2(contract_id, auth_ids)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
auth_ids = 'auth_ids_example' # str | 

    try:
        api_response = api_instance.get_ebay_authorizations_vendor_v2(contract_id, auth_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_ebay_authorizations_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
auth_ids = 'auth_ids_example' # str | 

    try:
        api_response = api_instance.get_ebay_authorizations_vendor_v2(contract_id, auth_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_ebay_authorizations_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **auth_ids** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_tags_manufacturer_v3**
> object get_extended_tags_manufacturer_v3(contract_id, product_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 

    try:
        api_response = api_instance.get_extended_tags_manufacturer_v3(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_extended_tags_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 

    try:
        api_response = api_instance.get_extended_tags_manufacturer_v3(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_extended_tags_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **product_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_export_delta_vendor_v2**
> object get_feed_export_delta_vendor_v2(contract_id, feed_id, file_name=file_name)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
feed_id = 'feed_id_example' # str | 
file_name = 'file_name_example' # str |  (optional)

    try:
        api_response = api_instance.get_feed_export_delta_vendor_v2(contract_id, feed_id, file_name=file_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_feed_export_delta_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
feed_id = 'feed_id_example' # str | 
file_name = 'file_name_example' # str |  (optional)

    try:
        api_response = api_instance.get_feed_export_delta_vendor_v2(contract_id, feed_id, file_name=file_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_feed_export_delta_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **feed_id** | **str**|  | 
 **file_name** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_feed_export_vendor_v2**
> object get_feed_export_vendor_v2(contract_id, feed_id, file_name=file_name)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
feed_id = 'feed_id_example' # str | 
file_name = 'file_name_example' # str |  (optional)

    try:
        api_response = api_instance.get_feed_export_vendor_v2(contract_id, feed_id, file_name=file_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_feed_export_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
feed_id = 'feed_id_example' # str | 
file_name = 'file_name_example' # str |  (optional)

    try:
        api_response = api_instance.get_feed_export_vendor_v2(contract_id, feed_id, file_name=file_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_feed_export_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **feed_id** | **str**|  | 
 **file_name** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_settings_vendor_v2**
> object get_import_settings_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_import_settings_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_import_settings_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_import_settings_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_import_settings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manufacturer_manufacturer_v2**
> object get_manufacturer_manufacturer_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_manufacturer_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_manufacturer_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_manufacturer_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_manufacturer_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manufacturer_v3**
> GetManufacturerV3ApiResponse get_manufacturer_v3(contract_id)

Get the contract information

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get the contract information
        api_response = api_instance.get_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get the contract information
        api_response = api_instance.get_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetManufacturerV3ApiResponse**](GetManufacturerV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract Information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mappings_vendor_v2**
> object get_mappings_vendor_v2(contract_id, input_type, identifiers)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
input_type = 'input_type_example' # str | 
identifiers = ['identifiers_example'] # list[str] | 

    try:
        api_response = api_instance.get_mappings_vendor_v2(contract_id, input_type, identifiers)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_mappings_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
input_type = 'input_type_example' # str | 
identifiers = ['identifiers_example'] # list[str] | 

    try:
        api_response = api_instance.get_mappings_vendor_v2(contract_id, input_type, identifiers)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_mappings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **input_type** | **str**|  | 
 **identifiers** | [**list[str]**](str.md)|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketplace_activation_status**
> ActivateMarketplaceResponseV3ApiResponse get_marketplace_activation_status(marketplace_country_code, company_id, contract_id)

Get marketplace activation status of a customer in our system. 

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    marketplace_country_code = 'DE' # str | Marketplace country code. You can view complete list here. https://developer-docs.amazon.com/sp-api/docs/marketplace-ids. Currently, only Europe as a region is supported.
company_id = 1 # int | ID of a company
contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get marketplace activation status of a customer in our system. 
        api_response = api_instance.get_marketplace_activation_status(marketplace_country_code, company_id, contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_marketplace_activation_status: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    marketplace_country_code = 'DE' # str | Marketplace country code. You can view complete list here. https://developer-docs.amazon.com/sp-api/docs/marketplace-ids. Currently, only Europe as a region is supported.
company_id = 1 # int | ID of a company
contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get marketplace activation status of a customer in our system. 
        api_response = api_instance.get_marketplace_activation_status(marketplace_country_code, company_id, contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_marketplace_activation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **marketplace_country_code** | **str**| Marketplace country code. You can view complete list here. https://developer-docs.amazon.com/sp-api/docs/marketplace-ids. Currently, only Europe as a region is supported. | 
 **company_id** | **int**| ID of a company | 
 **contract_id** | **str**| ID of the contract | 

### Return type

[**ActivateMarketplaceResponseV3ApiResponse**](ActivateMarketplaceResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marketplace activation status. |  -  |
**400** | - Specified marketplace already activated. - Invalid marketplace country code is specified. - Given company is not registered with our system. One must register his seller central account with our system.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_schedules_manufacturer_v3**
> GetMonitoringSchedulesApiResponse get_monitoring_schedules_manufacturer_v3(contract_id)

Get all the monitoring schedules for a specified contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the monitoring schedules for a specified contract.
        api_response = api_instance.get_monitoring_schedules_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_schedules_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the monitoring schedules for a specified contract.
        api_response = api_instance.get_monitoring_schedules_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_schedules_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetMonitoringSchedulesApiResponse**](GetMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of monitoring schedules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_schedules_vendor_v3**
> GetMonitoringSchedulesApiResponse get_monitoring_schedules_vendor_v3(contract_id)

Get all the monitoring schedules for a specified contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the monitoring schedules for a specified contract.
        api_response = api_instance.get_monitoring_schedules_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_schedules_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the monitoring schedules for a specified contract.
        api_response = api_instance.get_monitoring_schedules_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_schedules_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetMonitoringSchedulesApiResponse**](GetMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of monitoring schedules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_settings_manufacturer_v2**
> object get_monitoring_settings_manufacturer_v2(contract_id)



Get the current monitoring settings for a given contract

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_monitoring_settings_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_settings_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_monitoring_settings_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_settings_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current monitoring settings object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_settings_manufacturer_v3**
> object get_monitoring_settings_manufacturer_v3(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_monitoring_settings_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_settings_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_monitoring_settings_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_settings_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_settings_vendor_v2**
> object get_monitoring_settings_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_monitoring_settings_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_settings_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_monitoring_settings_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_settings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitoring_settings_vendor_v3**
> object get_monitoring_settings_vendor_v3(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_monitoring_settings_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_settings_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_monitoring_settings_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_monitoring_settings_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_filters_vendor_v2**
> object get_offer_filters_vendor_v2(contract_id, list_type)

Get all the vendor filters for the given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all the vendor filters for the given contract.
        api_response = api_instance.get_offer_filters_vendor_v2(contract_id, list_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offer_filters_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 

    try:
        # Get all the vendor filters for the given contract.
        api_response = api_instance.get_offer_filters_vendor_v2(contract_id, list_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the filters to ignore the individual offers. Offers are filtered against vendor name either for all the domain or for a specific domain. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_retention_settings_manufacturer_v3**
> object get_offer_retention_settings_manufacturer_v3(contract_id, contract_type)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
contract_type = 'contract_type_example' # str | 

    try:
        api_response = api_instance.get_offer_retention_settings_manufacturer_v3(contract_id, contract_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offer_retention_settings_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
contract_type = 'contract_type_example' # str | 

    try:
        api_response = api_instance.get_offer_retention_settings_manufacturer_v3(contract_id, contract_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offer_retention_settings_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **contract_type** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_retention_settings_vendor_v3**
> object get_offer_retention_settings_vendor_v3(contract_id, contract_type)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
contract_type = 'contract_type_example' # str | 

    try:
        api_response = api_instance.get_offer_retention_settings_vendor_v3(contract_id, contract_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offer_retention_settings_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
contract_type = 'contract_type_example' # str | 

    try:
        api_response = api_instance.get_offer_retention_settings_vendor_v3(contract_id, contract_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offer_retention_settings_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **contract_type** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer_statistics_manufacturer_v3**
> GetOfferStatisticsV3ApiResponse get_offer_statistics_manufacturer_v3(contract_id, include_delivery_costs, start_date=start_date, end_date=end_date)

Get offer statistics per product of a contract

Get offer statistics per product of a contract. Only the latest offers per product and domain the are taken into account.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
include_delivery_costs = True # bool | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        # Get offer statistics per product of a contract
        api_response = api_instance.get_offer_statistics_manufacturer_v3(contract_id, include_delivery_costs, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offer_statistics_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
include_delivery_costs = True # bool | 
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        # Get offer statistics per product of a contract
        api_response = api_instance.get_offer_statistics_manufacturer_v3(contract_id, include_delivery_costs, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offer_statistics_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **include_delivery_costs** | **bool**|  | 
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 

### Return type

[**GetOfferStatisticsV3ApiResponse**](GetOfferStatisticsV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of offer statistics per product. |  -  |
**400** | Specified time range is invalid (&gt; 48h). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offers_shops_manufacturer_v3**
> GetShopsByDomainResponseV3ApiResponse get_offers_shops_manufacturer_v3(contract_id, start_date=start_date, end_date=end_date)

Get shops with offers for time range

Returns all shops which have at least one offer for a given time range per domain.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Get shops with offers for time range
        api_response = api_instance.get_offers_shops_manufacturer_v3(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offers_shops_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Get shops with offers for time range
        api_response = api_instance.get_offers_shops_manufacturer_v3(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offers_shops_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. The time range may not exceed 1 week. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. The time range may not exceed 1 week. | [optional] 

### Return type

[**GetShopsByDomainResponseV3ApiResponse**](GetShopsByDomainResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shops which have at least one offer for a given time range per domain. |  -  |
**400** | Specified time range is invalid (&gt; 7 days). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offers_shops_vendor_v3**
> GetShopsByDomainResponseV3ApiResponse get_offers_shops_vendor_v3(contract_id, start_date=start_date, end_date=end_date)

Get shops with offers for time range per domain

Returns all shops which have at least one offer for a given time range per domain.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Get shops with offers for time range per domain
        api_response = api_instance.get_offers_shops_vendor_v3(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offers_shops_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. The time range may not exceed 1 week. (optional)

    try:
        # Get shops with offers for time range per domain
        api_response = api_instance.get_offers_shops_vendor_v3(contract_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offers_shops_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. The time range may not exceed 1 week. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. The time range may not exceed 1 week. | [optional] 

### Return type

[**GetShopsByDomainResponseV3ApiResponse**](GetShopsByDomainResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shops which have at least one offer for a given time range per domain. |  -  |
**400** | Specified time range is invalid (&gt; 7 days). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_count_by_portal_by_contract**
> object get_orders_count_by_portal_by_contract(contract_id)

Get orders count by portal

Get the number of orders by portal for the given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get orders count by portal
        api_response = api_instance.get_orders_count_by_portal_by_contract(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_orders_count_by_portal_by_contract: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get orders count by portal
        api_response = api_instance.get_orders_count_by_portal_by_contract(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_orders_count_by_portal_by_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_cutters_manufacturer_v2**
> object get_price_cutters_manufacturer_v2(contract_id, session, limit, include_delivery_costs, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_price_cutters_manufacturer_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_price_cutters_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_price_cutters_manufacturer_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_price_cutters_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **session** | **datetime**|  | 
 **limit** | **int**|  | 
 **include_delivery_costs** | **bool**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_cutters_vendor_v2**
> object get_price_cutters_vendor_v2(contract_id, session, limit, include_delivery_costs, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_price_cutters_vendor_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_price_cutters_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | 
limit = 56 # int | 
include_delivery_costs = True # bool | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_price_cutters_vendor_v2(contract_id, session, limit, include_delivery_costs, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_price_cutters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **session** | **datetime**|  | 
 **limit** | **int**|  | 
 **include_delivery_costs** | **bool**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_recommendation_stats_vendor_v2**
> object get_price_recommendation_stats_vendor_v2(contract_id, start_time, end_time, max_positions)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 
max_positions = 56 # int | 

    try:
        api_response = api_instance.get_price_recommendation_stats_vendor_v2(contract_id, start_time, end_time, max_positions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_price_recommendation_stats_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start_time = '2013-10-20T19:20:30+01:00' # datetime | 
end_time = '2013-10-20T19:20:30+01:00' # datetime | 
max_positions = 56 # int | 

    try:
        api_response = api_instance.get_price_recommendation_stats_vendor_v2(contract_id, start_time, end_time, max_positions)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_price_recommendation_stats_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start_time** | **datetime**|  | 
 **end_time** | **datetime**|  | 
 **max_positions** | **int**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_filters_by_id_vendor_v2**
> object get_product_filters_by_id_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_product_filters_by_id_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_filters_by_id_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_product_filters_by_id_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_filters_by_id_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_filters_by_range_vendor_v2**
> object get_product_filters_by_range_vendor_v2(contract_id, list_type, start, limit)

Get all the filters product-wise for the given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
start = 56 # int | 
limit = 56 # int | 

    try:
        # Get all the filters product-wise for the given contract.
        api_response = api_instance.get_product_filters_by_range_vendor_v2(contract_id, list_type, start, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_filters_by_range_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
start = 56 # int | 
limit = 56 # int | 

    try:
        # Get all the filters product-wise for the given contract.
        api_response = api_instance.get_product_filters_by_range_vendor_v2(contract_id, list_type, start, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_filters_by_range_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 
 **start** | **int**|  | 
 **limit** | **int**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the filters per product to ignore the individual offers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_filters_vendor_v2**
> OfferFilterApiResponse get_product_filters_vendor_v2(contract_id, list_type, product_id)

Get all the filters of a given product for the given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
product_id = 'product_id_example' # str | 

    try:
        # Get all the filters of a given product for the given contract.
        api_response = api_instance.get_product_filters_vendor_v2(contract_id, list_type, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_filters_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
product_id = 'product_id_example' # str | 

    try:
        # Get all the filters of a given product for the given contract.
        api_response = api_instance.get_product_filters_vendor_v2(contract_id, list_type, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 
 **product_id** | **str**|  | 

### Return type

[**OfferFilterApiResponse**](OfferFilterApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the filters to ignore the individual offers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_metrics_by_contract**
> object get_product_metrics_by_contract(contract_id, start, end)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        api_response = api_instance.get_product_metrics_by_contract(contract_id, start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_metrics_by_contract: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 

    try:
        api_response = api_instance.get_product_metrics_by_contract(contract_id, start, end)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_metrics_by_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_monitoring_status_stats_vendor_v3**
> GetProductMonitoringStatusStatsVendorV3ApiResponse get_product_monitoring_status_stats_vendor_v3(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_product_monitoring_status_stats_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_monitoring_status_stats_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_product_monitoring_status_stats_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_monitoring_status_stats_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetProductMonitoringStatusStatsVendorV3ApiResponse**](GetProductMonitoringStatusStatsVendorV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains the monitoring status stats per domain |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_price_violations_manufacturer_v2**
> object get_product_price_violations_manufacturer_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        api_response = api_instance.get_product_price_violations_manufacturer_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_price_violations_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        api_response = api_instance.get_product_price_violations_manufacturer_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_price_violations_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 
 **include_delivery_costs** | **bool**|  | 
 **reference_price_delta** | **float**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_price_violations_vendor_v2**
> object get_product_price_violations_vendor_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        api_response = api_instance.get_product_price_violations_vendor_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_price_violations_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = '2013-10-20T19:20:30+01:00' # datetime | 
end = '2013-10-20T19:20:30+01:00' # datetime | 
include_delivery_costs = True # bool | 
reference_price_delta = 3.4 # float | 

    try:
        api_response = api_instance.get_product_price_violations_vendor_v2(contract_id, start, end, include_delivery_costs, reference_price_delta)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_price_violations_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **datetime**|  | 
 **end** | **datetime**|  | 
 **include_delivery_costs** | **bool**|  | 
 **reference_price_delta** | **float**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repricing_strategy_vendor_v2**
> object get_repricing_strategy_vendor_v2(contract_id, document_version=document_version)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
document_version = 5 # int |  (optional)

    try:
        api_response = api_instance.get_repricing_strategy_vendor_v2(contract_id, document_version=document_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_repricing_strategy_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
document_version = 5 # int |  (optional)

    try:
        api_response = api_instance.get_repricing_strategy_vendor_v2(contract_id, document_version=document_version)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_repricing_strategy_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **document_version** | **int**|  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | In case a document version is provided, get that strategy version. Otherwise get latest strategy for this contract. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scenario_by_id**
> ScenarioStrategyResponse get_scenario_by_id(contract_id, scenario_id)

Get a strategy scenario with the provided scenario Id

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
scenario_id = 56 # int | ID of the required strategy scenario

    try:
        # Get a strategy scenario with the provided scenario Id
        api_response = api_instance.get_scenario_by_id(contract_id, scenario_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_scenario_by_id: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
scenario_id = 56 # int | ID of the required strategy scenario

    try:
        # Get a strategy scenario with the provided scenario Id
        api_response = api_instance.get_scenario_by_id(contract_id, scenario_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_scenario_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **scenario_id** | **int**| ID of the required strategy scenario | 

### Return type

[**ScenarioStrategyResponse**](ScenarioStrategyResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A strategy scenario |  -  |
**404** | Strategy scenario with the provided Id was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1 get_settings(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_settings(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_settings: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_settings(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1**](ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_values_manufacturer_v2**
> object get_tag_values_manufacturer_v2(contract_id, key)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
key = 'key_example' # str | 

    try:
        api_response = api_instance.get_tag_values_manufacturer_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tag_values_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
key = 'key_example' # str | 

    try:
        api_response = api_instance.get_tag_values_manufacturer_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tag_values_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **key** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_values_vendor_v2**
> object get_tag_values_vendor_v2(contract_id, key)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
key = 'key_example' # str | 

    try:
        api_response = api_instance.get_tag_values_vendor_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tag_values_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
key = 'key_example' # str | 

    try:
        api_response = api_instance.get_tag_values_vendor_v2(contract_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tag_values_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **key** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_manufacturer_v2**
> object get_tags_manufacturer_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_tags_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tags_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_tags_manufacturer_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tags_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_vendor_v2**
> object get_tags_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_tags_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tags_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_tags_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tags_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> object get_task(contract_id, task_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_data_manufacturer_v2**
> object get_task_data_manufacturer_v2(contract_id, task_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_data_manufacturer_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task_data_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_data_manufacturer_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task_data_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payload data of the requested task is returned |  -  |
**404** | The task with the given ID could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_data_vendor_v2**
> object get_task_data_vendor_v2(contract_id, task_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_data_vendor_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task_data_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_data_vendor_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task_data_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_manufacturer_v2**
> GenericTask get_task_manufacturer_v2(contract_id, task_id)



Get the task designated by the taskId parameter

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_manufacturer_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_manufacturer_v2(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

[**GenericTask**](GenericTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The task was found and is returned |  -  |
**404** | No task with given taskId was found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_state**
> object get_task_state(contract_id, task_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_state(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task_state: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 

    try:
        api_response = api_instance.get_task_state(contract_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_task_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> object get_tasks(contract_id, tasks, attributes, limit, task_type=task_type)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
tasks = 'tasks_example' # str | 
attributes = 'attributes_example' # str | 
limit = 56 # int | 
task_type = 'task_type_example' # str |  (optional)

    try:
        api_response = api_instance.get_tasks(contract_id, tasks, attributes, limit, task_type=task_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tasks: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
tasks = 'tasks_example' # str | 
attributes = 'attributes_example' # str | 
limit = 56 # int | 
task_type = 'task_type_example' # str |  (optional)

    try:
        api_response = api_instance.get_tasks(contract_id, tasks, attributes, limit, task_type=task_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **tasks** | **str**|  | 
 **attributes** | **str**|  | 
 **limit** | **int**|  | 
 **task_type** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_manufacturer_v2**
> list[GenericTask] get_tasks_manufacturer_v2(contract_id, task_type_filter, task_state, limit, include_failures, task_ids_filter=task_ids_filter, min_creation_date=min_creation_date, max_creation_date=max_creation_date)



Returns a list of task objects for the given contract

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_type_filter = ['task_type_filter_example'] # list[str] | A list of task types to filter for
task_state = ['task_state_example'] # list[str] | A list of task states to filter for
limit = 100 # int | The maximum number of tasks returned (default to 100)
include_failures = True # bool | Include failed tasks (default to True)
task_ids_filter = 'task_ids_filter_example' # str | Comma separated list of task IDs to filter for (optional)
min_creation_date = '2013-10-20T19:20:30+01:00' # datetime | Ignore all tasks created earlier than this date (ISO 8601) (optional)
max_creation_date = '2013-10-20T19:20:30+01:00' # datetime | Ignore all tasks created later than this date (ISO 8601) (optional)

    try:
        api_response = api_instance.get_tasks_manufacturer_v2(contract_id, task_type_filter, task_state, limit, include_failures, task_ids_filter=task_ids_filter, min_creation_date=min_creation_date, max_creation_date=max_creation_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tasks_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_type_filter = ['task_type_filter_example'] # list[str] | A list of task types to filter for
task_state = ['task_state_example'] # list[str] | A list of task states to filter for
limit = 100 # int | The maximum number of tasks returned (default to 100)
include_failures = True # bool | Include failed tasks (default to True)
task_ids_filter = 'task_ids_filter_example' # str | Comma separated list of task IDs to filter for (optional)
min_creation_date = '2013-10-20T19:20:30+01:00' # datetime | Ignore all tasks created earlier than this date (ISO 8601) (optional)
max_creation_date = '2013-10-20T19:20:30+01:00' # datetime | Ignore all tasks created later than this date (ISO 8601) (optional)

    try:
        api_response = api_instance.get_tasks_manufacturer_v2(contract_id, task_type_filter, task_state, limit, include_failures, task_ids_filter=task_ids_filter, min_creation_date=min_creation_date, max_creation_date=max_creation_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tasks_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_type_filter** | [**list[str]**](str.md)| A list of task types to filter for | 
 **task_state** | [**list[str]**](str.md)| A list of task states to filter for | 
 **limit** | **int**| The maximum number of tasks returned | [default to 100]
 **include_failures** | **bool**| Include failed tasks | [default to True]
 **task_ids_filter** | **str**| Comma separated list of task IDs to filter for | [optional] 
 **min_creation_date** | **datetime**| Ignore all tasks created earlier than this date (ISO 8601) | [optional] 
 **max_creation_date** | **datetime**| Ignore all tasks created later than this date (ISO 8601) | [optional] 

### Return type

[**list[GenericTask]**](GenericTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of tasks for the given contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_stats**
> object get_tasks_stats(since_seconds)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    since_seconds = 56 # int | 

    try:
        api_response = api_instance.get_tasks_stats(since_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tasks_stats: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    since_seconds = 56 # int | 

    try:
        api_response = api_instance.get_tasks_stats(since_seconds)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_tasks_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since_seconds** | **int**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_stamps**
> object get_time_stamps(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 56 # int | 

    try:
        api_response = api_instance.get_time_stamps(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_time_stamps: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 56 # int | 

    try:
        api_response = api_instance.get_time_stamps(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_time_stamps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> object get_user(email)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    email = 'email_example' # str | 

    try:
        api_response = api_instance.get_user(email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_user: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    email = 'email_example' # str | 

    try:
        api_response = api_instance.get_user(email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> object get_users(company_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company

    try:
        api_response = api_instance.get_users(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_users: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company

    try:
        api_response = api_instance.get_users(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_settings_v2_vendor_v2**
> object get_vendor_settings_v2_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_vendor_settings_v2_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_settings_v2_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_vendor_settings_v2_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_settings_v2_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_shop_mapping_manufacturer_v3**
> VendorShopMappingV3ApiResponse get_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)

Get vendor along with their associated shop for given vendor id and contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping

    try:
        # Get vendor along with their associated shop for given vendor id and contract.
        api_response = api_instance.get_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping

    try:
        # Get vendor along with their associated shop for given vendor id and contract.
        api_response = api_instance.get_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **vendor_id** | **int**| ID of vendor shop mapping | 

### Return type

[**VendorShopMappingV3ApiResponse**](VendorShopMappingV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get vendor along with their associated shop for given vendor id and contract. |  -  |
**404** | Vendor doesn&#39;t exist for given vendor id. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_shop_mappings_manufacturer_v3**
> GetVendorShopMappingsApiResponse get_vendor_shop_mappings_manufacturer_v3(contract_id)

Get all the vendors along with their associated shops for a specified contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the vendors along with their associated shops for a specified contract.
        api_response = api_instance.get_vendor_shop_mappings_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_shop_mappings_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        # Get all the vendors along with their associated shops for a specified contract.
        api_response = api_instance.get_vendor_shop_mappings_manufacturer_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_shop_mappings_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**GetVendorShopMappingsApiResponse**](GetVendorShopMappingsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of vendors along with their associated shops. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_v3**
> object get_vendor_v3(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_vendor_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_vendor_v2**
> object get_vendor_vendor_v2(contract_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_vendor_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract

    try:
        api_response = api_instance.get_vendor_vendor_v2(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendor_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendors_by_domain_manufacturer_v2**
> ComPatagonaPricemonitorShareApiPostVendorsByDomainResponse get_vendors_by_domain_manufacturer_v2(contract_id, domain, start, include_delivery_costs, session, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
domain = 'domain_example' # str | 
start = 56 # int | 
include_delivery_costs = True # bool | 
session = '2013-10-20T19:20:30+01:00' # datetime | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_vendors_by_domain_manufacturer_v2(contract_id, domain, start, include_delivery_costs, session, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendors_by_domain_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
domain = 'domain_example' # str | 
start = 56 # int | 
include_delivery_costs = True # bool | 
session = '2013-10-20T19:20:30+01:00' # datetime | 
com_patagona_pricemonitor_share_api_tag_filtered_vendors_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest() # ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.get_vendors_by_domain_manufacturer_v2(contract_id, domain, start, include_delivery_costs, session, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_vendors_by_domain_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **domain** | **str**|  | 
 **start** | **int**|  | 
 **include_delivery_costs** | **bool**|  | 
 **session** | **datetime**|  | 
 **com_patagona_pricemonitor_share_api_tag_filtered_vendors_request** | [**ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest**](ComPatagonaPricemonitorShareApiTagFilteredVendorsRequest.md)| This is a generated entry and needs to be described. | [optional] 

### Return type

[**ComPatagonaPricemonitorShareApiPostVendorsByDomainResponse**](ComPatagonaPricemonitorShareApiPostVendorsByDomainResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vendors**
> object list_vendors(name_filter)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    name_filter = 'name_filter_example' # str | 

    try:
        api_response = api_instance.list_vendors(name_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->list_vendors: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    name_filter = 'name_filter_example' # str | 

    try:
        api_response = api_instance.list_vendors(name_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->list_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_filter** | **str**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_by_auth_token**
> object login_by_auth_token(token)



### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    token = 'token_example' # str | 

    try:
        api_response = api_instance.login_by_auth_token(token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->login_by_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> object logout()



### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        api_response = api_instance.logout()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deauthenticate with the API and destroy the current session. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitoring_pipeline_post_request_manufacturer_v3**
> object monitoring_pipeline_post_request_manufacturer_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The monitoring-pipeline path to be called

    try:
        api_response = api_instance.monitoring_pipeline_post_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->monitoring_pipeline_post_request_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The monitoring-pipeline path to be called

    try:
        api_response = api_instance.monitoring_pipeline_post_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->monitoring_pipeline_post_request_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The monitoring-pipeline path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitoring_pipeline_post_request_vendor_v3**
> object monitoring_pipeline_post_request_vendor_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The monitoring-pipeline path to be called

    try:
        api_response = api_instance.monitoring_pipeline_post_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->monitoring_pipeline_post_request_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The monitoring-pipeline path to be called

    try:
        api_response = api_instance.monitoring_pipeline_post_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->monitoring_pipeline_post_request_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The monitoring-pipeline path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitoring_pipeline_upsert_search_attempts_manufacturer_v3**
> object monitoring_pipeline_upsert_search_attempts_manufacturer_v3(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->monitoring_pipeline_upsert_search_attempts_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->monitoring_pipeline_upsert_search_attempts_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitoring_pipeline_upsert_search_attempts_vendor_v3**
> object monitoring_pipeline_upsert_search_attempts_vendor_v3(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_vendor_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->monitoring_pipeline_upsert_search_attempts_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.monitoring_pipeline_upsert_search_attempts_vendor_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->monitoring_pipeline_upsert_search_attempts_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_product_manufacturer_v3**
> object patch_product_manufacturer_v3(contract_id, product_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.patch_product_manufacturer_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->patch_product_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.patch_product_manufacturer_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->patch_product_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **product_id** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_product_vendor_v3**
> object patch_product_vendor_v3(contract_id, product_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.patch_product_vendor_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->patch_product_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.patch_product_vendor_v3(contract_id, product_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->patch_product_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **product_id** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **position_distribution**
> object position_distribution(contract_id, vendor, day, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor = 'vendor_example' # str | 
day = '2013-10-20T19:20:30+01:00' # datetime | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.position_distribution(contract_id, vendor, day, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->position_distribution: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor = 'vendor_example' # str | 
day = '2013-10-20T19:20:30+01:00' # datetime | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.position_distribution(contract_id, vendor, day, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->position_distribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **vendor** | **str**|  | 
 **day** | **datetime**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_account_v3**
> PostAccountResponseV3ApiResponse post_account_v3(com_patagona_pricemonitor_share_api_post_account_request_v3=com_patagona_pricemonitor_share_api_post_account_request_v3)

Create a new user account

### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    com_patagona_pricemonitor_share_api_post_account_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAccountRequestV3() # ComPatagonaPricemonitorShareApiPostAccountRequestV3 | Request body for creating a new user account. It must contain name, email and password. (optional)

    try:
        # Create a new user account
        api_response = api_instance.post_account_v3(com_patagona_pricemonitor_share_api_post_account_request_v3=com_patagona_pricemonitor_share_api_post_account_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_account_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_post_account_request_v3** | [**ComPatagonaPricemonitorShareApiPostAccountRequestV3**](ComPatagonaPricemonitorShareApiPostAccountRequestV3.md)| Request body for creating a new user account. It must contain name, email and password. | [optional] 

### Return type

[**PostAccountResponseV3ApiResponse**](PostAccountResponseV3ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The account information of the newly created account. |  -  |
**400** | Returned if: - The Request body is not a valid JSON string - The user account name is empty - The email doesn&#39;t match a valid email format - The password length is less than 6 characters long - The enpoint was requested too often - The given email address already exists  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_activate_marketplace_vendor_v3**
> ActivateMarketplaceResponseV3ApiResponse post_activate_marketplace_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3=com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3)

Activate marketplace of a customer in our system. By activation, it means that our system can write prices back into the customer's Amazon shop. 

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company
com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3() # ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3 | Marketplace of a customer to be activated. (optional)

    try:
        # Activate marketplace of a customer in our system. By activation, it means that our system can write prices back into the customer's Amazon shop. 
        api_response = api_instance.post_activate_marketplace_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3=com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_activate_marketplace_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company
com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3() # ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3 | Marketplace of a customer to be activated. (optional)

    try:
        # Activate marketplace of a customer in our system. By activation, it means that our system can write prices back into the customer's Amazon shop. 
        api_response = api_instance.post_activate_marketplace_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3=com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_activate_marketplace_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 
 **com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3** | [**ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3**](ComPatagonaPricemonitorShareApiPostActivateMarketplaceRequestV3.md)| Marketplace of a customer to be activated. | [optional] 

### Return type

[**ActivateMarketplaceResponseV3ApiResponse**](ActivateMarketplaceResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully activated marketplace of a customer in our system. |  -  |
**400** | - Specified marketplace already activated. - Invalid marketplace country code is specified. - Given company is not registered with our system. One must register his seller central account with our system.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_authorize_seller_vendor_v3**
> PostAuthorizeSellerResponseV3ApiResponse post_authorize_seller_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3=com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3)

Set up an OAuth authorization for a customer's Amazon Seller Central account. It establishes a connection between our system and the customer's Amazon shop using the Amazon SP-API. Once connected, our system can write prices back to the customer's Amazon shop, allowing them to benefit from our price recommendations. 

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company
com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3() # ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3 | Customer's Amazon seller central account to be authorized. (optional)

    try:
        # Set up an OAuth authorization for a customer's Amazon Seller Central account. It establishes a connection between our system and the customer's Amazon shop using the Amazon SP-API. Once connected, our system can write prices back to the customer's Amazon shop, allowing them to benefit from our price recommendations. 
        api_response = api_instance.post_authorize_seller_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3=com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_authorize_seller_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company
com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3() # ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3 | Customer's Amazon seller central account to be authorized. (optional)

    try:
        # Set up an OAuth authorization for a customer's Amazon Seller Central account. It establishes a connection between our system and the customer's Amazon shop using the Amazon SP-API. Once connected, our system can write prices back to the customer's Amazon shop, allowing them to benefit from our price recommendations. 
        api_response = api_instance.post_authorize_seller_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3=com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_authorize_seller_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 
 **com_patagona_pricemonitor_share_api_post_authorize_seller_request_v3** | [**ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3**](ComPatagonaPricemonitorShareApiPostAuthorizeSellerRequestV3.md)| Customer&#39;s Amazon seller central account to be authorized. | [optional] 

### Return type

[**PostAuthorizeSellerResponseV3ApiResponse**](PostAuthorizeSellerResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully authorized customer&#39;s Amazon seller central account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ebay_authorization_vendor_v2**
> object post_ebay_authorization_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.post_ebay_authorization_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_ebay_authorization_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.post_ebay_authorization_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_ebay_authorization_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_embed_sso_url_manufacturer**
> EmbedSSOUrlResponseV3ApiResponse post_embed_sso_url_manufacturer(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)

Retrieve an embed SSO url for Looker.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3() # ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3 | Payload for retrieving a signed embed SSO url using Looker API. (optional)

    try:
        # Retrieve an embed SSO url for Looker.
        api_response = api_instance.post_embed_sso_url_manufacturer(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_embed_sso_url_manufacturer: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3() # ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3 | Payload for retrieving a signed embed SSO url using Looker API. (optional)

    try:
        # Retrieve an embed SSO url for Looker.
        api_response = api_instance.post_embed_sso_url_manufacturer(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_embed_sso_url_manufacturer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3** | [**ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3**](ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3.md)| Payload for retrieving a signed embed SSO url using Looker API. | [optional] 

### Return type

[**EmbedSSOUrlResponseV3ApiResponse**](EmbedSSOUrlResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signed embed SSO url for Looker. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_embed_sso_url_vendor**
> EmbedSSOUrlResponseV3ApiResponse post_embed_sso_url_vendor(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)

Retrieve an embed SSO url for Looker.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3() # ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3 | Payload for retrieving a signed embed SSO url using Looker API. (optional)

    try:
        # Retrieve an embed SSO url for Looker.
        api_response = api_instance.post_embed_sso_url_vendor(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_embed_sso_url_vendor: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3() # ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3 | Payload for retrieving a signed embed SSO url using Looker API. (optional)

    try:
        # Retrieve an embed SSO url for Looker.
        api_response = api_instance.post_embed_sso_url_vendor(contract_id, com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3=com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_embed_sso_url_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_embed_sso_url_request_v3** | [**ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3**](ComPatagonaPricemonitorShareApiPostEmbedSSOUrlRequestV3.md)| Payload for retrieving a signed embed SSO url using Looker API. | [optional] 

### Return type

[**EmbedSSOUrlResponseV3ApiResponse**](EmbedSSOUrlResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signed embed SSO url for Looker. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_feed_vendor_v2**
> object post_feed_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.post_feed_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_feed_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.post_feed_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_feed_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_mappings_vendor_v2**
> object post_mappings_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.post_mappings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_mappings_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.post_mappings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_mappings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_monitoring_schedule_manufacturer_v3**
> PutMonitoringSchedulesApiResponse post_monitoring_schedule_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)

Add a monitoring schedule for a given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add a monitoring schedule for a given contract.
        api_response = api_instance.post_monitoring_schedule_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add a monitoring schedule for a given contract.
        api_response = api_instance.post_monitoring_schedule_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3** | [**ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3**](ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3.md)| Request body for creating monitoring schedule. | [optional] 

### Return type

[**PutMonitoringSchedulesApiResponse**](PutMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monitoring schedule has been created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_monitoring_schedule_vendor_v3**
> PutMonitoringSchedulesApiResponse post_monitoring_schedule_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)

Add a monitoring schedule for a given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add a monitoring schedule for a given contract.
        api_response = api_instance.post_monitoring_schedule_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_monitoring_schedule_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for creating monitoring schedule. (optional)

    try:
        # Add a monitoring schedule for a given contract.
        api_response = api_instance.post_monitoring_schedule_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3** | [**ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3**](ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3.md)| Request body for creating monitoring schedule. | [optional] 

### Return type

[**PutMonitoringSchedulesApiResponse**](PutMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Monitoring schedule has been created successfully. |  -  |
**503** | Monitoring schedule could not be created due to an internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_offer_statistics_vendor_query**
> PostOfferStatisticsApiResponse post_offer_statistics_vendor_query(contract_id, post_offer_statistics_request)



This operation is used to get offer statistics (e.g. offer count, average price) grouped by product and domain.  Warning: This endpoint contains complex filter structure and will be replaced in the future. Currently, we only allow filtering by a list of internal pricemonitor product ids. Please note that offer statistics can only be computed for at **maximum 2500** products at a time.  To use the example request body from below, you have to adjust the `ownShopNames`, the `range` and `filter.right.value`. Where `filter.right.value` has to be a list of internal pricemonitor product ids corresponding to the `contractId` provided as part of the URL.  All prices will be with or without delivery costs depending on the `includeDeliveryCosts` parameter in the body. 

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        api_response = api_instance.post_offer_statistics_vendor_query(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_offer_statistics_vendor_query: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        api_response = api_instance.post_offer_statistics_vendor_query(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_offer_statistics_vendor_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **post_offer_statistics_request** | [**PostOfferStatisticsRequest**](PostOfferStatisticsRequest.md)|  | 

### Return type

[**PostOfferStatisticsApiResponse**](PostOfferStatisticsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of offer statistics per product. ## How to use this endpoint&#39;s result to get Total Market statistics ### Minimum Price To calculate the minimum price in the total market, you have to take the minimum of the &#x60;minPrice&#x60; of each domain. In the example below, both products have the same min prices: &#x60;min(16.00,7.99) &#x3D; 7.99&#x60;. ### Average Price To calculate the average price in the total market, you have to calculate a **weighted average**, weighing the average price of each domain by its offer count. In the example below we get different results for the average price in the total market for product id &#x60;1001&#x60; and &#x60;1002&#x60; even though they have the same average price in each domain. This is due to the different offer counts:    - product id &#x60;1001&#x60;: &#x60;(20.00 * 4 + 10.00 * 12) / (4 + 12) &#x3D; 12.50&#x60;   - product id &#x60;1002&#x60;: &#x60;(20.00 * 12 + 10.00 * 4) / (12 + 4) &#x3D; 17.50&#x60;  ### Offer Count The offer count of one product in the total market is the sum of the offer counts for all its domains. In the example below, both products would have an offer count of &#x60;12 + 4 &#x3D; 16&#x60;. ### Market Position The market position of a product generally **can not be deduced** from the data provided in this endpoint.  |  -  |
**400** | Returned in case of unparsable request body JSON or unsupported filter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_vendor_shop_mapping_manufacturer_v3**
> VendorShopMappingV3ApiResponse post_vendor_shop_mapping_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)

Add a new vendor for a given contract and associate shops with the given vendor.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for creating a new vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. (optional)

    try:
        # Add a new vendor for a given contract and associate shops with the given vendor.
        api_response = api_instance.post_vendor_shop_mapping_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for creating a new vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. (optional)

    try:
        # Add a new vendor for a given contract and associate shops with the given vendor.
        api_response = api_instance.post_vendor_shop_mapping_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->post_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3** | [**ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3**](ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3.md)| Request body for creating a new vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. | [optional] 

### Return type

[**VendorShopMappingV3ApiResponse**](VendorShopMappingV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vendor shop mapping has been successfully created. |  -  |
**400** | The specified vendor name is empty. Or the specified shops are empty. |  -  |
**409** | The specified vendor name already exists in our system. |  -  |
**422** | The specified shops do not exist in our system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prices_by_day_by_product_id_manufacturer_v2**
> list[ComPatagonaPricemonitorShareApiPricesByDayByProductIdResponseV2] prices_by_day_by_product_id_manufacturer_v2(contract_id, product_id, com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2=com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | The product ID to filter for
com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2() # ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2 | Query all known prices for a given day & product ID. Can be filtered by using the selectors. (optional)

    try:
        api_response = api_instance.prices_by_day_by_product_id_manufacturer_v2(contract_id, product_id, com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2=com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->prices_by_day_by_product_id_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
product_id = 'product_id_example' # str | The product ID to filter for
com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2() # ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2 | Query all known prices for a given day & product ID. Can be filtered by using the selectors. (optional)

    try:
        api_response = api_instance.prices_by_day_by_product_id_manufacturer_v2(contract_id, product_id, com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2=com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->prices_by_day_by_product_id_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **product_id** | **str**| The product ID to filter for | 
 **com_patagona_pricemonitor_share_api_prices_by_day_by_product_id_request_v2** | [**ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2**](ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2.md)| Query all known prices for a given day &amp; product ID. Can be filtered by using the selectors. | [optional] 

### Return type

[**list[ComPatagonaPricemonitorShareApiPricesByDayByProductIdResponseV2]**](ComPatagonaPricemonitorShareApiPricesByDayByProductIdResponseV2.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of all known prices for the queried day &amp; product ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_preprocessing_task_vendor_v3**
> EmptyApiResponse publish_preprocessing_task_vendor_v3(retrospective_in_minutes, contract_id, trigger_follow_up_task=trigger_follow_up_task)

Publish a preprocessing task for vendor.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    retrospective_in_minutes = 56 # int | The timespan, in minutes, for considering offers in preprocessing. Allowed value is between 1 and 10080
contract_id = 'qbcxvb' # str | ID of the contract
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Publish a preprocessing task for vendor.
        api_response = api_instance.publish_preprocessing_task_vendor_v3(retrospective_in_minutes, contract_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->publish_preprocessing_task_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    retrospective_in_minutes = 56 # int | The timespan, in minutes, for considering offers in preprocessing. Allowed value is between 1 and 10080
contract_id = 'qbcxvb' # str | ID of the contract
trigger_follow_up_task = True # bool |  (optional)

    try:
        # Publish a preprocessing task for vendor.
        api_response = api_instance.publish_preprocessing_task_vendor_v3(retrospective_in_minutes, contract_id, trigger_follow_up_task=trigger_follow_up_task)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->publish_preprocessing_task_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrospective_in_minutes** | **int**| The timespan, in minutes, for considering offers in preprocessing. Allowed value is between 1 and 10080 | 
 **contract_id** | **str**| ID of the contract | 
 **trigger_follow_up_task** | **bool**|  | [optional] 

### Return type

[**EmptyApiResponse**](EmptyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Preprocessing task created successfully |  -  |
**400** | - Invalid retrospective value. - No retrospective value is specified.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_callbacks**
> put_callbacks(contract_id, callbacks)

Set callbacks

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
callbacks = pricemonitor_api_client.Callbacks() # Callbacks | Callbacks

    try:
        # Set callbacks
        api_instance.put_callbacks(contract_id, callbacks)
    except ApiException as e:
        print("Exception when calling InternalApi->put_callbacks: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
callbacks = pricemonitor_api_client.Callbacks() # Callbacks | Callbacks

    try:
        # Set callbacks
        api_instance.put_callbacks(contract_id, callbacks)
    except ApiException as e:
        print("Exception when calling InternalApi->put_callbacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **callbacks** | [**Callbacks**](Callbacks.md)| Callbacks | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | - |  -  |
**404** | Settings for this contract don&#39;t exist yet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_callbacks_vendor_v2**
> object put_callbacks_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_callbacks_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_callbacks_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_callbacks_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_callbacks_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_complex_offer_filters_vendor_v2**
> OfferFilterApiResponse put_complex_offer_filters_vendor_v2(contract_id, list_type, and_offer_filter=and_offer_filter)

Add the complex filters for the given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
and_offer_filter = [pricemonitor_api_client.AndOfferFilter()] # list[AndOfferFilter] | List of the filter that needs to be considered to ignore the individual offers. (optional)

    try:
        # Add the complex filters for the given contract.
        api_response = api_instance.put_complex_offer_filters_vendor_v2(contract_id, list_type, and_offer_filter=and_offer_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_complex_offer_filters_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
and_offer_filter = [pricemonitor_api_client.AndOfferFilter()] # list[AndOfferFilter] | List of the filter that needs to be considered to ignore the individual offers. (optional)

    try:
        # Add the complex filters for the given contract.
        api_response = api_instance.put_complex_offer_filters_vendor_v2(contract_id, list_type, and_offer_filter=and_offer_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_complex_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 
 **and_offer_filter** | [**list[AndOfferFilter]**](AndOfferFilter.md)| List of the filter that needs to be considered to ignore the individual offers. | [optional] 

### Return type

[**OfferFilterApiResponse**](OfferFilterApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the filters that have been sent as the request body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_currency_vendor_v2**
> object put_currency_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_currency_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_currency_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_currency_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_currency_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_customer_contract_settings_manufacturer_v3**
> PutCustomerContractSettingsApiResponse put_customer_contract_settings_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_customer_contract_settings=com_patagona_pricemonitor_share_api_customer_contract_settings)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_customer_contract_settings = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCustomerContractSettings() # ComPatagonaPricemonitorShareApiCustomerContractSettings | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_customer_contract_settings_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_customer_contract_settings=com_patagona_pricemonitor_share_api_customer_contract_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_customer_contract_settings_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_customer_contract_settings = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCustomerContractSettings() # ComPatagonaPricemonitorShareApiCustomerContractSettings | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_customer_contract_settings_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_customer_contract_settings=com_patagona_pricemonitor_share_api_customer_contract_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_customer_contract_settings_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_customer_contract_settings** | [**ComPatagonaPricemonitorShareApiCustomerContractSettings**](ComPatagonaPricemonitorShareApiCustomerContractSettings.md)| This is a generated entry and needs to be described. | [optional] 

### Return type

[**PutCustomerContractSettingsApiResponse**](PutCustomerContractSettingsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings for this contract. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_customer_contract_settings_vendor_v3**
> PutCustomerContractSettingsApiResponse put_customer_contract_settings_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_customer_contract_settings=com_patagona_pricemonitor_share_api_customer_contract_settings)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_customer_contract_settings = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCustomerContractSettings() # ComPatagonaPricemonitorShareApiCustomerContractSettings | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_customer_contract_settings_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_customer_contract_settings=com_patagona_pricemonitor_share_api_customer_contract_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_customer_contract_settings_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_customer_contract_settings = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCustomerContractSettings() # ComPatagonaPricemonitorShareApiCustomerContractSettings | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_customer_contract_settings_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_customer_contract_settings=com_patagona_pricemonitor_share_api_customer_contract_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_customer_contract_settings_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_customer_contract_settings** | [**ComPatagonaPricemonitorShareApiCustomerContractSettings**](ComPatagonaPricemonitorShareApiCustomerContractSettings.md)| This is a generated entry and needs to be described. | [optional] 

### Return type

[**PutCustomerContractSettingsApiResponse**](PutCustomerContractSettingsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings for this contract. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_dynamic_monitoring_settings**
> object put_dynamic_monitoring_settings(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_dynamic_monitoring_settings(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_dynamic_monitoring_settings: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_dynamic_monitoring_settings(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_dynamic_monitoring_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_feed_vendor_v2**
> object put_feed_vendor_v2(contract_id, feed_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
feed_id = 'feed_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_feed_vendor_v2(contract_id, feed_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_feed_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
feed_id = 'feed_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_feed_vendor_v2(contract_id, feed_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_feed_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **feed_id** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_tag_manufacturer_v2**
> object put_image_tag_manufacturer_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_image_tag_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_image_tag_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_image_tag_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_image_tag_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_image_tag_vendor_v2**
> object put_image_tag_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_image_tag_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_image_tag_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_image_tag_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_image_tag_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import_settings_vendor_v2**
> object put_import_settings_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_import_settings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_import_settings_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_import_settings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_import_settings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitoring_schedule_manufacturer_v3**
> PutMonitoringSchedulesApiResponse put_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)

Update a monitoring schedule for a given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update a monitoring schedule for a given contract.
        api_response = api_instance.put_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update a monitoring schedule for a given contract.
        api_response = api_instance.put_monitoring_schedule_manufacturer_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_schedule_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 
 **com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3** | [**ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3**](ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3.md)| Request body for updating monitoring schedule. | [optional] 

### Return type

[**PutMonitoringSchedulesApiResponse**](PutMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Monitoring schedule has been updated successfully. |  -  |
**404** | Specified monitoring schedule does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitoring_schedule_vendor_v3**
> PutMonitoringSchedulesApiResponse put_monitoring_schedule_vendor_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)

Update a monitoring schedule for a given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update a monitoring schedule for a given contract.
        api_response = api_instance.put_monitoring_schedule_vendor_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_schedule_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
schedule_id = 56 # int | ID of a monitoring schedule
com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3() # ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3 | Request body for updating monitoring schedule. (optional)

    try:
        # Update a monitoring schedule for a given contract.
        api_response = api_instance.put_monitoring_schedule_vendor_v3(contract_id, schedule_id, com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3=com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_schedule_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **schedule_id** | **int**| ID of a monitoring schedule | 
 **com_patagona_pricemonitor_share_api_post_monitoring_schedule_request_v3** | [**ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3**](ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3.md)| Request body for updating monitoring schedule. | [optional] 

### Return type

[**PutMonitoringSchedulesApiResponse**](PutMonitoringSchedulesApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Monitoring schedule has been updated successfully. |  -  |
**404** | Specified monitoring schedule does not exist. |  -  |
**503** | Monitoring schedule could not be updated due to an internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitoring_settings_manufacturer_v2**
> object put_monitoring_settings_manufacturer_v2(contract_id, body=body)



Update the monitoring settings for a given contract

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | The monitoring settings object to be written to the database (optional)

    try:
        api_response = api_instance.put_monitoring_settings_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_settings_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | The monitoring settings object to be written to the database (optional)

    try:
        api_response = api_instance.put_monitoring_settings_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_settings_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| The monitoring settings object to be written to the database | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the successfully updated monitoring settings object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitoring_settings_manufacturer_v3**
> object put_monitoring_settings_manufacturer_v3(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_monitoring_settings_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_settings_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_monitoring_settings_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_settings_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitoring_settings_vendor_v2**
> object put_monitoring_settings_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_monitoring_settings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_settings_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_monitoring_settings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_settings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_monitoring_settings_vendor_v3**
> object put_monitoring_settings_vendor_v3(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_monitoring_settings_vendor_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_settings_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_monitoring_settings_vendor_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_monitoring_settings_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_offer_filters_vendor_v2**
> object put_offer_filters_vendor_v2(contract_id, list_type, body=body)

Store the vendor filters for the given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
body = None # object | List of the filters that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store the vendor filters for the given contract.
        api_response = api_instance.put_offer_filters_vendor_v2(contract_id, list_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_offer_filters_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
body = None # object | List of the filters that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store the vendor filters for the given contract.
        api_response = api_instance.put_offer_filters_vendor_v2(contract_id, list_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_offer_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 
 **body** | **object**| List of the filters that needs to be considered to ignore the individual offers. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the filters that have been sent as the request body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_offer_retention_settings_manufacturer_v3**
> object put_offer_retention_settings_manufacturer_v3(contract_id, contract_type, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
contract_type = 'contract_type_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_offer_retention_settings_manufacturer_v3(contract_id, contract_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_offer_retention_settings_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
contract_type = 'contract_type_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_offer_retention_settings_manufacturer_v3(contract_id, contract_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_offer_retention_settings_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **contract_type** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_offer_retention_settings_vendor_v3**
> object put_offer_retention_settings_vendor_v3(contract_id, contract_type, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
contract_type = 'contract_type_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_offer_retention_settings_vendor_v3(contract_id, contract_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_offer_retention_settings_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
contract_type = 'contract_type_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_offer_retention_settings_vendor_v3(contract_id, contract_type, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_offer_retention_settings_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **contract_type** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_product_filters_vendor_v2**
> OfferFilterApiResponse put_product_filters_vendor_v2(contract_id, list_type, product_id, and_offer_filter=and_offer_filter)

Store the filters of a given product for the given contract.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
product_id = 'product_id_example' # str | 
and_offer_filter = [pricemonitor_api_client.AndOfferFilter()] # list[AndOfferFilter] | List of the filter that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store the filters of a given product for the given contract.
        api_response = api_instance.put_product_filters_vendor_v2(contract_id, list_type, product_id, and_offer_filter=and_offer_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_product_filters_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
list_type = 'list_type_example' # str | 
product_id = 'product_id_example' # str | 
and_offer_filter = [pricemonitor_api_client.AndOfferFilter()] # list[AndOfferFilter] | List of the filter that needs to be considered to ignore the individual offers. (optional)

    try:
        # Store the filters of a given product for the given contract.
        api_response = api_instance.put_product_filters_vendor_v2(contract_id, list_type, product_id, and_offer_filter=and_offer_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_product_filters_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **list_type** | **str**|  | 
 **product_id** | **str**|  | 
 **and_offer_filter** | [**list[AndOfferFilter]**](AndOfferFilter.md)| List of the filter that needs to be considered to ignore the individual offers. | [optional] 

### Return type

[**OfferFilterApiResponse**](OfferFilterApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the filters that have been sent as the request body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_products_csv_manufacturer_v2**
> object put_products_csv_manufacturer_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_products_csv_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_products_csv_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_products_csv_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_products_csv_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_products_vendor_v2**
> object put_products_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_products_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_products_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_products_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_products_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repricing_strategy_vendor_v2**
> object put_repricing_strategy_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_repricing_strategy_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_repricing_strategy_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_repricing_strategy_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_repricing_strategy_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Save a new strategy version |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_settings**
> ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody put_settings(contract_id, com_patagona_pricemonitor_share_api_put_admin_contract_settings_body=com_patagona_pricemonitor_share_api_put_admin_contract_settings_body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_put_admin_contract_settings_body = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody() # ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_settings(contract_id, com_patagona_pricemonitor_share_api_put_admin_contract_settings_body=com_patagona_pricemonitor_share_api_put_admin_contract_settings_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_settings: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_put_admin_contract_settings_body = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody() # ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_settings(contract_id, com_patagona_pricemonitor_share_api_put_admin_contract_settings_body=com_patagona_pricemonitor_share_api_put_admin_contract_settings_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_put_admin_contract_settings_body** | [**ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody**](ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.md)| This is a generated entry and needs to be described. | [optional] 

### Return type

[**ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody**](ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_vendor_settings_vendor_v2**
> object put_vendor_settings_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_vendor_settings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_vendor_settings_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.put_vendor_settings_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_vendor_settings_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_vendor_shop_mapping_manufacturer_v3**
> VendorShopMappingV3ApiResponse put_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)

Update an existing vendor for a given contract and associate shops with the given vendor.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for updating an existing vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. (optional)

    try:
        # Update an existing vendor for a given contract and associate shops with the given vendor.
        api_response = api_instance.put_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
vendor_id = 1 # int | ID of vendor shop mapping
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for updating an existing vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. (optional)

    try:
        # Update an existing vendor for a given contract and associate shops with the given vendor.
        api_response = api_instance.put_vendor_shop_mapping_manufacturer_v3(contract_id, vendor_id, com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3=com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_vendor_shop_mapping_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **vendor_id** | **int**| ID of vendor shop mapping | 
 **com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3** | [**ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3**](ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3.md)| Request body for updating an existing vendor and associate shops with it. Please note that atleast one shop is required for a successful creation. | [optional] 

### Return type

[**VendorShopMappingV3ApiResponse**](VendorShopMappingV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vendor shop mapping has been successfully updated. |  -  |
**400** | The specified vendor name is empty. Or the specified shops are empty. |  -  |
**409** | The specified vendor name already exists in our system. |  -  |
**422** | The specified shops do not exist in our system. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_manufacturer_v3**
> object query_offers_manufacturer_v3(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.query_offers_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.query_offers_manufacturer_v3(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_shop_manufacturer_v3**
> QueryOffersOfShopV3ApiResponse query_offers_shop_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)



Get all offers of a shop. Please note that it might return offers for inactive products.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        api_response = api_instance.query_offers_shop_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_shop_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        api_response = api_instance.query_offers_shop_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_shop_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3** | [**ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3**](ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.md)|  | 

### Return type

[**QueryOffersOfShopV3ApiResponse**](QueryOffersOfShopV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns offers of the shop |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_shop_vendor_v3**
> QueryOffersOfShopV3ApiResponse query_offers_shop_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)



Get all offers of a shop. Please note that it might return offers for inactive products.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        api_response = api_instance.query_offers_shop_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_shop_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3() # ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 | 

    try:
        api_response = api_instance.query_offers_shop_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_shop_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3** | [**ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3**](ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.md)|  | 

### Return type

[**QueryOffersOfShopV3ApiResponse**](QueryOffersOfShopV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns offers of the shop |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_stats_manufacturer_v3**
> PostOfferStatisticsApiResponse query_offers_stats_manufacturer_v3(contract_id, post_offer_statistics_request)



This operation is used to get offer statistics (e.g. offer count, average price) grouped by product and domain. Warning: This endpoint contains complex query structure and will be replaced in the future. Please note that offer statistics can only be computed for at maximum 2500 products at a time.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        api_response = api_instance.query_offers_stats_manufacturer_v3(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_stats_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
post_offer_statistics_request = pricemonitor_api_client.PostOfferStatisticsRequest() # PostOfferStatisticsRequest | 

    try:
        api_response = api_instance.query_offers_stats_manufacturer_v3(contract_id, post_offer_statistics_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_stats_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **post_offer_statistics_request** | [**PostOfferStatisticsRequest**](PostOfferStatisticsRequest.md)|  | 

### Return type

[**PostOfferStatisticsApiResponse**](PostOfferStatisticsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of offer statistics per product. |  -  |
**400** | Returned in case of unparsable request body JSON or unsupported filter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_price_recommendations_vendor_v2**
> QueryPriceRecommendationsV2ApiResponse query_price_recommendations_vendor_v2(contract_id, price_recommendation_api_query_v2=price_recommendation_api_query_v2)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
price_recommendation_api_query_v2 = pricemonitor_api_client.PriceRecommendationApiQueryV2() # PriceRecommendationApiQueryV2 | The request body specifies which price recommendations will be searched for. (optional)

    try:
        api_response = api_instance.query_price_recommendations_vendor_v2(contract_id, price_recommendation_api_query_v2=price_recommendation_api_query_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_price_recommendations_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
price_recommendation_api_query_v2 = pricemonitor_api_client.PriceRecommendationApiQueryV2() # PriceRecommendationApiQueryV2 | The request body specifies which price recommendations will be searched for. (optional)

    try:
        api_response = api_instance.query_price_recommendations_vendor_v2(contract_id, price_recommendation_api_query_v2=price_recommendation_api_query_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_price_recommendations_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **price_recommendation_api_query_v2** | [**PriceRecommendationApiQueryV2**](PriceRecommendationApiQueryV2.md)| The request body specifies which price recommendations will be searched for. | [optional] 

### Return type

[**QueryPriceRecommendationsV2ApiResponse**](QueryPriceRecommendationsV2ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of price recommendations is returned for the specified timerange. &lt;br&gt; Only the newest price recommendations are returned in case of multiple price recommendations per product.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_products_by_filter_manufacturer_v3**
> QueryProductsByFilterManufacturerV3ApiResponse query_products_by_filter_manufacturer_v3(contract_id, query_products_request_v3=query_products_request_v3)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        api_response = api_instance.query_products_by_filter_manufacturer_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_products_by_filter_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        api_response = api_instance.query_products_by_filter_manufacturer_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_products_by_filter_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **query_products_request_v3** | [**QueryProductsRequestV3**](QueryProductsRequestV3.md)| The body contains the products query. | [optional] 

### Return type

[**QueryProductsByFilterManufacturerV3ApiResponse**](QueryProductsByFilterManufacturerV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of found products. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_products_by_filter_vendor_v3**
> QueryProductsByFilterVendorV3ApiResponse query_products_by_filter_vendor_v3(contract_id, query_products_request_v3=query_products_request_v3)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        api_response = api_instance.query_products_by_filter_vendor_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_products_by_filter_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
query_products_request_v3 = pricemonitor_api_client.QueryProductsRequestV3() # QueryProductsRequestV3 | The body contains the products query. (optional)

    try:
        api_response = api_instance.query_products_by_filter_vendor_v3(contract_id, query_products_request_v3=query_products_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_products_by_filter_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **query_products_request_v3** | [**QueryProductsRequestV3**](QueryProductsRequestV3.md)| The body contains the products query. | [optional] 

### Return type

[**QueryProductsByFilterVendorV3ApiResponse**](QueryProductsByFilterVendorV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of found products. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **raw_offers**
> object raw_offers(contract_id, start, limit, since=since, until=until)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.raw_offers(contract_id, start, limit, since=since, until=until)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->raw_offers: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
start = 56 # int | 
limit = 56 # int | 
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        api_response = api_instance.raw_offers(contract_id, start, limit, since=since, until=until)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->raw_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **int**|  | 
 **limit** | **int**|  | 
 **since** | **datetime**|  | [optional] 
 **until** | **datetime**|  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user**
> object remove_user(company_id, user_id)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company
user_id = 56 # int | 

    try:
        api_response = api_instance.remove_user(company_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->remove_user: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    company_id = 1 # int | ID of a company
user_id = 56 # int | 

    try:
        api_response = api_instance.remove_user(company_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->remove_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 
 **user_id** | **int**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_new_password**
> str request_new_password(com_patagona_pricemonitor_share_api_post_new_password_request=com_patagona_pricemonitor_share_api_post_new_password_request)

Request a new password

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    com_patagona_pricemonitor_share_api_post_new_password_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostNewPasswordRequest() # ComPatagonaPricemonitorShareApiPostNewPasswordRequest | Request a new password. (optional)

    try:
        # Request a new password
        api_response = api_instance.request_new_password(com_patagona_pricemonitor_share_api_post_new_password_request=com_patagona_pricemonitor_share_api_post_new_password_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->request_new_password: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    com_patagona_pricemonitor_share_api_post_new_password_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostNewPasswordRequest() # ComPatagonaPricemonitorShareApiPostNewPasswordRequest | Request a new password. (optional)

    try:
        # Request a new password
        api_response = api_instance.request_new_password(com_patagona_pricemonitor_share_api_post_new_password_request=com_patagona_pricemonitor_share_api_post_new_password_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->request_new_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_post_new_password_request** | [**ComPatagonaPricemonitorShareApiPostNewPasswordRequest**](ComPatagonaPricemonitorShareApiPostNewPasswordRequest.md)| Request a new password. | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response upon password request |  -  |
**400** | Invalid request body is specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> str reset_password(com_patagona_pricemonitor_share_api_put_reset_password_request=com_patagona_pricemonitor_share_api_put_reset_password_request)

Reset the password

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    com_patagona_pricemonitor_share_api_put_reset_password_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutResetPasswordRequest() # ComPatagonaPricemonitorShareApiPutResetPasswordRequest | Reset a password (optional)

    try:
        # Reset the password
        api_response = api_instance.reset_password(com_patagona_pricemonitor_share_api_put_reset_password_request=com_patagona_pricemonitor_share_api_put_reset_password_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->reset_password: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    com_patagona_pricemonitor_share_api_put_reset_password_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutResetPasswordRequest() # ComPatagonaPricemonitorShareApiPutResetPasswordRequest | Reset a password (optional)

    try:
        # Reset the password
        api_response = api_instance.reset_password(com_patagona_pricemonitor_share_api_put_reset_password_request=com_patagona_pricemonitor_share_api_put_reset_password_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **com_patagona_pricemonitor_share_api_put_reset_password_request** | [**ComPatagonaPricemonitorShareApiPutResetPasswordRequest**](ComPatagonaPricemonitorShareApiPutResetPasswordRequest.md)| Reset a password | [optional] 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password changed successfully. |  -  |
**400** | Password didn&#39;t change successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_include_delivery_costs**
> object save_include_delivery_costs(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.save_include_delivery_costs(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->save_include_delivery_costs: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.save_include_delivery_costs(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->save_include_delivery_costs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduler_delete_request_manufacturer_v3**
> object scheduler_delete_request_manufacturer_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_delete_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_delete_request_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_delete_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_delete_request_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The scheduler path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduler_delete_request_vendor_v3**
> object scheduler_delete_request_vendor_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_delete_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_delete_request_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_delete_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_delete_request_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The scheduler path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduler_get_request_manufacturer_v3**
> object scheduler_get_request_manufacturer_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_get_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_get_request_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_get_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_get_request_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The scheduler path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduler_get_request_vendor_v3**
> object scheduler_get_request_vendor_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_get_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_get_request_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_get_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_get_request_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The scheduler path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduler_post_request_manufacturer_v3**
> object scheduler_post_request_manufacturer_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_post_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_post_request_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_post_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_post_request_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The scheduler path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduler_post_request_vendor_v3**
> object scheduler_post_request_vendor_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_post_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_post_request_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_post_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_post_request_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The scheduler path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduler_put_request_manufacturer_v3**
> object scheduler_put_request_manufacturer_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_put_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_put_request_manufacturer_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_put_request_manufacturer_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_put_request_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The scheduler path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduler_put_request_vendor_v3**
> object scheduler_put_request_vendor_v3(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_put_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_put_request_vendor_v3: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The scheduler path to be called

    try:
        api_response = api_instance.scheduler_put_request_vendor_v3(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->scheduler_put_request_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The scheduler path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_offers_manufacturer_v2**
> object segment_offers_manufacturer_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.segment_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->segment_offers_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.segment_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->segment_offers_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segment_offers_vendor_v2**
> object segment_offers_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.segment_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->segment_offers_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.segment_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->segment_offers_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shop_integration_get_request**
> object shop_integration_get_request(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The shop-integration path to be called

    try:
        api_response = api_instance.shop_integration_get_request(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->shop_integration_get_request: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The shop-integration path to be called

    try:
        api_response = api_instance.shop_integration_get_request(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->shop_integration_get_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The shop-integration path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shop_integration_post_request**
> object shop_integration_post_request(contract_id, path)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The shop-integration path to be called

    try:
        api_response = api_instance.shop_integration_post_request(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->shop_integration_post_request: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | The shop-integration path to be called

    try:
        api_response = api_instance.shop_integration_post_request(contract_id, path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->shop_integration_post_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**| The shop-integration path to be called | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shop_integration_post_request_vendor_v2**
> object shop_integration_post_request_vendor_v2(contract_id, path, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.shop_integration_post_request_vendor_v2(contract_id, path, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->shop_integration_post_request_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
path = 'path_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.shop_integration_post_request_vendor_v2(contract_id, path, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->shop_integration_post_request_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **path** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_manufacturer_v2**
> ComPatagonaPricemonitorShareApiContractStats stats_manufacturer_v2(contract_id, session)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | A ISO 8601 timestamp which marks the end of a 48h time range in which the data is collected

    try:
        api_response = api_instance.stats_manufacturer_v2(contract_id, session)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->stats_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
session = '2013-10-20T19:20:30+01:00' # datetime | A ISO 8601 timestamp which marks the end of a 48h time range in which the data is collected

    try:
        api_response = api_instance.stats_manufacturer_v2(contract_id, session)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->stats_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **session** | **datetime**| A ISO 8601 timestamp which marks the end of a 48h time range in which the data is collected | 

### Return type

[**ComPatagonaPricemonitorShareApiContractStats**](ComPatagonaPricemonitorShareApiContractStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the contract statistics: product count, vendor count, found offers count (filters applied), active portals count, found offers count (no filters applied) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timestamps_manufacturer_v2**
> object timestamps_manufacturer_v2(contract_id, limit)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
limit = 56 # int | 

    try:
        api_response = api_instance.timestamps_manufacturer_v2(contract_id, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->timestamps_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
limit = 56 # int | 

    try:
        api_response = api_instance.timestamps_manufacturer_v2(contract_id, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->timestamps_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **limit** | **int**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_settings**
> object update_alert_settings(contract_id, alert_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
alert_id = 'alert_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_alert_settings(contract_id, alert_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_alert_settings: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
alert_id = 'alert_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_alert_settings(contract_id, alert_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_alert_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **alert_id** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_token**
> object update_auth_token(email, token, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    email = 'email_example' # str | 
token = 'token_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_auth_token(email, token, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_auth_token: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    email = 'email_example' # str | 
token = 'token_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_auth_token(email, token, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **token** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_manufacturer_v2**
> GenericTask update_task_manufacturer_v2(contract_id, task_id, update_task_request_v2=update_task_request_v2)



Update an existing task

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 
update_task_request_v2 = pricemonitor_api_client.UpdateTaskRequestV2() # UpdateTaskRequestV2 | The new task object to be written to the database (optional)

    try:
        api_response = api_instance.update_task_manufacturer_v2(contract_id, task_id, update_task_request_v2=update_task_request_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_task_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 
update_task_request_v2 = pricemonitor_api_client.UpdateTaskRequestV2() # UpdateTaskRequestV2 | The new task object to be written to the database (optional)

    try:
        api_response = api_instance.update_task_manufacturer_v2(contract_id, task_id, update_task_request_v2=update_task_request_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_task_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 
 **update_task_request_v2** | [**UpdateTaskRequestV2**](UpdateTaskRequestV2.md)| The new task object to be written to the database | [optional] 

### Return type

[**GenericTask**](GenericTask.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The task was successfully updated and the given data is returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_vendor_v2**
> object update_task_vendor_v2(contract_id, task_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_task_vendor_v2(contract_id, task_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_task_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
task_id = 'task_id_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_task_vendor_v2(contract_id, task_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_task_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **task_id** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_role**
> object update_user_role(user_id, role_name, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    user_id = 56 # int | 
role_name = 'role_name_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_user_role(user_id, role_name, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_user_role: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    user_id = 56 # int | 
role_name = 'role_name_example' # str | 
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.update_user_role(user_id, role_name, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->update_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **role_name** | **str**|  | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_info**
> ComPatagonaPricemonitorShareApiUserInfo user_info()

Details of the current user

Returns the current user with its companies and contracts

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        # Details of the current user
        api_response = api_instance.user_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->user_info: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        # Details of the current user
        api_response = api_instance.user_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ComPatagonaPricemonitorShareApiUserInfo**](ComPatagonaPricemonitorShareApiUserInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_signup**
> user_signup(user_signup_request)

Create a new user account in the system

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    user_signup_request = pricemonitor_api_client.UserSignupRequest() # UserSignupRequest | The user sign up data

    try:
        # Create a new user account in the system
        api_instance.user_signup(user_signup_request)
    except ApiException as e:
        print("Exception when calling InternalApi->user_signup: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    user_signup_request = pricemonitor_api_client.UserSignupRequest() # UserSignupRequest | The user sign up data

    try:
        # Create a new user account in the system
        api_instance.user_signup(user_signup_request)
    except ApiException as e:
        print("Exception when calling InternalApi->user_signup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_signup_request** | [**UserSignupRequest**](UserSignupRequest.md)| The user sign up data | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |
**201** | User was created and confirmation e-mail was sent |  -  |
**400** | Unable to create the user because of bad request data |  -  |
**500** | Unable to create the user because of an unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_offers_manufacturer_v2**
> object validate_offers_manufacturer_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.validate_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->validate_offers_manufacturer_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.validate_offers_manufacturer_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->validate_offers_manufacturer_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_offers_vendor_v2**
> object validate_offers_vendor_v2(contract_id, body=body)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.validate_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->validate_offers_vendor_v2: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    contract_id = 'qbcxvb' # str | ID of the contract
body = None # object | This is a generated entry and needs to be described. (optional)

    try:
        api_response = api_instance.validate_offers_vendor_v2(contract_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->validate_offers_vendor_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **object**| This is a generated entry and needs to be described. | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_data**
> object vendor_data(vendor, min_price, max_price)



### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    vendor = 'vendor_example' # str | 
min_price = 3.4 # float | 
max_price = 3.4 # float | 

    try:
        api_response = api_instance.vendor_data(vendor, min_price, max_price)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->vendor_data: %s\n" % e)
```

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = pricemonitor_api_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure Bearer authorization (JWT): BearerAuth
configuration = pricemonitor_api_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    vendor = 'vendor_example' # str | 
min_price = 3.4 # float | 
max_price = 3.4 # float | 

    try:
        api_response = api_instance.vendor_data(vendor, min_price, max_price)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->vendor_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor** | **str**|  | 
 **min_price** | **float**|  | 
 **max_price** | **float**|  | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This is a generated entry and needs to be described. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version**
> VersionApiResponse version()

Get the current application version

### Example

```python
from __future__ import print_function
import time
import pricemonitor_api_client
from pricemonitor_api_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.patagona.de
# See configuration.py for a list of all supported configuration parameters.
configuration = pricemonitor_api_client.Configuration(
    host = "https://api.patagona.de"
)


# Enter a context with an instance of the API client
with pricemonitor_api_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pricemonitor_api_client.InternalApi(api_client)
    
    try:
        # Get the current application version
        api_response = api_instance.version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionApiResponse**](VersionApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current application version. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

