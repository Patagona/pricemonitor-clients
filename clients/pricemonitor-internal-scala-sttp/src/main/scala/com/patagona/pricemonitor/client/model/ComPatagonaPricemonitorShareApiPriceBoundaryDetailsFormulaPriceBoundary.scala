/**
 * Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts and more.
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.7039
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.patagona.pricemonitor.client.model

import com.patagona.pricemonitor.client.core.ApiModel

  /**
   * The price boundary which has been calculated by a formula.
   */
case class ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary(
  /* The price boundary. */
  price: Double,
  /* The formula which has been used to calculate the price boundary. */
  formula: String,
  /* The relevant variables used in the formula. */
  variables: Seq[FormulaVariable]
) extends ApiModel

