/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.5360
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { OfferStatistics } from './offerStatistics';


export interface ProductOfferStatistics { 
    /**
     * The internal product id of the pricemonitor
     */
    productId?: string;
    /**
     * The offer statistics are grouped by domain.
     */
    statsByDomain?: { [key: string]: OfferStatistics; };
}
