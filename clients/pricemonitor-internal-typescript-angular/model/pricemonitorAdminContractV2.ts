/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.5458
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * A contract used for data representation in the admin-endpoint
 */
export interface PricemonitorAdminContractV2 { 
    /**
     * The date and time the contract expires
     */
    expirationDate?: string;
    /**
     * The contract\'s description
     */
    description: string;
    /**
     * The id of the contract
     */
    id: string;
    /**
     * The date and time the contract was created
     */
    creationDate: string;
    type: PricemonitorAdminContractV2.TypeEnum;
    /**
     * The contract-status
     */
    active: boolean;
}
export namespace PricemonitorAdminContractV2 {
    export type TypeEnum = 'Pricemonitor for manufacturers' | 'Pricemonitor for resellers';
    export const TypeEnum = {
        Manufacturers: 'Pricemonitor for manufacturers' as TypeEnum,
        Resellers: 'Pricemonitor for resellers' as TypeEnum
    };
}

