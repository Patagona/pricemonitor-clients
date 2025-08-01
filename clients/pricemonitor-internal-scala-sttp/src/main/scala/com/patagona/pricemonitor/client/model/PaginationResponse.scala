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
   * This model describes the information passed to the user for a paginated request.
   */
case class PaginationResponse(
  /* the url that can be called to retrieve the next page, None if th last page has been requested */
  nextUrl: Option[String] = None,
  /* the total number of elements that is paginated over */
  totalSize: Int,
  /* the start index of the currently requested page */
  start: Int,
  /* the number of elements in a full page */
  limit: Int
) extends ApiModel


