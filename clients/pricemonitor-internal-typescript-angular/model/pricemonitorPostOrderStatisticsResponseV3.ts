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
 * Represents aggregated order statistics for a single product.
 */
export interface PricemonitorPostOrderStatisticsResponseV3 { 
    /**
     * Pricemonitor\'s internal unique product identifier.
     */
    productId: string;
    /**
     * The unique identifier of the sold item, expected to align with the customerProductId.
     */
    itemId: string;
    /**
     * The total count of how often the product has been sold.
     */
    numberOfSoldItems: number;
}

