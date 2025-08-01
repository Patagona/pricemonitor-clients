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


/**
 * Definition of a task to be created.
 */
export interface PricemonitorCreateTaskBodyV2 { 
    /**
     * The type of the task to be created. Can be any of [alert, backend.tasks.pricemonitor.offers.monitoring, backend.tasks.pricemonitor.offers.preprocessing, backend.tasks.pricemonitor.callback]
     */
    taskType: string;
    data?: object;
    /**
     * optional flag to specify whether or not to trigger the next task. Currently only integrated to trigger callbacks after preprocessing
     */
    triggerFollowUpTask?: boolean;
    /**
     * optional flag to specify whether or not to include the task in billing. This is especially useful when manual monitoring is triggered by our admins
     */
    includeForBilling?: boolean;
}

