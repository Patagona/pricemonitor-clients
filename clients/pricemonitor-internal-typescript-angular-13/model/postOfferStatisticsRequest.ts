/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.6128
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { TimeRange } from './timeRange';
import { ProductsFilter } from './productsFilter';


export interface PostOfferStatisticsRequest { 
    filter: ProductsFilter;
    includeDeliveryCosts: boolean;
    /**
     * Providing own shops names enables calculating shop positions. The keys are domain names. The values are lists of shop names.
     */
    ownShopNames: { [key: string]: Array<string>; };
    range: TimeRange;
}
