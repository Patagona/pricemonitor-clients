/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.5542
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * This model describes a step in a paginated endpoint. It consists of the start index, set to 0 for the first page. The next page starts at (previous start) + limit. Reasonable values for the limit parameter depend on the specific endpoint.
 */
export interface PricemonitorPagination { 
    start: number;
    limit: number;
}
