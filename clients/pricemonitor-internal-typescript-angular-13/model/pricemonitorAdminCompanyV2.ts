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
import { PricemonitorAdminContractV2 } from './pricemonitorAdminContractV2';


/**
 * A company with its contracts used for data representation in the admin-endpoint
 */
export interface PricemonitorAdminCompanyV2 { 
    /**
     * The id of the company
     */
    id: number;
    /**
     * The company\'s name
     */
    name: string;
    /**
     * A list of the comapny\'s contracts
     */
    contracts: Array<PricemonitorAdminContractV2>;
}

