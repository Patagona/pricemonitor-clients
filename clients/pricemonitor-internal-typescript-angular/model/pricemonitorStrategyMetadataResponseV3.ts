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
 * Metadata used for strategy versioning.
 */
export interface PricemonitorStrategyMetadataResponseV3 { 
    /**
     * strategy version per contract
     */
    documentVersion: number;
    /**
     * message provided by user when saving new strategy
     */
    documentVersionMessage?: string;
    /**
     * schema version of the strategy
     */
    version: string;
    /**
     * timestamp of last strategy update. It needs to be an option to ensure old strategies can be read.
     */
    updateDate?: string;
    /**
     * user email of the account that updated the strategy. It needs to be an option to ensure old strategies can be read.
     */
    updatedBy?: string;
}

