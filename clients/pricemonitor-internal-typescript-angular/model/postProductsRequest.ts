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
import { PostProductsIdentifyingAttribute } from './postProductsIdentifyingAttribute';
import { PostProduct } from './postProduct';


/**
 * Request body which contains products
 */
export interface PostProductsRequest { 
    /**
     * Products which should be added to the pricemonitor
     */
    products: Array<PostProduct>;
    /**
     * Version of the request body. Only version 2 is supported.
     */
    version: PostProductsRequest.VersionEnum;
    /**
     * Non-empty list of product attributes which identify your products uniquely. Please ensure that you specify only one attribute in the list. Avoid using tags as an identifier, as this feature will soon be deprecated. By doing so, may loose historical market data during product import.
     */
    identifyingAttributes: Array<PostProductsIdentifyingAttribute>;
}
export namespace PostProductsRequest {
    export type VersionEnum = '2';
    export const VersionEnum = {
        _2: '2' as VersionEnum
    };
}


