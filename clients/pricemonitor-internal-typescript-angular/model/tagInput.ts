/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.6436
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface TagInput { 
    /**
     * Must not be an empty string. Must not have more than 100 characters. All tags of one product need to have a unique key
     */
    key: string;
    /**
     * Must not have more than 10000 characters
     */
    value: string;
}
