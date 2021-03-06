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

case class PutAdminContractSettingsBody(
  name: String,
  expirationDate: Option[OffsetDateTime] = None,
  portals: Seq[String],
  features: ContractFeatures,
  id: Double,
  monitoringPriority: Option[Int] = None,
  `type`: String,
  sid: String,
  active: Boolean
) extends ApiModel


