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
 * Request body for resetting the password
 */
export interface PricemonitorPutResetPasswordRequest { 
    /**
     * Received via email after requesting a new password.
     */
    token: string;
    /**
     * Password entered by the user.
     */
    password: string;
}
