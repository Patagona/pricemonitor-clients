/**
 * Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts and more.
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.7155
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { PricemonitorCustomerOrderV3 } from './pricemonitorCustomerOrderV3';


/**
 * Request body containing bulked orders
 */
export interface PricemonitorPutCustomerOrdersRequestV3 { 
    /**
     * List of orders
     */
    orders: Array<PricemonitorCustomerOrderV3>;
    /**
     * Version of orders. Currently only \"3\" is allowed
     */
    version: string;
}

