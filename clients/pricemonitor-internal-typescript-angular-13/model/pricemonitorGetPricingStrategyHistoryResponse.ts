/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.6521
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { PricemonitorStrategyMetadataResponseV3 } from './pricemonitorStrategyMetadataResponseV3';


/**
 * Version history of all strategies
 */
export interface PricemonitorGetPricingStrategyHistoryResponse { 
    /**
     * contains metadata of all strategies
     */
    history: Array<PricemonitorStrategyMetadataResponseV3>;
}
