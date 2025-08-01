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
import { PricemonitorProductPriceSimulationOutcome } from './pricemonitorProductPriceSimulationOutcome';
import { PricemonitorOwnShopMapping } from './pricemonitorOwnShopMapping';
import { PricemonitorOffsetTimeRange } from './pricemonitorOffsetTimeRange';


/**
 * Represents a bulk response with simulated price recommendations for multiple products.
 */
export interface PricemonitorPriceSimulationBulkResponseV3 { 
    strategyBuilder: object;
    /**
     * The timestamp for which the price calculation has been simulated.
     */
    calculationTimestamp: string;
    /**
     * The simulation results. All results are in order with respect to the input list of product simulation requests.
     */
    simulationResults: Array<PricemonitorProductPriceSimulationOutcome>;
    dataTimeRange: PricemonitorOffsetTimeRange;
    /**
     * The considered own shops.
     */
    ownShops: Array<PricemonitorOwnShopMapping>;
}

