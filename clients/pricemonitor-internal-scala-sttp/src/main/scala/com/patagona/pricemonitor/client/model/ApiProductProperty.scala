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
package com.patagona.pricemonitor.client.model

import com.patagona.pricemonitor.client.core.ApiModel

  /**
   * Product properties represent additional information for a product. The `stringValue` is used for deriving further evaluated values at server-side: - **Date Properties**: Submit dates in the `stringValue` field using the ISO 8601 format (e.g., `YYYY-MM-DDTHH:MM:SSZ`). This ensures that the server correctly interprets the date and time. - **Numeric Properties**: Submit numbers in the `stringValue` field by using dot as decimal separator.
   */
case class ApiProductProperty(
  /* The name of the property. It can't be empty. At maximum 100 characters are allowed. */
  key: String,
  /* The text value of the property. At maximum 10,000 characters are allowed. */
  stringValue: String
) extends ApiModel


