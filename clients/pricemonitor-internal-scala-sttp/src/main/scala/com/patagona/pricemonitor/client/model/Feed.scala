/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.5687
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.patagona.pricemonitor.client.model

import java.time.OffsetDateTime
import com.patagona.pricemonitor.client.core.ApiModel

case class Feed(
  contractId: Option[String] = None,
  csvDecimalSeparator: Option[String] = None,
  csvSeparator: Option[String] = None,
  deltaUrl: Option[String] = None,
  fields: Option[Seq[FeedFields]] = None,
  format: Option[String] = None,
  id: Option[String] = None,
  lastAccessed: Option[OffsetDateTime] = None,
  lastDeletion: Option[OffsetDateTime] = None,
  name: Option[String] = None,
  url: Option[String] = None,
  version: Option[Long] = None
) extends ApiModel


