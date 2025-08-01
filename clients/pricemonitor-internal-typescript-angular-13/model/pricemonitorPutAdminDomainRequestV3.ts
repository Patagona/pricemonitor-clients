/**
 * Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts, and more.  This API supports both public endpoints for customer integration and internal endpoints for platform management. All endpoints are authenticated using either Basic Authentication or JWT Bearer tokens.
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.7216
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * Request body that contains information about updating an existing domain with new offerSources or adding a new domain
 */
export interface PricemonitorPutAdminDomainRequestV3 { 
    /**
     * display name for the domain in the UI. (Must be unique and non-empty)
     */
    name: string;
    /**
     * sources of offers on this domain. Allowed sources: \"DEFAULT_MONITORING\", \"CUSTOM_MONITORING\", \"OMNIA_CUSTOM_SPIDERING\", \"PUSH_API\", \"OTHER\" @example name = \"google\", offerSources = Set(\"DEFAULT_MONITORING\")
     */
    offerSources: Set<string>;
}

