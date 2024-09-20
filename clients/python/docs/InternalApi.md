# pricemonitor_api_client.InternalApi

All URIs are relative to *https://api.patagona.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company**](InternalApi.md#add_company) | **POST** /controlpanel/api/companies | Add company
[**add_company_user**](InternalApi.md#add_company_user) | **PUT** /controlpanel/companies/{id}/users/{email} | Add user to company
[**add_pricing_strategy_scenario**](InternalApi.md#add_pricing_strategy_scenario) | **POST** /api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/scenarios | Add scenario strategy
[**add_user**](InternalApi.md#add_user) | **POST** /controlpanel/users | Add a new user
[**authenticate**](InternalApi.md#authenticate) | **POST** /login | Authenticate
[**change_password**](InternalApi.md#change_password) | **PUT** /api/account/password | Change password
[**check_user_confirmation**](InternalApi.md#check_user_confirmation) | **HEAD** /api/account/confirm/{token} | Check if a specific confirmation token exists
[**confirm_user**](InternalApi.md#confirm_user) | **POST** /api/account/confirm/{token} | Confirm an unconfirmed user
[**create_alert_settings**](InternalApi.md#create_alert_settings) | **POST** /api/1/{contractId}/settings/alerts | Create alert settings
[**create_auth_token**](InternalApi.md#create_auth_token) | **POST** /controlpanel/users/{email}/authtokens | Create authentication token
[**create_task**](InternalApi.md#create_task) | **POST** /api/1/{contractId}/tasks | Create task
[**create_task_manufacturer_v2**](InternalApi.md#create_task_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/tasks | Create task [manufacturer]
[**create_task_vendor_v2**](InternalApi.md#create_task_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/tasks | Create a task [vendor]
[**delete_alert_settings**](InternalApi.md#delete_alert_settings) | **DELETE** /api/1/{contractId}/settings/alerts/{alertId} | Delete alert settings
[**delete_auth_token**](InternalApi.md#delete_auth_token) | **DELETE** /controlpanel/users/{email}/authtokens/{token} | Delete authentication token
[**delete_callback_settings_manufacturer_v2**](InternalApi.md#delete_callback_settings_manufacturer_v2) | **DELETE** /api/2/m/contracts/{contractId}/settings/callbacks | Delete callbacks [manufacturer]
[**delete_callback_settings_vendor_v2**](InternalApi.md#delete_callback_settings_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/settings/callbacks | Delete callbacks
[**delete_contract_vendor_v2**](InternalApi.md#delete_contract_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId} | Delete contract [vendor]
[**delete_dynamic_monitoring_settings**](InternalApi.md#delete_dynamic_monitoring_settings) | **DELETE** /api/1/{contractId}/settings/dynamicmonitoring | Delete dynamic monitoring settings
[**delete_feed_vendor_v2**](InternalApi.md#delete_feed_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/feeds/{feedId} | Deleted feed
[**delete_import_settings_vendor_v2**](InternalApi.md#delete_import_settings_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/settings/import | Delete import settings
[**delete_monitoring_schedule_manufacturer_v3**](InternalApi.md#delete_monitoring_schedule_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Delete monitoring schedule for contract [manufacturer]
[**delete_monitoring_schedule_vendor_v3**](InternalApi.md#delete_monitoring_schedule_vendor_v3) | **DELETE** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Delete monitoring schedule for contract [vendor]
[**delete_products_manufacturer_v3**](InternalApi.md#delete_products_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/products | Delete products [manufacturer]
[**delete_repricing_strategy_vendor_v2**](InternalApi.md#delete_repricing_strategy_vendor_v2) | **DELETE** /api/2/v/contracts/{contractId}/settings/repricingstrategy | Delete repricing strategy
[**delete_user_role**](InternalApi.md#delete_user_role) | **DELETE** /api/2/users/{userId}/role/{roleName} | Delete user role
[**delete_vendor_shop_mapping_manufacturer_v3**](InternalApi.md#delete_vendor_shop_mapping_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/vendors/{vendorId} | Delete vendor and associated shops for contract
[**execute_monitoring_schedule_manufacturer_v3**](InternalApi.md#execute_monitoring_schedule_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId}/execute | Trigger monitoring pipeline for schedule [manufacturer]
[**execute_monitoring_schedule_vendor_v3**](InternalApi.md#execute_monitoring_schedule_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId}/execute | Trigger monitoring pipeline for schedule [vendor]
[**get_active_ebay_token_vendor_v2**](InternalApi.md#get_active_ebay_token_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/ebay/token | Get active Ebay token
[**get_alert_settings**](InternalApi.md#get_alert_settings) | **GET** /api/1/{contractId}/settings/alerts | Get alert settings
[**get_all_companies**](InternalApi.md#get_all_companies) | **GET** /controlpanel/api/companies | Get a list of all companies
[**get_all_contracts**](InternalApi.md#get_all_contracts) | **GET** /controlpanel/api/contracts | Get a list of all contracts
[**get_all_domains_control_panel_v3**](InternalApi.md#get_all_domains_control_panel_v3) | **POST** /controlpanel/api/v3/domains | Add domain
[**get_all_ebay_authorizations_vendor_v2**](InternalApi.md#get_all_ebay_authorizations_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/ebay/authorizations | Get Ebay authorizations
[**get_all_ebay_tokens_vendor_v2**](InternalApi.md#get_all_ebay_tokens_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/ebay/tokens | Get all Ebay tokens
[**get_all_portals**](InternalApi.md#get_all_portals) | **GET** /controlpanel/api/portals | Get a list of all portals
[**get_all_scenarios_metadata**](InternalApi.md#get_all_scenarios_metadata) | **GET** /api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/scenarios | Get all scenario strategies
[**get_all_tasks**](InternalApi.md#get_all_tasks) | **GET** /controlpanel/api/tasks | Get all tasks
[**get_all_users**](InternalApi.md#get_all_users) | **GET** /controlpanel/api/users | Get a list of all users
[**get_authorization_status_vendor_v3**](InternalApi.md#get_authorization_status_vendor_v3) | **GET** /api/v3/companies/{companyId}/amazon/authorization/status | Get authorization status for Amazon seller account
[**get_callbacks**](InternalApi.md#get_callbacks) | **GET** /api/2/m/contracts/{contractId}/settings/callbacks | Get callbacks [manufacturer]
[**get_cheapest_vendors_manufacturer_v2**](InternalApi.md#get_cheapest_vendors_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/vendors/cheapest | Query cheapest offers
[**get_company**](InternalApi.md#get_company) | **GET** /controlpanel/api/companies/{companyId} | Get company
[**get_complex_offer_filters_vendor_v2**](InternalApi.md#get_complex_offer_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/complex | Get all complex filters for the given contract.
[**get_contracts_vendor_v2**](InternalApi.md#get_contracts_vendor_v2) | **GET** /api/2/v/contracts | Get contracts [vendor]
[**get_currency_vendor_v2**](InternalApi.md#get_currency_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/currency | Get currency settings [vendor]
[**get_customer_contract_settings_manufaturer_v3**](InternalApi.md#get_customer_contract_settings_manufaturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/customer | Get contract settings [manufacturer]
[**get_customer_contract_settings_vendor_v3**](InternalApi.md#get_customer_contract_settings_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/customer | Get customer contract settings [vendor]
[**get_domains_vendor_v2**](InternalApi.md#get_domains_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/domains | Get domains for contract
[**get_dynamic_monitoring_settings**](InternalApi.md#get_dynamic_monitoring_settings) | **GET** /api/1/{contractId}/settings/dynamicmonitoring | Get dynamic monitoring settings
[**get_ebay_authorizations_vendor_v2**](InternalApi.md#get_ebay_authorizations_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/ebay/authorizations/{authIds} | Get Ebay authorization
[**get_extended_tags_manufacturer_v3**](InternalApi.md#get_extended_tags_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/products/{productId}/extendedtags | Get extended tags [manufacturer]
[**get_feed_export_delta_vendor_v2**](InternalApi.md#get_feed_export_delta_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/feeds/{feedId}/export/delta | Get delta export feed
[**get_feed_export_vendor_v2**](InternalApi.md#get_feed_export_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/feeds/{feedId}/export | Get export feed
[**get_import_settings_vendor_v2**](InternalApi.md#get_import_settings_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/import | Get import settings
[**get_looker_user_attributes**](InternalApi.md#get_looker_user_attributes) | **GET** /api/v3/user/looker/attributes | Get Looker user attributes
[**get_manufacturer_manufacturer_v2**](InternalApi.md#get_manufacturer_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId} | Get contract [manufacturer]
[**get_manufacturer_v3**](InternalApi.md#get_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId} | Get contract [manufacturer]
[**get_mappings_vendor_v2**](InternalApi.md#get_mappings_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/productidentifiermapping | Get product mappings
[**get_marketplace_activation_status**](InternalApi.md#get_marketplace_activation_status) | **GET** /api/v3/companies/{companyId}/amazon/marketplace/{marketplaceCountryCode}/contracts/{contractId} | Get marketplace activation status
[**get_monitoring_schedules_manufacturer_v3**](InternalApi.md#get_monitoring_schedules_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules | Get all monitoring schedules for contract [manufacturer]
[**get_monitoring_schedules_vendor_v3**](InternalApi.md#get_monitoring_schedules_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules | Get all monitoring schedules for contract [vendor]
[**get_monitoring_settings_manufacturer_v2**](InternalApi.md#get_monitoring_settings_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/settings/monitoring | Get monitoring settings for contract
[**get_monitoring_settings_manufacturer_v3**](InternalApi.md#get_monitoring_settings_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/monitoring | Get monitoring settings [manufacturer]
[**get_monitoring_settings_vendor_v2**](InternalApi.md#get_monitoring_settings_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/monitoring | Get monitoring settings [vendor]
[**get_monitoring_settings_vendor_v3**](InternalApi.md#get_monitoring_settings_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/monitoring | Get monitoring settings [vendor]
[**get_offer_filters_vendor_v2**](InternalApi.md#get_offer_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/vendors | Get all vendor filters for contract
[**get_offer_retention_settings_manufacturer_v3**](InternalApi.md#get_offer_retention_settings_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/settings/offerretention | Get offer retention settings [manufacturer]
[**get_offer_retention_settings_vendor_v3**](InternalApi.md#get_offer_retention_settings_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/settings/offerretention | Get offer retention settings [vendor]
[**get_offer_statistics_manufacturer_v3**](InternalApi.md#get_offer_statistics_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers/stats | Get offer statistics per product of a contract
[**get_offers**](InternalApi.md#get_offers) | **GET** /api/2/v/contracts/{contractId}/result/offers | Get all offers for all products
[**get_offers_shops_manufacturer_v3**](InternalApi.md#get_offers_shops_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/offers/shops | Get shops with offers for time range
[**get_offers_shops_vendor_v3**](InternalApi.md#get_offers_shops_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/offers/shops | Get shops with offers for time range per domain
[**get_orders_count_by_portal_by_contract**](InternalApi.md#get_orders_count_by_portal_by_contract) | **GET** /api/1/{contractId}/products/orderscountbyportal | Get orders count by portal
[**get_price_cutters_manufacturer_v2**](InternalApi.md#get_price_cutters_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/pricecutters | Query price cutters [manufacturer]
[**get_price_cutters_vendor_v2**](InternalApi.md#get_price_cutters_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/pricecutters | Query price cutters [vendor]
[**get_price_recommendation_stats_vendor_v2**](InternalApi.md#get_price_recommendation_stats_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/result/pricerecommendationstats | Get price reommendation stats
[**get_product_filters_by_id_vendor_v2**](InternalApi.md#get_product_filters_by_id_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/offerfilters/:listType/products/query | Get filtered offers
[**get_product_filters_by_range_vendor_v2**](InternalApi.md#get_product_filters_by_range_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products | Get all the filters product-wise for the given contract.
[**get_product_filters_vendor_v2**](InternalApi.md#get_product_filters_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products/{productId} | Get all the filters of a given product for the given contract.
[**get_product_metrics_by_contract**](InternalApi.md#get_product_metrics_by_contract) | **GET** /api/1/{contractId}/products/articlescountbyportal | Get product metrics for contract
[**get_product_monitoring_status_stats_vendor_v3**](InternalApi.md#get_product_monitoring_status_stats_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/monitoringstatus/stats | Get product monitoring status stats [vendor]
[**get_product_price_violations_manufacturer_v2**](InternalApi.md#get_product_price_violations_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/priceviolations | Get product price violations [manufacturer]
[**get_product_price_violations_vendor_v2**](InternalApi.md#get_product_price_violations_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/result/priceviolations | Get product price violations [vendor]
[**get_product_properties_v3**](InternalApi.md#get_product_properties_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/{productId}/properties | Get all product properties for a product
[**get_product_property_keys_v3**](InternalApi.md#get_product_property_keys_v3) | **GET** /api/v3/vendor/contracts/{contractId}/products/properties/keys | Get all product properties keys
[**get_repricing_strategy_vendor_v2**](InternalApi.md#get_repricing_strategy_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/repricingstrategy | Get repricing strategy
[**get_scenario_by_id**](InternalApi.md#get_scenario_by_id) | **GET** /api/v3/vendor/contracts/{contractId}/settings/pricingstrategies/scenarios/{scenarioId} | Get scenario strategy
[**get_settings**](InternalApi.md#get_settings) | **GET** /api/1/{contractId}/settings | Get settings for contract
[**get_tag_values_manufacturer_v2**](InternalApi.md#get_tag_values_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/products/tags/{key} | Get product tag values [manufacturer]
[**get_tag_values_vendor_v2**](InternalApi.md#get_tag_values_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/products/tags/{key} | Get tag values for key
[**get_tags_manufacturer_v2**](InternalApi.md#get_tags_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/products/tags | Get product tags [manufacturer]
[**get_tags_vendor_v2**](InternalApi.md#get_tags_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/products/tags | Get product tags [vendor]
[**get_task**](InternalApi.md#get_task) | **GET** /api/1/{contractId}/tasks/{taskId} | Get task
[**get_task_data_manufacturer_v2**](InternalApi.md#get_task_data_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/tasks/{taskId}/data | Get task data [manufacturer]
[**get_task_data_vendor_v2**](InternalApi.md#get_task_data_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/tasks/{taskId}/data | Get task data [vendor]
[**get_task_manufacturer_v2**](InternalApi.md#get_task_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/tasks/{taskId} | Get task [manufacturer]
[**get_task_state**](InternalApi.md#get_task_state) | **GET** /api/1/{contractId}/tasks/{taskId}/state | Get task state
[**get_tasks**](InternalApi.md#get_tasks) | **GET** /api/1/{contractId}/tasks | Get tasks
[**get_tasks_manufacturer_v2**](InternalApi.md#get_tasks_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/tasks | Find tasks for contract [manufactuerer]
[**get_tasks_stats**](InternalApi.md#get_tasks_stats) | **GET** /controlpanel/api/tasks/stats | Get all task stats
[**get_time_stamps**](InternalApi.md#get_time_stamps) | **GET** /api/1/{contractId}/products/analysis/timestamps | Get time stamps
[**get_user**](InternalApi.md#get_user) | **GET** /controlpanel/api/users/{email} | Get user
[**get_user_access_to_contracts_of_company_v3**](InternalApi.md#get_user_access_to_contracts_of_company_v3) | **GET** /api/v3/companies/{companyId}/users/contractaccess | Get contract access of users
[**get_users**](InternalApi.md#get_users) | **GET** /controlpanel/api/companies/{companyId}/users | Get all users of a company
[**get_vendor_settings_v2_vendor_v2**](InternalApi.md#get_vendor_settings_v2_vendor_v2) | **GET** /api/2/v/contracts/{contractId}/settings/repricing | Get repricing settings
[**get_vendor_shop_mapping_manufacturer_v3**](InternalApi.md#get_vendor_shop_mapping_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/vendors/{vendorId} | Get vendor and shops for contract
[**get_vendor_shop_mappings_manufacturer_v3**](InternalApi.md#get_vendor_shop_mappings_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/vendors | Get all vendors and shops for contract
[**get_vendor_v3**](InternalApi.md#get_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId} | Get contract [vendor]
[**get_vendor_vendor_v2**](InternalApi.md#get_vendor_vendor_v2) | **GET** /api/2/v/contracts/{contractId} | Get contract [vendor]
[**get_vendors_by_domain_manufacturer_v2**](InternalApi.md#get_vendors_by_domain_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/vendors/list | Get vendors by domain
[**list_vendors**](InternalApi.md#list_vendors) | **GET** /controlpanel/vendors | Get list of vendors
[**login_by_auth_token**](InternalApi.md#login_by_auth_token) | **GET** /api/login/token/{token} | Log in with authentication token
[**logout**](InternalApi.md#logout) | **POST** /logout | Log out
[**monitoring_pipeline_post_request_manufacturer_v3**](InternalApi.md#monitoring_pipeline_post_request_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/monitoringpipeline/{path} | Update monitoring pipeline [manufacturer]
[**monitoring_pipeline_post_request_vendor_v3**](InternalApi.md#monitoring_pipeline_post_request_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/monitoringpipeline/{path} | Update monitoring pipeline [vendor]
[**monitoring_pipeline_upsert_search_attempts_manufacturer_v3**](InternalApi.md#monitoring_pipeline_upsert_search_attempts_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/monitoringpipeline/v1/searchattempts | Update monitoring pipeline search attempts [manufacturer]
[**monitoring_pipeline_upsert_search_attempts_vendor_v3**](InternalApi.md#monitoring_pipeline_upsert_search_attempts_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/monitoringpipeline/v1/searchattempts | Update monitoring pipeline search attempts [vendor]
[**patch_product_manufacturer_v3**](InternalApi.md#patch_product_manufacturer_v3) | **PATCH** /api/v3/manufacturer/contracts/{contractId}/products/{productId} | Update product [manufacturer]
[**patch_product_vendor_v3**](InternalApi.md#patch_product_vendor_v3) | **PATCH** /api/v3/vendor/contracts/{contractId}/products/{productId} | Update product [vendor]
[**position_distribution**](InternalApi.md#position_distribution) | **POST** /api/1/{contractId}/vendors/{vendor}/positions | Update position distribution
[**post_account_v3**](InternalApi.md#post_account_v3) | **POST** /api/v3/account | Create user account
[**post_activate_marketplace_vendor_v3**](InternalApi.md#post_activate_marketplace_vendor_v3) | **POST** /api/v3/companies/{companyId}/amazon/marketplace | Activate Amazon marketplace
[**post_authorize_seller_vendor_v3**](InternalApi.md#post_authorize_seller_vendor_v3) | **POST** /api/v3/companies/{companyId}/amazon/authorization | Set up authorization for Amazon seller account
[**post_ebay_authorization_vendor_v2**](InternalApi.md#post_ebay_authorization_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/settings/ebay/authorizations | Update Ebay authorization
[**post_embed_sso_url_manufacturer**](InternalApi.md#post_embed_sso_url_manufacturer) | **POST** /api/v3/manufacturer/contracts/{contractId}/looker/sso/embed/url | Retrieve Looker embed SSO url [manufacturer]
[**post_embed_sso_url_vendor**](InternalApi.md#post_embed_sso_url_vendor) | **POST** /api/v3/vendor/contracts/{contractId}/looker/sso/embed/url | Retrieve Looker embed SSO url [vendor]
[**post_feed_vendor_v2**](InternalApi.md#post_feed_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/feeds | Create feed
[**post_mappings_vendor_v2**](InternalApi.md#post_mappings_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/productidentifiermapping | Update product identifier mapping
[**post_monitoring_schedule_manufacturer_v3**](InternalApi.md#post_monitoring_schedule_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules | Add monitoring schedule for contract [manufacturer]
[**post_monitoring_schedule_vendor_v3**](InternalApi.md#post_monitoring_schedule_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules | Add monitoring schedule for contract
[**post_offer_statistics_vendor_query**](InternalApi.md#post_offer_statistics_vendor_query) | **POST** /api/v3/vendor/contracts/{contractId}/offers/stats/query | Get offer statistics per product
[**post_vendor_shop_mapping_manufacturer_v3**](InternalApi.md#post_vendor_shop_mapping_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/vendors | Add new vendor to contract and associate shops
[**prices_by_day_by_product_id_manufacturer_v2**](InternalApi.md#prices_by_day_by_product_id_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/pricesbyday/productid/{productId} | Query prices by day by product
[**publish_preprocessing_task_vendor_v3**](InternalApi.md#publish_preprocessing_task_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/tasks/preprocessing | Publish preprocessing task [vendor]
[**put_admin_domain_control_panel_v3**](InternalApi.md#put_admin_domain_control_panel_v3) | **PUT** /controlpanel/api/v3/domains/{domain} | Update or add domain
[**put_callbacks**](InternalApi.md#put_callbacks) | **PUT** /api/2/m/contracts/{contractId}/settings/callbacks | Update callbacks [manufacturer]
[**put_complex_offer_filters_vendor_v2**](InternalApi.md#put_complex_offer_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/complex | Add the complex filters for the given contract.
[**put_csv_products**](InternalApi.md#put_csv_products) | **PUT** /api/2/v/contracts/{contractId}/products/csv | Set products via CSV file (V2)
[**put_csv_products_manufacturer_v3**](InternalApi.md#put_csv_products_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/products | Set products via CSV file (V3)
[**put_currency_vendor_v2**](InternalApi.md#put_currency_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/currency | Update currency settings [vendor]
[**put_customer_contract_settings_manufacturer_v3**](InternalApi.md#put_customer_contract_settings_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/customer | Update contract settings [manufacturer]
[**put_customer_contract_settings_vendor_v3**](InternalApi.md#put_customer_contract_settings_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/customer | Update customer contract settings [vendor]
[**put_dynamic_monitoring_settings**](InternalApi.md#put_dynamic_monitoring_settings) | **PUT** /api/1/{contractId}/settings/dynamicmonitoring | Update dynamic monitoring settings
[**put_feed_vendor_v2**](InternalApi.md#put_feed_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/feeds/{feedId} | Update feed
[**put_image_tag_manufacturer_v2**](InternalApi.md#put_image_tag_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/settings/imagetag | Update image tag [manufacturer]
[**put_image_tag_vendor_v2**](InternalApi.md#put_image_tag_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/imagetag | Update image tag [vendor]
[**put_import_settings_vendor_v2**](InternalApi.md#put_import_settings_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/import | Update import settings
[**put_monitoring_schedule_manufacturer_v3**](InternalApi.md#put_monitoring_schedule_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Update monitoring schedule for contract [manufacturer]
[**put_monitoring_schedule_vendor_v3**](InternalApi.md#put_monitoring_schedule_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/monitoringschedules/{scheduleId} | Update monitoring schedule for contract [vendor]
[**put_monitoring_settings_manufacturer_v2**](InternalApi.md#put_monitoring_settings_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/settings/monitoring | Update monitoring settings for contract
[**put_monitoring_settings_manufacturer_v3**](InternalApi.md#put_monitoring_settings_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/monitoring | Update monitoring settings [manufacturer]
[**put_monitoring_settings_vendor_v2**](InternalApi.md#put_monitoring_settings_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/monitoring | Update monitoring settings [vendor]
[**put_monitoring_settings_vendor_v3**](InternalApi.md#put_monitoring_settings_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/monitoring | Update monitoring settings [vendor]
[**put_offer_filters_vendor_v2**](InternalApi.md#put_offer_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/vendors | Store vendor filters for contract
[**put_offer_retention_settings_manufacturer_v3**](InternalApi.md#put_offer_retention_settings_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/settings/offerretention | Update offer retention settings [manufacturer]
[**put_offer_retention_settings_vendor_v3**](InternalApi.md#put_offer_retention_settings_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/settings/offerretention | Update offer retention settings [vendor]
[**put_product_filters_vendor_v2**](InternalApi.md#put_product_filters_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/offerfilters/{listType}/products/{productId} | Store the filters of a given product for the given contract.
[**put_product_properties_v3**](InternalApi.md#put_product_properties_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/products/{productId}/properties | Manage product properties for a product
[**put_products_csv_manufacturer_v2**](InternalApi.md#put_products_csv_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/products/csv | Set products via CSV file [manufacturer]
[**put_products_vendor_v2**](InternalApi.md#put_products_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/products | Update products in bulk (JSON)
[**put_repricing_strategy_vendor_v2**](InternalApi.md#put_repricing_strategy_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/repricingstrategy | Update repricing strategy
[**put_settings**](InternalApi.md#put_settings) | **PUT** /api/1/{contractId}/settings | Update settings for contract
[**put_user_access_to_contracts_of_company_v3**](InternalApi.md#put_user_access_to_contracts_of_company_v3) | **PUT** /api/v3/companies/{companyId}/users/contractaccess | Set contract access of users
[**put_vendor_settings_vendor_v2**](InternalApi.md#put_vendor_settings_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/settings/repricing | Update repricing settings
[**put_vendor_shop_mapping_manufacturer_v3**](InternalApi.md#put_vendor_shop_mapping_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/vendors/{vendorId} | Update vendor for contract and associate shops
[**query_offers_manufacturer_v3**](InternalApi.md#query_offers_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/query | Query offers [manufacturer]
[**query_offers_price_dumping_stats_manufacturer_v3**](InternalApi.md#query_offers_price_dumping_stats_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/pricedumpingstats | Query price dumping statistics
[**query_offers_price_dumping_stats_vendor_v3**](InternalApi.md#query_offers_price_dumping_stats_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/offers/pricedumpingstats | Query price dumping statistics
[**query_offers_shop_manufacturer_v3**](InternalApi.md#query_offers_shop_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/shop/query | Get all offers [manufacturer]
[**query_offers_shop_vendor_v3**](InternalApi.md#query_offers_shop_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/offers/shop/query | Get all offers [vendor]
[**query_offers_stats_manufacturer_v3**](InternalApi.md#query_offers_stats_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/offers/stats/query | Query offer statistics per product
[**query_offers_stats_manufacturer_v31**](InternalApi.md#query_offers_stats_manufacturer_v31) | **POST** /api/v3.1/manufacturer/contracts/{contractId}/offers/stats/query | Query offer statistics per product
[**query_price_recommendations_vendor_v2**](InternalApi.md#query_price_recommendations_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/pricerecommendations/query | Query price recommendations
[**query_products_by_filter_manufacturer_v3**](InternalApi.md#query_products_by_filter_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/products/query | Get products of a contract
[**query_products_by_filter_vendor_v3**](InternalApi.md#query_products_by_filter_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/products/query | Query products of a contract
[**query_products_manufacturer_v3**](InternalApi.md#query_products_manufacturer_v3) | **POST** /api/v3.1/manufacturer/contracts/{contractId}/products/query | Query products for manufacturer
[**raw_offers**](InternalApi.md#raw_offers) | **GET** /api/1/{contractId}/products/offers | Get offers for contract
[**remove_user**](InternalApi.md#remove_user) | **DELETE** /controlpanel/api/companies/{companyId}/users/{userId} | Remove user from company
[**request_new_password**](InternalApi.md#request_new_password) | **POST** /api/account/password/reset | Request a new password
[**reset_password**](InternalApi.md#reset_password) | **PUT** /api/account/password/reset | Reset the password
[**save_include_delivery_costs**](InternalApi.md#save_include_delivery_costs) | **POST** /api/1/{contractId}/settings/include_delivery_costs | Update includes delivery costs setting
[**scheduler_delete_request_manufacturer_v3**](InternalApi.md#scheduler_delete_request_manufacturer_v3) | **DELETE** /api/v3/manufacturer/contracts/{contractId}/scheduler/{path} | Delete scheduler operation [manufacturer]
[**scheduler_delete_request_vendor_v3**](InternalApi.md#scheduler_delete_request_vendor_v3) | **DELETE** /api/v3/vendor/contracts/{contractId}/scheduler/{path} | Delete scheduler operation
[**scheduler_get_request_manufacturer_v3**](InternalApi.md#scheduler_get_request_manufacturer_v3) | **GET** /api/v3/manufacturer/contracts/{contractId}/scheduler/{path} | Get scheduler operation [manufacturer]
[**scheduler_get_request_vendor_v3**](InternalApi.md#scheduler_get_request_vendor_v3) | **GET** /api/v3/vendor/contracts/{contractId}/scheduler/{path} | Get scheduler operation [vendor]
[**scheduler_post_request_manufacturer_v3**](InternalApi.md#scheduler_post_request_manufacturer_v3) | **POST** /api/v3/manufacturer/contracts/{contractId}/scheduler/{path} | Create scheduler operation [manufacturer]
[**scheduler_post_request_vendor_v3**](InternalApi.md#scheduler_post_request_vendor_v3) | **POST** /api/v3/vendor/contracts/{contractId}/scheduler/{path} | Create scheduler operation
[**scheduler_put_request_manufacturer_v3**](InternalApi.md#scheduler_put_request_manufacturer_v3) | **PUT** /api/v3/manufacturer/contracts/{contractId}/scheduler/{path} | Update scheduler operation [manufacturer]
[**scheduler_put_request_vendor_v3**](InternalApi.md#scheduler_put_request_vendor_v3) | **PUT** /api/v3/vendor/contracts/{contractId}/scheduler/{path} | Update scheduler operation
[**segment_offers_manufacturer_v2**](InternalApi.md#segment_offers_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/offersegmentation | Update segment offers [manufacturer]
[**segment_offers_vendor_v2**](InternalApi.md#segment_offers_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/offersegmentation | Update segment offers [vendor]
[**shop_integration_get_request**](InternalApi.md#shop_integration_get_request) | **GET** /api/2/v/contracts/{contractId}/shop-integration/{path} | Get shop integration
[**shop_integration_post_request**](InternalApi.md#shop_integration_post_request) | **POST** /api/2/v/contracts/{contractId}/shop-integration/{path} | Update shop integration
[**shop_integration_post_request_vendor_v2**](InternalApi.md#shop_integration_post_request_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/products/import | Update shop integration import
[**stats_manufacturer_v2**](InternalApi.md#stats_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/contract/stats | Get contract statistics [manufacturer]
[**timestamps_manufacturer_v2**](InternalApi.md#timestamps_manufacturer_v2) | **GET** /api/2/m/contracts/{contractId}/result/timestamps | Get timestamps
[**update_alert_settings**](InternalApi.md#update_alert_settings) | **PUT** /api/1/{contractId}/settings/alerts/{alertId} | Update alert settings
[**update_auth_token**](InternalApi.md#update_auth_token) | **PUT** /controlpanel/users/{email}/authtokens/{token} | Update authentication token
[**update_task_manufacturer_v2**](InternalApi.md#update_task_manufacturer_v2) | **PUT** /api/2/m/contracts/{contractId}/tasks/{taskId} | Update task [manufacturer]
[**update_task_vendor_v2**](InternalApi.md#update_task_vendor_v2) | **PUT** /api/2/v/contracts/{contractId}/tasks/{taskId} | Update a task
[**update_user_role**](InternalApi.md#update_user_role) | **PUT** /api/2/users/{userId}/role/{roleName} | Add user role
[**user_info**](InternalApi.md#user_info) | **GET** /api/account | Details of the current user
[**user_signup**](InternalApi.md#user_signup) | **POST** /api/account | Create a new user account in the system
[**validate_offers_manufacturer_v2**](InternalApi.md#validate_offers_manufacturer_v2) | **POST** /api/2/m/contracts/{contractId}/result/validation | Validate offers [manufacturer]
[**validate_offers_vendor_v2**](InternalApi.md#validate_offers_vendor_v2) | **POST** /api/2/v/contracts/{contractId}/result/validation | Validate offers [vendor]
[**vendor_data**](InternalApi.md#vendor_data) | **GET** /controlpanel/vendorexport/{vendor} | Get vendor export data
[**version**](InternalApi.md#version) | **GET** /version | Get application version


# **add_company**
> object add_company()

Add company

Add a company.

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
        # Add company
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
        # Add company
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

Add user to company

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
        # Add user to company
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
        # Add user to company
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

Add scenario strategy

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
        # Add scenario strategy
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
        # Add scenario strategy
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

Authenticate

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
        # Authenticate
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

Change password

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
        # Change password
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
        # Change password
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

Create alert settings

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
        # Create alert settings
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
        # Create alert settings
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

Create authentication token

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
        # Create authentication token
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
        # Create authentication token
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

Create task

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
com_patagona_pricemonitor_share_api_create_task_body_v2 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCreateTaskBodyV2() # ComPatagonaPricemonitorShareApiCreateTaskBodyV2 | Create a new task (optional)

    try:
        # Create task
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
        # Create task
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

Create task [manufacturer]

Creates a new task for a manufacturer contract

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
        # Create task [manufacturer]
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
        # Create task [manufacturer]
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

Create a task [vendor]

Creates a new task for a vendor contract.

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
        # Create a task [vendor]
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
        # Create a task [vendor]
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

Delete alert settings

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
        # Delete alert settings
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
        # Delete alert settings
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

Delete authentication token

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
        # Delete authentication token
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
        # Delete authentication token
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

Delete callbacks [manufacturer]

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
        # Delete callbacks [manufacturer]
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
        # Delete callbacks [manufacturer]
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

Delete callbacks

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
        # Delete callbacks
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
        # Delete callbacks
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

Delete contract [vendor]

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
        # Delete contract [vendor]
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
        # Delete contract [vendor]
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

Delete dynamic monitoring settings

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
        # Delete dynamic monitoring settings
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
        # Delete dynamic monitoring settings
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

Deleted feed

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
        # Deleted feed
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
        # Deleted feed
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

Delete import settings

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
        # Delete import settings
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
        # Delete import settings
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

Delete monitoring schedule for contract [manufacturer]

Delete a monitoring schedule for a given manufacturer contract.

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
        # Delete monitoring schedule for contract [manufacturer]
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
        # Delete monitoring schedule for contract [manufacturer]
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

Delete monitoring schedule for contract [vendor]

Delete a monitoring schedule for a given vendor contract.

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
        # Delete monitoring schedule for contract [vendor]
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
        # Delete monitoring schedule for contract [vendor]
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

Delete products [manufacturer]

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
        # Delete products [manufacturer]
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
        # Delete products [manufacturer]
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

Delete repricing strategy

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
        # Delete repricing strategy
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
        # Delete repricing strategy
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

Delete user role

Remove the specified role from the given user.

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
        # Delete user role
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
        # Delete user role
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

Delete vendor and associated shops for contract

Delete a vendor and associated shops for a given manufacturer contract.

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
        # Delete vendor and associated shops for contract
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
        # Delete vendor and associated shops for contract
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

Trigger monitoring pipeline for schedule [manufacturer]

Trigger a monitoring pipeline task for a manufacturer for a configured monitoring schedule.

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
        # Trigger monitoring pipeline for schedule [manufacturer]
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
        # Trigger monitoring pipeline for schedule [manufacturer]
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

Trigger monitoring pipeline for schedule [vendor]

Trigger a monitoring pipeline task for a vendor for a configured monitoring schedule.

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
        # Trigger monitoring pipeline for schedule [vendor]
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
        # Trigger monitoring pipeline for schedule [vendor]
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

Get active Ebay token

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
        # Get active Ebay token
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
        # Get active Ebay token
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

Get alert settings

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
        # Get alert settings
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
        # Get alert settings
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

Add domain

Add a new domain.

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
        # Add domain
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
        # Add domain
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

Get Ebay authorizations

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
        # Get Ebay authorizations
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
        # Get Ebay authorizations
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

Get all Ebay tokens

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
        # Get all Ebay tokens
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
        # Get all Ebay tokens
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

Get all scenario strategies

Get a list of all scenario strategy metadata for a contract.

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
        # Get all scenario strategies
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
        # Get all scenario strategies
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
**200** | List of all scenario strategy metadata |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tasks**
> object get_all_tasks(contract_id, task_id, task_type, task_state, limit, min_creation_date=min_creation_date, max_creation_date=max_creation_date)

Get all tasks

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
        # Get all tasks
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
        # Get all tasks
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

Get authorization status for Amazon seller account

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
        # Get authorization status for Amazon seller account
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
        # Get authorization status for Amazon seller account
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
> ComPatagonaPricemonitorShareApiCallbacks get_callbacks(contract_id)

Get callbacks [manufacturer]

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
        # Get callbacks [manufacturer]
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
        # Get callbacks [manufacturer]
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

[**ComPatagonaPricemonitorShareApiCallbacks**](ComPatagonaPricemonitorShareApiCallbacks.md)

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

# **get_cheapest_vendors_manufacturer_v2**
> object get_cheapest_vendors_manufacturer_v2(contract_id, session, include_delivery_costs, com_patagona_pricemonitor_share_api_tag_filtered_vendors_request=com_patagona_pricemonitor_share_api_tag_filtered_vendors_request)

Query cheapest offers

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
        # Query cheapest offers
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
        # Query cheapest offers
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

Get company

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
        # Get company
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
        # Get company
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

Get contracts [vendor]

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
        # Get contracts [vendor]
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
        # Get contracts [vendor]
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

Get currency settings [vendor]

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
        # Get currency settings [vendor]
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
        # Get currency settings [vendor]
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

Get contract settings [manufacturer]

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
        # Get contract settings [manufacturer]
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
        # Get contract settings [manufacturer]
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

Get customer contract settings [vendor]

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
        # Get customer contract settings [vendor]
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
        # Get customer contract settings [vendor]
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
> StringArrayResponse get_domains_vendor_v2(contract_id)

Get domains for contract

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
        # Get domains for contract
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
        # Get domains for contract
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

[**StringArrayResponse**](StringArrayResponse.md)

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

Get dynamic monitoring settings

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
        # Get dynamic monitoring settings
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
        # Get dynamic monitoring settings
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

Get Ebay authorization

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
        # Get Ebay authorization
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
        # Get Ebay authorization
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

Get extended tags [manufacturer]

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
        # Get extended tags [manufacturer]
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
        # Get extended tags [manufacturer]
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

Get delta export feed

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
        # Get delta export feed
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
        # Get delta export feed
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

Get export feed

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
        # Get export feed
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
        # Get export feed
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

Get import settings

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
        # Get import settings
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
        # Get import settings
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

# **get_looker_user_attributes**
> LookerUserAttributesV3ApiResponse get_looker_user_attributes()

Get Looker user attributes

Retrieves user attributes from Looker. We created the endpoint to allow us to track the impact of the issue described in [Confluence](https://omniaretail.atlassian.net/wiki/spaces/DEV/pages/648151090/Looker+Dashboard+Mismatch+Problem+in+Omnia+2.0) 

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
        # Get Looker user attributes
        api_response = api_instance.get_looker_user_attributes()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_looker_user_attributes: %s\n" % e)
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
        # Get Looker user attributes
        api_response = api_instance.get_looker_user_attributes()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_looker_user_attributes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LookerUserAttributesV3ApiResponse**](LookerUserAttributesV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Looker user attributes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manufacturer_manufacturer_v2**
> object get_manufacturer_manufacturer_v2(contract_id)

Get contract [manufacturer]

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
        # Get contract [manufacturer]
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
        # Get contract [manufacturer]
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

Get contract [manufacturer]

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
        # Get contract [manufacturer]
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
        # Get contract [manufacturer]
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

Get product mappings

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
        # Get product mappings
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
        # Get product mappings
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

Get marketplace activation status

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
        # Get marketplace activation status
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
        # Get marketplace activation status
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

Get all monitoring schedules for contract [manufacturer]

Get all the monitoring schedules for a specified manufacturer contract.

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
        # Get all monitoring schedules for contract [manufacturer]
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
        # Get all monitoring schedules for contract [manufacturer]
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

Get all monitoring schedules for contract [vendor]

Get all the monitoring schedules for a specified vendor contract.

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
        # Get all monitoring schedules for contract [vendor]
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
        # Get all monitoring schedules for contract [vendor]
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

Get monitoring settings for contract

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
        # Get monitoring settings for contract
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
        # Get monitoring settings for contract
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

Get monitoring settings [manufacturer]

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
        # Get monitoring settings [manufacturer]
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
        # Get monitoring settings [manufacturer]
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

Get monitoring settings [vendor]

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
        # Get monitoring settings [vendor]
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
        # Get monitoring settings [vendor]
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

Get monitoring settings [vendor]

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
        # Get monitoring settings [vendor]
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
        # Get monitoring settings [vendor]
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

Get all vendor filters for contract

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
        # Get all vendor filters for contract
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
        # Get all vendor filters for contract
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

Get offer retention settings [manufacturer]

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
        # Get offer retention settings [manufacturer]
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
        # Get offer retention settings [manufacturer]
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

Get offer retention settings [vendor]

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
        # Get offer retention settings [vendor]
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
        # Get offer retention settings [vendor]
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

# **get_offers**
> GetOffersResponse get_offers(contract_id, start, limit, start_date=start_date, end_date=end_date)

Get all offers for all products

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
start = 56 # int | Start product index for pagination
limit = 56 # int | Number of products for pagination
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        # Get all offers for all products
        api_response = api_instance.get_offers(contract_id, start, limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offers: %s\n" % e)
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
start = 56 # int | Start product index for pagination
limit = 56 # int | Number of products for pagination
start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'. (optional)

    try:
        # Get all offers for all products
        api_response = api_instance.get_offers(contract_id, start, limit, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **start** | **int**| Start product index for pagination | 
 **limit** | **int**| Number of products for pagination | 
 **start_date** | **datetime**| Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 
 **end_date** | **datetime**| Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is &#39;NOW - 48 hours to NOW&#39;. | [optional] 

### Return type

[**GetOffersResponse**](GetOffersResponse.md)

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

Query price cutters [manufacturer]

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
        # Query price cutters [manufacturer]
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
        # Query price cutters [manufacturer]
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

Query price cutters [vendor]

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
        # Query price cutters [vendor]
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
        # Query price cutters [vendor]
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

Get price reommendation stats

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
        # Get price reommendation stats
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
        # Get price reommendation stats
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

Get filtered offers

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
        # Get filtered offers
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
        # Get filtered offers
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

Get product metrics for contract

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
        # Get product metrics for contract
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
        # Get product metrics for contract
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

Get product monitoring status stats [vendor]

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
        # Get product monitoring status stats [vendor]
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
        # Get product monitoring status stats [vendor]
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

Get product price violations [manufacturer]

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
        # Get product price violations [manufacturer]
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
        # Get product price violations [manufacturer]
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

Get product price violations [vendor]

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
        # Get product price violations [vendor]
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
        # Get product price violations [vendor]
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

# **get_product_properties_v3**
> GetProductPropertiesV3ApiResponse get_product_properties_v3(contract_id, product_id)

Get all product properties for a product

This endpoint returns a list product properties for a certain product and contract. Product properties represent additional information for a product, independent of the imported products and tags.

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
product_id = 12345678 # int | ID of the product (Omnia's internal product id)

    try:
        # Get all product properties for a product
        api_response = api_instance.get_product_properties_v3(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_properties_v3: %s\n" % e)
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
product_id = 12345678 # int | ID of the product (Omnia's internal product id)

    try:
        # Get all product properties for a product
        api_response = api_instance.get_product_properties_v3(contract_id, product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_properties_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **product_id** | **int**| ID of the product (Omnia&#39;s internal product id) | 

### Return type

[**GetProductPropertiesV3ApiResponse**](GetProductPropertiesV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of product properties |  -  |
**404** | Returned if the product does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_property_keys_v3**
> StringArrayResponse get_product_property_keys_v3(contract_id)

Get all product properties keys

This endpoint returns a list of distinct product property keys for all imported products of a contract.

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
        # Get all product properties keys
        api_response = api_instance.get_product_property_keys_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_property_keys_v3: %s\n" % e)
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
        # Get all product properties keys
        api_response = api_instance.get_product_property_keys_v3(contract_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_product_property_keys_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 

### Return type

[**StringArrayResponse**](StringArrayResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of distinct keys of all product properties. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repricing_strategy_vendor_v2**
> object get_repricing_strategy_vendor_v2(contract_id, document_version=document_version)

Get repricing strategy

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
        # Get repricing strategy
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
        # Get repricing strategy
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

Get scenario strategy

Get a scenario strategy with the provided scenario id.

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
scenario_id = 56 # int | ID of the required scenario strategy

    try:
        # Get scenario strategy
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
scenario_id = 56 # int | ID of the required scenario strategy

    try:
        # Get scenario strategy
        api_response = api_instance.get_scenario_by_id(contract_id, scenario_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_scenario_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **scenario_id** | **int**| ID of the required scenario strategy | 

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
**200** | A scenario strategy |  -  |
**404** | Scenario strategy with the provided Id was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1 get_settings(contract_id)

Get settings for contract

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
        # Get settings for contract
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
        # Get settings for contract
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

Get product tag values [manufacturer]

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
        # Get product tag values [manufacturer]
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
        # Get product tag values [manufacturer]
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

Get tag values for key

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
        # Get tag values for key
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
        # Get tag values for key
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

Get product tags [manufacturer]

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
        # Get product tags [manufacturer]
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
        # Get product tags [manufacturer]
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

Get product tags [vendor]

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
        # Get product tags [vendor]
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
        # Get product tags [vendor]
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

Get task

Get a task by id

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
        # Get task
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
        # Get task
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

Get task data [manufacturer]

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
        # Get task data [manufacturer]
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
        # Get task data [manufacturer]
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

Get task data [vendor]

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
        # Get task data [vendor]
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
        # Get task data [vendor]
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

Get task [manufacturer]

Get the task with the specified id.

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
        # Get task [manufacturer]
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
        # Get task [manufacturer]
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

Get task state

Gets the state of a task.

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
        # Get task state
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
        # Get task state
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

Get tasks

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
        # Get tasks
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
        # Get tasks
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

Find tasks for contract [manufactuerer]

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
        # Find tasks for contract [manufactuerer]
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
        # Find tasks for contract [manufactuerer]
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

Get all task stats

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
        # Get all task stats
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
        # Get all task stats
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

Get time stamps

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
        # Get time stamps
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
        # Get time stamps
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

Get user

Get the user with the specified email address.

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
        # Get user
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
        # Get user
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

# **get_user_access_to_contracts_of_company_v3**
> GetUserAccessToContractsOfCompanyV3ApiResponse get_user_access_to_contracts_of_company_v3(company_id)

Get contract access of users

Get which user can access which contract of the company. 

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
        # Get contract access of users
        api_response = api_instance.get_user_access_to_contracts_of_company_v3(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_user_access_to_contracts_of_company_v3: %s\n" % e)
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
        # Get contract access of users
        api_response = api_instance.get_user_access_to_contracts_of_company_v3(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->get_user_access_to_contracts_of_company_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 

### Return type

[**GetUserAccessToContractsOfCompanyV3ApiResponse**](GetUserAccessToContractsOfCompanyV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All users and their accessible contracts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> list[ComPatagonaPricemonitorShareApiGetCompanyUsersUser] get_users(company_id)

Get all users of a company

This endpoint returns all users that are assigned to a company. It is only accessible for admins or company admins.

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
        # Get all users of a company
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
        # Get all users of a company
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

[**list[ComPatagonaPricemonitorShareApiGetCompanyUsersUser]**](ComPatagonaPricemonitorShareApiGetCompanyUsersUser.md)

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

Get repricing settings

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
        # Get repricing settings
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
        # Get repricing settings
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

Get vendor and shops for contract

Get vendor along with their associated shop for given vendor id and manufacturer contract.

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
        # Get vendor and shops for contract
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
        # Get vendor and shops for contract
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

Get all vendors and shops for contract

Get all the vendors along with their associated shops for a specified manufacturer contract.

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
        # Get all vendors and shops for contract
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
        # Get all vendors and shops for contract
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

Get contract [vendor]

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
        # Get contract [vendor]
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
        # Get contract [vendor]
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

Get contract [vendor]

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
        # Get contract [vendor]
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
        # Get contract [vendor]
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

Get vendors by domain

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
        # Get vendors by domain
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
        # Get vendors by domain
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

Get list of vendors

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
        # Get list of vendors
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
        # Get list of vendors
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

Log in with authentication token

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
        # Log in with authentication token
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

Log out

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
        # Log out
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

Update monitoring pipeline [manufacturer]

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
        # Update monitoring pipeline [manufacturer]
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
        # Update monitoring pipeline [manufacturer]
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

Update monitoring pipeline [vendor]

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
        # Update monitoring pipeline [vendor]
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
        # Update monitoring pipeline [vendor]
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

Update monitoring pipeline search attempts [manufacturer]

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
        # Update monitoring pipeline search attempts [manufacturer]
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
        # Update monitoring pipeline search attempts [manufacturer]
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

Update monitoring pipeline search attempts [vendor]

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
        # Update monitoring pipeline search attempts [vendor]
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
        # Update monitoring pipeline search attempts [vendor]
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

Update product [manufacturer]

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
        # Update product [manufacturer]
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
        # Update product [manufacturer]
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

Update product [vendor]

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
        # Update product [vendor]
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
        # Update product [vendor]
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

Update position distribution

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
        # Update position distribution
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
        # Update position distribution
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

Create user account

Create a new user account.

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
        # Create user account
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
**400** | Returned if: - The Request body is not a valid JSON string - The user account name is empty - The email doesn&#39;t match a valid email format - The password length is less than 6 characters long - The endpoint was requested too often - The given email address already exists  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_activate_marketplace_vendor_v3**
> ActivateMarketplaceResponseV3ApiResponse post_activate_marketplace_vendor_v3(company_id, com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3=com_patagona_pricemonitor_share_api_post_activate_marketplace_request_v3)

Activate Amazon marketplace

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
        # Activate Amazon marketplace
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
        # Activate Amazon marketplace
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

Set up authorization for Amazon seller account

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
        # Set up authorization for Amazon seller account
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
        # Set up authorization for Amazon seller account
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

Update Ebay authorization

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
        # Update Ebay authorization
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
        # Update Ebay authorization
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

Retrieve Looker embed SSO url [manufacturer]

Retrieve an embed SSO url for Looker for a manufacturer contract.

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
        # Retrieve Looker embed SSO url [manufacturer]
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
        # Retrieve Looker embed SSO url [manufacturer]
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

Retrieve Looker embed SSO url [vendor]

Retrieve an embed SSO url for Looker for a vendor contract.

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
        # Retrieve Looker embed SSO url [vendor]
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
        # Retrieve Looker embed SSO url [vendor]
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

Create feed

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
        # Create feed
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
        # Create feed
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

Update product identifier mapping

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
        # Update product identifier mapping
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
        # Update product identifier mapping
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

Add monitoring schedule for contract [manufacturer]

Add a monitoring schedule for a given manufacturer contract.

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
        # Add monitoring schedule for contract [manufacturer]
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
        # Add monitoring schedule for contract [manufacturer]
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

Add monitoring schedule for contract

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
        # Add monitoring schedule for contract
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
        # Add monitoring schedule for contract
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

Get offer statistics per product

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
        # Get offer statistics per product
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
        # Get offer statistics per product
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

Add new vendor to contract and associate shops

Add a new vendor for a given manufacturer contract and associate shops with the given vendor.

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
        # Add new vendor to contract and associate shops
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
        # Add new vendor to contract and associate shops
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

Query prices by day by product

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
        # Query prices by day by product
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
        # Query prices by day by product
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

Publish preprocessing task [vendor]

Publish a preprocessing task for a vendor.

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
        # Publish preprocessing task [vendor]
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
        # Publish preprocessing task [vendor]
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

# **put_admin_domain_control_panel_v3**
> PutAdminDomainResponseV3ApiResponse put_admin_domain_control_panel_v3(domain, com_patagona_pricemonitor_share_api_put_admin_domain_request_v3=com_patagona_pricemonitor_share_api_put_admin_domain_request_v3)

Update or add domain

Update an existing domain or add a new domain in case domain does not exist.

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
    domain = 'google.com' # str | Fully qualified domain name
com_patagona_pricemonitor_share_api_put_admin_domain_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutAdminDomainRequestV3() # ComPatagonaPricemonitorShareApiPutAdminDomainRequestV3 | The domain to be updated or added and its offer sources (optional)

    try:
        # Update or add domain
        api_response = api_instance.put_admin_domain_control_panel_v3(domain, com_patagona_pricemonitor_share_api_put_admin_domain_request_v3=com_patagona_pricemonitor_share_api_put_admin_domain_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_admin_domain_control_panel_v3: %s\n" % e)
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
    domain = 'google.com' # str | Fully qualified domain name
com_patagona_pricemonitor_share_api_put_admin_domain_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutAdminDomainRequestV3() # ComPatagonaPricemonitorShareApiPutAdminDomainRequestV3 | The domain to be updated or added and its offer sources (optional)

    try:
        # Update or add domain
        api_response = api_instance.put_admin_domain_control_panel_v3(domain, com_patagona_pricemonitor_share_api_put_admin_domain_request_v3=com_patagona_pricemonitor_share_api_put_admin_domain_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_admin_domain_control_panel_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Fully qualified domain name | 
 **com_patagona_pricemonitor_share_api_put_admin_domain_request_v3** | [**ComPatagonaPricemonitorShareApiPutAdminDomainRequestV3**](ComPatagonaPricemonitorShareApiPutAdminDomainRequestV3.md)| The domain to be updated or added and its offer sources | [optional] 

### Return type

[**PutAdminDomainResponseV3ApiResponse**](PutAdminDomainResponseV3ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A domain was updated or added. |  -  |
**400** | Domain could not be updated or added. - Offer sources must be valid - Domain must be a valid internet domain and non-empty - Domain name must be unique and non-empty - Please refer to the request schema for what constitutes valid offer sources and a valid domain |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_callbacks**
> put_callbacks(contract_id, com_patagona_pricemonitor_share_api_callbacks)

Update callbacks [manufacturer]

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
com_patagona_pricemonitor_share_api_callbacks = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCallbacks() # ComPatagonaPricemonitorShareApiCallbacks | Callbacks

    try:
        # Update callbacks [manufacturer]
        api_instance.put_callbacks(contract_id, com_patagona_pricemonitor_share_api_callbacks)
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
com_patagona_pricemonitor_share_api_callbacks = pricemonitor_api_client.ComPatagonaPricemonitorShareApiCallbacks() # ComPatagonaPricemonitorShareApiCallbacks | Callbacks

    try:
        # Update callbacks [manufacturer]
        api_instance.put_callbacks(contract_id, com_patagona_pricemonitor_share_api_callbacks)
    except ApiException as e:
        print("Exception when calling InternalApi->put_callbacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_callbacks** | [**ComPatagonaPricemonitorShareApiCallbacks**](ComPatagonaPricemonitorShareApiCallbacks.md)| Callbacks | 

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

# **put_csv_products**
> put_csv_products(contract_id, body)

Set products via CSV file (V2)

Warning: Deletes all existing products.         <br/>Note that this will not happen immediately. Instead, you receive the ID of a task that has been created.         <br/>Furthermore you receive an URL which you can use to check if the task was executed successfully.         <br>The csv file must contain following columns:         <ul>           <li>productId - arbitrary string, can be used for the systems product id.</li>           <li>gtin - the GTIN of the product           <li>description - name or short description of the product           <li>referencePrice - arbitrary decimal number, usually the current price or recommended retail price (gross)           <li>minPriceBoundary - decimal number defining the lower price boundary (gross)           <li>maxPriceBoundary - decimal number defining the upper price boundary (gross)           <li>Additional columns are added as product tags. Tags are used for repricing strategies and several other           purpose.         </ul>         <br/>Column separator must be semicolon, the decimal separator must be dot. File encoding must be UTF-8.

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
body = 'body_example' # str | CSV file containing the products

    try:
        # Set products via CSV file (V2)
        api_instance.put_csv_products(contract_id, body)
    except ApiException as e:
        print("Exception when calling InternalApi->put_csv_products: %s\n" % e)
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
body = 'body_example' # str | CSV file containing the products

    try:
        # Set products via CSV file (V2)
        api_instance.put_csv_products(contract_id, body)
    except ApiException as e:
        print("Exception when calling InternalApi->put_csv_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **body** | **str**| CSV file containing the products | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | - |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_csv_products_manufacturer_v3**
> PutProductsApiResponse put_csv_products_manufacturer_v3(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)

Set products via CSV file (V3)

This operation is used to import products into the pricemonitor. This process is represented by a task, which is processed asynchronously. In the response you will receive a url which is used to check the status of the import process. <br>  When the process is done all products in csv file from the request body will be in the pricemonitor. Products that were already present before have been updated and new products have been added. <br>  Warning: All products that were in the pricemonitor before but are not present in the new import will be deleted.  Identification of the products is done based on the identifying attributes (see parameter: patagona-product-identifying-attributes)'

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
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | Comma separated list of csv columns that identify a product uniquely
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products. Note: The CSV file should be encoded in UTF-8.
patagona_product_gtin = 'gtin-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Set products via CSV file (V3)
        api_response = api_instance.put_csv_products_manufacturer_v3(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_csv_products_manufacturer_v3: %s\n" % e)
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
content_type = 'text/csv' # str | 
patagona_product_identifying_attributes = 'id-column' # str | Comma separated list of csv columns that identify a product uniquely
patagona_product_name = 'name-column' # str | Csv column that contains the product name
patagona_product_reference_price = 'reference-price-column' # str | Csv column that contains the reference price
patagona_decimal_separator = '.' # str | Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \",\", \".\"
patagona_csv_column_separator = ',' # str | The csv column separator \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
patagona_csv_quotation_character = '\"' # str | The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another.
body = 'body_example' # str | CSV file containing the products. Note: The CSV file should be encoded in UTF-8.
patagona_product_gtin = 'gtin-column' # str | Csv column that contains the gtin (optional)
patagona_product_customer_id = 'id-column' # str | Csv column that contains an id (There is no requirement for this field to be unique) (optional)

    try:
        # Set products via CSV file (V3)
        api_response = api_instance.put_csv_products_manufacturer_v3(contract_id, content_type, patagona_product_identifying_attributes, patagona_product_name, patagona_product_reference_price, patagona_decimal_separator, patagona_csv_column_separator, patagona_csv_quotation_character, body, patagona_product_gtin=patagona_product_gtin, patagona_product_customer_id=patagona_product_customer_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_csv_products_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **content_type** | **str**|  | 
 **patagona_product_identifying_attributes** | **str**| Comma separated list of csv columns that identify a product uniquely | 
 **patagona_product_name** | **str**| Csv column that contains the product name | 
 **patagona_product_reference_price** | **str**| Csv column that contains the reference price | 
 **patagona_decimal_separator** | **str**| Decimal separator used for parsing numbers \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. \\ Available values: \&quot;,\&quot;, \&quot;.\&quot; | 
 **patagona_csv_column_separator** | **str**| The csv column separator \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **patagona_csv_quotation_character** | **str**| The csv quotation character \\ The values for patagona-decimal-separator, patagona-csv-column-separator and patagona-csv-quotation-character must be different from one another. | 
 **body** | **str**| CSV file containing the products. Note: The CSV file should be encoded in UTF-8. | 
 **patagona_product_gtin** | **str**| Csv column that contains the gtin | [optional] 
 **patagona_product_customer_id** | **str**| Csv column that contains an id (There is no requirement for this field to be unique) | [optional] 

### Return type

[**PutProductsApiResponse**](PutProductsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The field data.url in the returned object allows to check the status of the import process. It will point to the endpoint GET /api/2/v/contracts/{contractId}/tasks/{taskId}. \\ The field data.id is the task id corresponding to the product import. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_currency_vendor_v2**
> object put_currency_vendor_v2(contract_id, body=body)

Update currency settings [vendor]

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
        # Update currency settings [vendor]
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
        # Update currency settings [vendor]
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

Update contract settings [manufacturer]

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
        # Update contract settings [manufacturer]
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
        # Update contract settings [manufacturer]
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

Update customer contract settings [vendor]

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
        # Update customer contract settings [vendor]
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
        # Update customer contract settings [vendor]
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

Update dynamic monitoring settings

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
        # Update dynamic monitoring settings
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
        # Update dynamic monitoring settings
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

Update feed

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
        # Update feed
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
        # Update feed
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

Update image tag [manufacturer]

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
        # Update image tag [manufacturer]
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
        # Update image tag [manufacturer]
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

Update image tag [vendor]

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
        # Update image tag [vendor]
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
        # Update image tag [vendor]
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

Update import settings

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
        # Update import settings
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
        # Update import settings
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

Update monitoring schedule for contract [manufacturer]

Update a monitoring schedule for a given manufacturer contract.

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
        # Update monitoring schedule for contract [manufacturer]
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
        # Update monitoring schedule for contract [manufacturer]
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

Update monitoring schedule for contract [vendor]

Update a monitoring schedule for a given vendor contract.

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
        # Update monitoring schedule for contract [vendor]
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
        # Update monitoring schedule for contract [vendor]
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

Update monitoring settings for contract

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
        # Update monitoring settings for contract
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
        # Update monitoring settings for contract
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

Update monitoring settings [manufacturer]

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
        # Update monitoring settings [manufacturer]
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
        # Update monitoring settings [manufacturer]
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

Update monitoring settings [vendor]

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
        # Update monitoring settings [vendor]
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
        # Update monitoring settings [vendor]
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

Update monitoring settings [vendor]

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
        # Update monitoring settings [vendor]
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
        # Update monitoring settings [vendor]
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

Store vendor filters for contract

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
        # Store vendor filters for contract
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
        # Store vendor filters for contract
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

Update offer retention settings [manufacturer]

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
        # Update offer retention settings [manufacturer]
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
        # Update offer retention settings [manufacturer]
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

Update offer retention settings [vendor]

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
        # Update offer retention settings [vendor]
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
        # Update offer retention settings [vendor]
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

# **put_product_properties_v3**
> EmptyApiResponse put_product_properties_v3(contract_id, product_id, com_patagona_pricemonitor_share_api_put_product_properties_request_v3)

Manage product properties for a product

This endpoint allows creating, updating, or deleting product properties for a certain product and contract. For deleting product properties, it's sufficient to provide an empty list of product properties. When providing dates, please use the ISO 8601 format. When providing numbers, please use dot as decimal separator.  Product properties represent additional information for a product, independent of imported products and tags. 

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
product_id = 12345678 # int | ID of the product (Omnia's internal product id)
com_patagona_pricemonitor_share_api_put_product_properties_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3() # ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3 | 

    try:
        # Manage product properties for a product
        api_response = api_instance.put_product_properties_v3(contract_id, product_id, com_patagona_pricemonitor_share_api_put_product_properties_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_product_properties_v3: %s\n" % e)
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
product_id = 12345678 # int | ID of the product (Omnia's internal product id)
com_patagona_pricemonitor_share_api_put_product_properties_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3() # ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3 | 

    try:
        # Manage product properties for a product
        api_response = api_instance.put_product_properties_v3(contract_id, product_id, com_patagona_pricemonitor_share_api_put_product_properties_request_v3)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_product_properties_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **product_id** | **int**| ID of the product (Omnia&#39;s internal product id) | 
 **com_patagona_pricemonitor_share_api_put_product_properties_request_v3** | [**ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3**](ComPatagonaPricemonitorShareApiPutProductPropertiesRequestV3.md)|  | 

### Return type

[**EmptyApiResponse**](EmptyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The product properties have been stored successfully for the product. |  -  |
**400** | Returned if the request body is invalid: - The request body is not a valid JSON string. - The provided product properties contain duplicated keys. - The provided product properties contain an empty key. - The provided product properties contain a key which is too long. - The provided product properties contain a value which is too long.  |  -  |
**404** | Returned if the product does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_products_csv_manufacturer_v2**
> object put_products_csv_manufacturer_v2(contract_id, body=body)

Set products via CSV file [manufacturer]

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
        # Set products via CSV file [manufacturer]
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
        # Set products via CSV file [manufacturer]
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

Update products in bulk (JSON)

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
        # Update products in bulk (JSON)
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
        # Update products in bulk (JSON)
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

Update repricing strategy

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
        # Update repricing strategy
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
        # Update repricing strategy
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

Update settings for contract

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
        # Update settings for contract
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
        # Update settings for contract
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

# **put_user_access_to_contracts_of_company_v3**
> EmptyApiResponse put_user_access_to_contracts_of_company_v3(company_id, com_patagona_pricemonitor_share_api_user_access_to_contracts_of_company=com_patagona_pricemonitor_share_api_user_access_to_contracts_of_company)

Set contract access of users

Users can either access all contracts of a company or only dedicated contracts. With this api endpoint one can control the access rights of a user. 

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
com_patagona_pricemonitor_share_api_user_access_to_contracts_of_company = pricemonitor_api_client.ComPatagonaPricemonitorShareApiUserAccessToContractsOfCompany() # ComPatagonaPricemonitorShareApiUserAccessToContractsOfCompany | All users and their accessible contracts (optional)

    try:
        # Set contract access of users
        api_response = api_instance.put_user_access_to_contracts_of_company_v3(company_id, com_patagona_pricemonitor_share_api_user_access_to_contracts_of_company=com_patagona_pricemonitor_share_api_user_access_to_contracts_of_company)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_user_access_to_contracts_of_company_v3: %s\n" % e)
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
com_patagona_pricemonitor_share_api_user_access_to_contracts_of_company = pricemonitor_api_client.ComPatagonaPricemonitorShareApiUserAccessToContractsOfCompany() # ComPatagonaPricemonitorShareApiUserAccessToContractsOfCompany | All users and their accessible contracts (optional)

    try:
        # Set contract access of users
        api_response = api_instance.put_user_access_to_contracts_of_company_v3(company_id, com_patagona_pricemonitor_share_api_user_access_to_contracts_of_company=com_patagona_pricemonitor_share_api_user_access_to_contracts_of_company)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->put_user_access_to_contracts_of_company_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| ID of a company | 
 **com_patagona_pricemonitor_share_api_user_access_to_contracts_of_company** | [**ComPatagonaPricemonitorShareApiUserAccessToContractsOfCompany**](ComPatagonaPricemonitorShareApiUserAccessToContractsOfCompany.md)| All users and their accessible contracts | [optional] 

### Return type

[**EmptyApiResponse**](EmptyApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty response signalling that the changes have been applied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_vendor_settings_vendor_v2**
> object put_vendor_settings_vendor_v2(contract_id, body=body)

Update repricing settings

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
        # Update repricing settings
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
        # Update repricing settings
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

Update vendor for contract and associate shops

Update an existing vendor for a given manufacturer contract and associate shops with the given vendor.

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
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for updating an existing vendor and associate shops with it. Please note that at least one shop is required for a successful creation. (optional)

    try:
        # Update vendor for contract and associate shops
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
com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3 = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3() # ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3 | Request body for updating an existing vendor and associate shops with it. Please note that at least one shop is required for a successful creation. (optional)

    try:
        # Update vendor for contract and associate shops
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
 **com_patagona_pricemonitor_share_api_post_vendor_shop_mapping_request_v3** | [**ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3**](ComPatagonaPricemonitorShareApiPostVendorShopMappingRequestV3.md)| Request body for updating an existing vendor and associate shops with it. Please note that at least one shop is required for a successful creation. | [optional] 

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

Query offers [manufacturer]

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
        # Query offers [manufacturer]
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
        # Query offers [manufacturer]
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

# **query_offers_price_dumping_stats_manufacturer_v3**
> QueryPriceDumpingStatsApiResponse query_offers_price_dumping_stats_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)

Query price dumping statistics

This operation is used to query price dumping statistics for a time range for a set of shops.

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
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        # Query price dumping statistics
        api_response = api_instance.query_offers_price_dumping_stats_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_price_dumping_stats_manufacturer_v3: %s\n" % e)
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
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        # Query price dumping statistics
        api_response = api_instance.query_offers_price_dumping_stats_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_price_dumping_stats_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_price_dumping_stats_request** | [**ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest**](ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest.md)|  | 

### Return type

[**QueryPriceDumpingStatsApiResponse**](QueryPriceDumpingStatsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the price dumping statistics in the given time range. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_price_dumping_stats_vendor_v3**
> QueryPriceDumpingStatsApiResponse query_offers_price_dumping_stats_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)

Query price dumping statistics

This operation is used to query price dumping statistics for a time range for a set of shops.

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
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        # Query price dumping statistics
        api_response = api_instance.query_offers_price_dumping_stats_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_price_dumping_stats_vendor_v3: %s\n" % e)
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
com_patagona_pricemonitor_share_api_price_dumping_stats_request = pricemonitor_api_client.ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest() # ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest | 

    try:
        # Query price dumping statistics
        api_response = api_instance.query_offers_price_dumping_stats_vendor_v3(contract_id, com_patagona_pricemonitor_share_api_price_dumping_stats_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_price_dumping_stats_vendor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_price_dumping_stats_request** | [**ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest**](ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest.md)|  | 

### Return type

[**QueryPriceDumpingStatsApiResponse**](QueryPriceDumpingStatsApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the price dumping statistics in the given time range. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_offers_shop_manufacturer_v3**
> QueryOffersOfShopV3ApiResponse query_offers_shop_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_query_offers_of_shop_request_v3)

Get all offers [manufacturer]

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
        # Get all offers [manufacturer]
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
        # Get all offers [manufacturer]
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

Get all offers [vendor]

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
        # Get all offers [vendor]
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
        # Get all offers [vendor]
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

Query offer statistics per product

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
        # Query offer statistics per product
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
        # Query offer statistics per product
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

# **query_offers_stats_manufacturer_v31**
> QueryOfferStatisticsV31ApiResponse query_offers_stats_manufacturer_v31(contract_id, com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31=com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31)

Query offer statistics per product

This endpoint can be used to query offer statistics (e.g. offer count, average price) grouped by product. Only the most recent market data is considered per product and domain. 

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
com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-10-17T08:00:00Z","end":"2023-10-19T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"productId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. This is particularly useful when querying a set of customerProductId's. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000. The allowed query pattern is structured as follows: ``` json {   \"pagination\": {     \"start\": ${start},     \"limit\": ${limit}   },   \"range\": {     \"start\": ${start},     \"end\": ${end}   },   \"filter\": {     \"oneOf\": {       \"field\": \"customerProductId\",       \"values\": [${customerProductIds as a list of strings}]     }   } } ``` (optional)

    try:
        # Query offer statistics per product
        api_response = api_instance.query_offers_stats_manufacturer_v31(contract_id, com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31=com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_stats_manufacturer_v31: %s\n" % e)
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
com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31 = {"pagination":{"start":0,"limit":10},"range":{"start":"2023-10-17T08:00:00Z","end":"2023-10-19T08:00:00Z"},"filter":{"oneOf":{"field":"customerProductId","values":["1","2","3","4","5","6","7","8","9","10"]}}} # ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31 | The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \"customerProductId\"   - \"productId\" (Patagona's internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \"productId\" for queries when a product query is utilized.  Pagination operates based on the provided products query. This is particularly useful when querying a set of customerProductId's. For chunked requests over a set of ids, it's straightforward to specify up to 10,000 customerProductId's in the query with pagination set at start: 0, limit: 10,000. The allowed query pattern is structured as follows: ``` json {   \"pagination\": {     \"start\": ${start},     \"limit\": ${limit}   },   \"range\": {     \"start\": ${start},     \"end\": ${end}   },   \"filter\": {     \"oneOf\": {       \"field\": \"customerProductId\",       \"values\": [${customerProductIds as a list of strings}]     }   } } ``` (optional)

    try:
        # Query offer statistics per product
        api_response = api_instance.query_offers_stats_manufacturer_v31(contract_id, com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31=com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_offers_stats_manufacturer_v31: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_post_offer_statistics_request_v31** | [**ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31**](ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31.md)| The request body may include an optional products query. If omitted, all products are queried. Currently, product queries can be performed on two attributes:   - \&quot;customerProductId\&quot;   - \&quot;productId\&quot; (Patagona&#39;s internal product id; must be a numerical integer)  Pagination is supported with a maximum limit of 10,000. For optimized performance:   - Use a limit of 10,000 products per page when querying all products of a contract.   - Prefer using \&quot;productId\&quot; for queries when a product query is utilized.  Pagination operates based on the provided products query. This is particularly useful when querying a set of customerProductId&#39;s. For chunked requests over a set of ids, it&#39;s straightforward to specify up to 10,000 customerProductId&#39;s in the query with pagination set at start: 0, limit: 10,000. The allowed query pattern is structured as follows: &#x60;&#x60;&#x60; json {   \&quot;pagination\&quot;: {     \&quot;start\&quot;: ${start},     \&quot;limit\&quot;: ${limit}   },   \&quot;range\&quot;: {     \&quot;start\&quot;: ${start},     \&quot;end\&quot;: ${end}   },   \&quot;filter\&quot;: {     \&quot;oneOf\&quot;: {       \&quot;field\&quot;: \&quot;customerProductId\&quot;,       \&quot;values\&quot;: [${customerProductIds as a list of strings}]     }   } } &#x60;&#x60;&#x60; | [optional] 

### Return type

[**QueryOfferStatisticsV31ApiResponse**](QueryOfferStatisticsV31ApiResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of offer statistics per product. When a product has no market data then no offer statistics are returned for that product.  |  -  |
**400** | A &#x60;400&#x60; error is returned under the following conditions: - The request body JSON is unparsable. - An unsupported filter is provided. - The specified time range exceeds 48 hours. - The pagination limit exceeds 10,000.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_price_recommendations_vendor_v2**
> QueryPriceRecommendationsV2ApiResponse query_price_recommendations_vendor_v2(contract_id, price_recommendation_api_query_v2=price_recommendation_api_query_v2)

Query price recommendations

This endpoint is used to query certain price recommendations. It supports a rather complex filtering structure. Most commonly it's used for querying by our internal product id.  Here you can find an example request body for querying one product id (here `123456`):  <details> <summary>Click to expand</summary>  ``` json {   \"pagination\": {     \"start\": 0,     \"limit\": 500   },   \"range\": {     \"start\": \"2023-01-07T12:05:01.000Z\",     \"end\": \"2023-01-09T12:05:01.000Z\"   },   \"filter\": {     \"filters\": [{       \"left\": {         \"attributeName\": \"productId\",         \"type\": \"StringValueProvider\"       },       \"right\": {         \"value\": \"123456\",         \"type\": \"StringConstantValueProvider\"       },       \"comparison\": {         \"type\": \"StringEquality\"       },       \"type\": \"ComparisonFilter\"     }],     \"type\": \"OrFilter\"   } } ``` </details>  If you want to query for multiple product ids, then you need to provide one object per product id in the filters-array.  It's recommended to query for at most 1000 price recommendations at once.

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
        # Query price recommendations
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
        # Query price recommendations
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

Get products of a contract

This endpoint can be used for querying either all products or certain products by product ids.

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
        # Get products of a contract
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
        # Get products of a contract
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

Query products of a contract

This endpoint can be used for querying either all products or certain products by product ids.

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
        # Query products of a contract
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
        # Query products of a contract
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

# **query_products_manufacturer_v3**
> QueryProductsManufacturerV3ApiResponse query_products_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)

Query products for manufacturer

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
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> For better performance, when paginating over all products of a contract, we recommend to use a limit of 10000 products per page. Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br>  (optional)

    try:
        # Query products for manufacturer
        api_response = api_instance.query_products_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_products_manufacturer_v3: %s\n" % e)
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
com_patagona_pricemonitor_share_api_api_query = pricemonitor_api_client.ComPatagonaPricemonitorShareApiApiQuery() # ComPatagonaPricemonitorShareApiApiQuery | The body contains the products query. <br> Currently, it supports only product queries for two attributes:<br> <ul>   <li> by \"customerProductId\"</li>   <li> by \"productId\" (Patagona's internal product id). Allowed values for 'productId' are numerical integer values</li> </ul> The maximum allowed limit in the pagination is 10000. <br> For better performance, when paginating over all products of a contract, we recommend to use a limit of 10000 products per page. Pagination works with respective to the given products query. <br> This is most relevant when querying for a set of customerProductId's. <br> When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId's in the query and keep the pagination at start: 0, limit: 10000. <br> The only allowed pattern is currently: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": ${start}, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": ${limit} <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [${customerProductIds as a list of strings}] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br> <br> example: <br> { <br> &nbsp;&nbsp;\"pagination\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;\"start\": 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;\"limit\": 10 <br> &nbsp;&nbsp;}, <br> &nbsp;&nbsp;\"filter\": { <br> &nbsp;&nbsp;\"oneOf\": { <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"field\": \"customerProductId\", <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"values\": [\"1\", \"2\", \"3\", \"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \"10\"] <br> &nbsp;&nbsp;&nbsp;&nbsp;} <br> &nbsp;&nbsp;} <br> } <br>  (optional)

    try:
        # Query products for manufacturer
        api_response = api_instance.query_products_manufacturer_v3(contract_id, com_patagona_pricemonitor_share_api_api_query=com_patagona_pricemonitor_share_api_api_query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InternalApi->query_products_manufacturer_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| ID of the contract | 
 **com_patagona_pricemonitor_share_api_api_query** | [**ComPatagonaPricemonitorShareApiApiQuery**](ComPatagonaPricemonitorShareApiApiQuery.md)| The body contains the products query. &lt;br&gt; Currently, it supports only product queries for two attributes:&lt;br&gt; &lt;ul&gt;   &lt;li&gt; by \&quot;customerProductId\&quot;&lt;/li&gt;   &lt;li&gt; by \&quot;productId\&quot; (Patagona&#39;s internal product id). Allowed values for &#39;productId&#39; are numerical integer values&lt;/li&gt; &lt;/ul&gt; The maximum allowed limit in the pagination is 10000. &lt;br&gt; For better performance, when paginating over all products of a contract, we recommend to use a limit of 10000 products per page. Pagination works with respective to the given products query. &lt;br&gt; This is most relevant when querying for a set of customerProductId&#39;s. &lt;br&gt; When the requests are chunked over a set of ids, it is easiest to provide up to 10000 customerProductId&#39;s in the query and keep the pagination at start: 0, limit: 10000. &lt;br&gt; The only allowed pattern is currently: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: ${start}, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: ${limit} &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [${customerProductIds as a list of strings}] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; } &lt;br&gt; &lt;br&gt; example: &lt;br&gt; { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;pagination\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;start\&quot;: 0, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;limit\&quot;: 10 &lt;br&gt; &amp;nbsp;&amp;nbsp;}, &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;filter\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;\&quot;oneOf\&quot;: { &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;field\&quot;: \&quot;customerProductId\&quot;, &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;values\&quot;: [\&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot;, \&quot;4\&quot;, \&quot;5\&quot;, \&quot;6\&quot;, \&quot;7\&quot;, \&quot;8\&quot;, \&quot;9\&quot;, \&quot;10\&quot;] &lt;br&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &lt;br&gt; &amp;nbsp;&amp;nbsp;} &lt;br&gt; } &lt;br&gt;  | [optional] 

### Return type

[**QueryProductsManufacturerV3ApiResponse**](QueryProductsManufacturerV3ApiResponse.md)

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

Get offers for contract

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
        # Get offers for contract
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
        # Get offers for contract
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

Remove user from company

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
        # Remove user from company
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
        # Remove user from company
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

Update includes delivery costs setting

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
        # Update includes delivery costs setting
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
        # Update includes delivery costs setting
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

Delete scheduler operation [manufacturer]

The DELETE request is proxied to the internal Scheduler API.

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
        # Delete scheduler operation [manufacturer]
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
        # Delete scheduler operation [manufacturer]
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

Delete scheduler operation

The DELETE request is proxied to the internal Scheduler API.

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
        # Delete scheduler operation
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
        # Delete scheduler operation
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

Get scheduler operation [manufacturer]

The GET request is proxied to the internal Scheduler API.

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
        # Get scheduler operation [manufacturer]
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
        # Get scheduler operation [manufacturer]
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

Get scheduler operation [vendor]

The GET request is proxied to the internal Scheduler API.

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
        # Get scheduler operation [vendor]
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
        # Get scheduler operation [vendor]
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

Create scheduler operation [manufacturer]

The POST request is proxied to the internal Scheduler API.

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
        # Create scheduler operation [manufacturer]
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
        # Create scheduler operation [manufacturer]
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

Create scheduler operation

The POST request is proxied to the internal Scheduler API.

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
        # Create scheduler operation
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
        # Create scheduler operation
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

Update scheduler operation [manufacturer]

The PUT request is proxied to the internal Scheduler API.

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
        # Update scheduler operation [manufacturer]
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
        # Update scheduler operation [manufacturer]
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

Update scheduler operation

The PUT request is proxied to the internal Scheduler API.

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
        # Update scheduler operation
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
        # Update scheduler operation
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

Update segment offers [manufacturer]

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
        # Update segment offers [manufacturer]
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
        # Update segment offers [manufacturer]
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

Update segment offers [vendor]

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
        # Update segment offers [vendor]
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
        # Update segment offers [vendor]
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

Get shop integration

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
        # Get shop integration
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
        # Get shop integration
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

Update shop integration

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
        # Update shop integration
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
        # Update shop integration
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

Update shop integration import

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
        # Update shop integration import
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
        # Update shop integration import
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

Get contract statistics [manufacturer]

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
        # Get contract statistics [manufacturer]
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
        # Get contract statistics [manufacturer]
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

Get timestamps

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
        # Get timestamps
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
        # Get timestamps
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

Update alert settings

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
        # Update alert settings
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
        # Update alert settings
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

Update authentication token

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
        # Update authentication token
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
        # Update authentication token
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

Update task [manufacturer]

Update an existing task.

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
        # Update task [manufacturer]
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
        # Update task [manufacturer]
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

Update a task

Update the task with the specified id for the given contract.

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
        # Update a task
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
        # Update a task
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

Add user role

Add the specified role to the given user.

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
        # Add user role
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
        # Add user role
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

Validate offers [manufacturer]

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
        # Validate offers [manufacturer]
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
        # Validate offers [manufacturer]
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

Validate offers [vendor]

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
        # Validate offers [vendor]
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
        # Validate offers [vendor]
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

Get vendor export data

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
        # Get vendor export data
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
        # Get vendor export data
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

Get application version

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
        # Get application version
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

