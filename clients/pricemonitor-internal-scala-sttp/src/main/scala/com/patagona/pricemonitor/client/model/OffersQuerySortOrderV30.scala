/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.5478
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.patagona.pricemonitor.client.model

import com.patagona.pricemonitor.client.core.ApiModel

case class OffersQuerySortOrderV30(
  metric: OffersQuerySortOrderV30Enums.Metric,
  order: OffersQuerySortOrderV30Enums.Order
) extends ApiModel

object OffersQuerySortOrderV30Enums {

  type Metric = Metric.Value
  type Order = Order.Value
  object Metric extends Enumeration {
    val TotalPrice = Value("TotalPrice")
    val Price = Value("Price")
  }

  object Order extends Enumeration {
    val Asc = Value("asc")
  }

}
