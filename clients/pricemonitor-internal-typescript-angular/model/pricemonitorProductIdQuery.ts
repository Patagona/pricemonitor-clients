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
 * This product query evaluates to \'true\' if the value of the \'field\' is one on the specified \'values\'.
 */
export interface PricemonitorProductIdQuery { 
    /**
     * Specifies the attribute to filter by. It accepts two values: <br> - \"customerProductId\": Your unique identifier for the product. <br> - \"productId\": Patagona\'s internal product id (must be a numerical integer).
     */
    field: string;
    /**
     * An array of strings containing the ids of the products to be queried.
     */
    values: Array<string>;
}

