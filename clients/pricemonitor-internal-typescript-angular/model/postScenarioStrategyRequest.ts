/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.6498
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * Request body which contains the strategy and relevant metadata
 */
export interface PostScenarioStrategyRequest { 
    /**
     * Title of the scenario strategy. Should not be empty and a maximum of 50 chars is allowed
     */
    title: string;
    /**
     * Description of the scenario strategy. Maximum of 1000 chars allowed
     */
    description?: string;
    /**
     * Version of the schema the scenario strategy is encoded in
     */
    schemaVersion: number;
    /**
     * This is a placeholder for a pricing strategy. These are using advanced features and are not covered by openapi. If you need to work with pricing strategies please contract us.
     */
    strategy: object;
}
