/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.6671
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * This product query evaluates to \'true\' if the value of the \'field\' is one on the specified \'values\'.
 */
export interface PricemonitorPostOfferStatisticsOneOfV31 { 
    /**
     * Specifies the attribute to filter by. It accepts two values: <br> - \"customerProductId\": Your unique identifier for the product. <br> - \"productId\": Patagona\'s internal product id (must be a numerical integer).
     */
    field: string;
    /**
     * An array of strings containing the ids of the products to be queried.
     */
    values: Array<string>;
}
