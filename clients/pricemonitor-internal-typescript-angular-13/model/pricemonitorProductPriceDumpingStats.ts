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
 * This class contains the number of price dumping events. The counts prefixed with \"uniqueProduct\" only count the events once per product, the non prefixed counts count every event. If we are unable to detect which vendor reduced the price first, because we only sampled the price when multiple vendors are at the same price, those events are counted in the fields infixed with \"potetially\".
 */
export interface PricemonitorProductPriceDumpingStats { 
    /**
     * This field denotes the number of products at the min price from the queried vendors, at the respective newest timestamp per domain and product.
     */
    productsAtMinPrice: number;
    /**
     * 
     */
    uniqueProductInitiatedPriceDumpings: number;
    /**
     * 
     */
    uniqueProductPotentiallyInitiatedPriceDumpings: number;
    /**
     * 
     */
    initiatedPriceDumpings: number;
    /**
     * 
     */
    potentiallyInitiatedPriceDumpings: number;
}

