/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.6521
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
  /* Origin of the offers. The domain needs to be set for the contract, otherwise, the offers will be rejected. */
  domain: String,
  /* Non-empty list of offers. */
  offers: Seq[ApiOfferV2]
) extends ApiModel

