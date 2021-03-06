/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.5687
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { PricemonitorProductPriceDumpingStats } from './pricemonitorProductPriceDumpingStats';


/**
 * This class contains the price dumping statistic for a single domain. A price dumping event exists if a vendor reduces the price below the minimum price at the previous timestamp while also selling the product at the new minimum price.
 */
export interface PricemonitorDomainPriceDumpingStats { 
    domain: string;
    productPriceDumpingStats: PricemonitorProductPriceDumpingStats;
}

