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
import { PricemonitorContractFeatures } from './pricemonitorContractFeatures';


export interface PricemonitorGetContractSettingsResponseV1 { 
    /**
     * 
     */
    name: string;
    /**
     * 
     */
    expirationDate?: string;
    /**
     * 
     */
    portals: Array<string>;
    /**
     * 
     */
    includeDeliveryCosts: boolean;
    features: PricemonitorContractFeatures;
    /**
     * The name of the tag that contains the product image url
     */
    imageTag?: string;
    /**
     * 
     */
    company: string;
    /**
     * 
     */
    id: number;
    /**
     * Priority of the contract in the monitoring queue
     */
    monitoringPriority: number;
    /**
     * The contract\'s currency as three letter code
     */
    currency: string;
    type: string;
    /**
     * 
     */
    sid: string;
    /**
     * The name of the tag that contains the manufacturers suggested retail price
     */
    msrpTag?: string;
    /**
     * The name of the tag that contains the minimum advertised price
     */
    mapTag?: string;
    /**
     * 
     */
    active: boolean;
}

