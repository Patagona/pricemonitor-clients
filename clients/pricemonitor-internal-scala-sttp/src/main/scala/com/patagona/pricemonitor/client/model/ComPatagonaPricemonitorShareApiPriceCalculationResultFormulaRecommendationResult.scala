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
   * A price recommendation has been calculated by a formula.
   */
case class ComPatagonaPricemonitorShareApiPriceCalculationResultFormulaRecommendationResult(
  /* The own offers which have been considered for the price calculation. */
  ownOffers: Seq[ApiOffer],
  /* The offers of the competitors which have been considered for the price calculation. */
  competitorOffers: Seq[ApiOffer],
  minPriceBoundary: PriceBoundaryDetails,
  /* The relevant variables used in the formula. */
  variables: Seq[FormulaVariable],
  /* The calculated price recommendation. */
  unitPriceRecommendation: Double,
  /* The unevaluated formula. */
  formula: String,
  maxPriceBoundary: PriceBoundaryDetails,
  /* The ID of the node which calculated the price. */
  nodeId: Int
) extends ApiModel


