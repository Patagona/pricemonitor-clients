/**
 * Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts, and more.  This API supports both public endpoints for customer integration and internal endpoints for platform management. All endpoints are authenticated using either Basic Authentication or JWT Bearer tokens.
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.7183
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
   * Represents a single request to post offers for a snapshot. A snapshot is a unique combination of productId, creationDate, and domain.
   */
case class PostProductOfferRequest(
  /* Patagona's internal product id. */
  productId: String,
  /* ISO 8601 timestamp when the offers have been gathered. This timestamp needs to be more recent compared to already existing offers. Otherwise, the offers will be rejected. */
  creationDate: OffsetDateTime,
  /* Origin of the offers. */
  domain: String,
  /* Non-empty list of offers. */
  offers: Seq[ApiOfferV2]
) extends ApiModel


