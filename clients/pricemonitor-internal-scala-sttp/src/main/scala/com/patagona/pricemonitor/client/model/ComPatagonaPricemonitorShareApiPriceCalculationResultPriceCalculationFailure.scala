/**
 * Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts and more.
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.7155
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.patagona.pricemonitor.client.model

import com.patagona.pricemonitor.client.core.ApiModel

  /**
   * An exception occurred during the price calculation.
   */
case class ComPatagonaPricemonitorShareApiPriceCalculationResultPriceCalculationFailure(
  /* The reason why the price calculation failed. */
  reason: String,
  /* The ID of the node where the price calculation failed. */
  nodeId: Int
) extends ApiModel


