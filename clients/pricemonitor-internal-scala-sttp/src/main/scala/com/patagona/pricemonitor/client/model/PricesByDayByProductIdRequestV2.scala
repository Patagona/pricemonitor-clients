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

import java.time.OffsetDateTime
import com.patagona.pricemonitor.client.core.ApiModel

  /**
   * A request for all known prices for a given day & product ID. Provides the option to filter the results using the `offerSelectors`.
   */
case class PricesByDayByProductIdRequestV2(
  /* The day for which to return the prices in ISO 8601 */
  day: OffsetDateTime,
  /* A list of `OfferSelector`s that allows filtering down the results. The selectors are combined using an OR operation. The list must contain at least one element. */
  offers: Seq[OfferSelector]
) extends ApiModel


