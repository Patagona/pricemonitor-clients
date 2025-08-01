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
import { PricemonitorUserCompany } from './pricemonitorUserCompany';


/**
 * This case class is used for serializing user-information for the account-endpoints
 */
export interface PricemonitorUserInfo { 
    /**
     * The user\'s name
     */
    name: string;
    /**
     * The companies of the user
     */
    companies: Array<PricemonitorUserCompany>;
    /**
     * The last time the user was active
     */
    lastActiveDate: string;
    /**
     * The user\'s mail-address
     */
    email: string;
    /**
     * The id of the user
     */
    id: number;
    /**
     * The user\'s role
     */
    roles: Array<string>;
}

