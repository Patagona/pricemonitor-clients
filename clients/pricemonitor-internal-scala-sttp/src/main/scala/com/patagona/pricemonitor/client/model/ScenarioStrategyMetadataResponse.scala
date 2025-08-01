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
   * Metadata of a scenario strategy in an API response. Here the createdBy/updatedBy fields are e-mails, in [[com.patagona.pricemonitor.share.strategies.ScenarioStrategyMetadata]] these refer to ids
   */
case class ScenarioStrategyMetadataResponse(
  /* optional description of the scenario */
  description: Option[String] = None,
  /* unique identifier of the strategy scenario */
  id: Double,
  /* timestamp of last strategy update */
  updateDate: OffsetDateTime,
  /* e-mail of the user creating the strategy */
  createdBy: String,
  /* timestamp of when the strategy was created */
  creationDate: OffsetDateTime,
  /* up to 50 characters, has to be unique for one contract */
  title: String,
  /* schema version of the strategy */
  schemaVersion: Int,
  /* e-mail of the user that last updated the strategy */
  updatedBy: String
) extends ApiModel


