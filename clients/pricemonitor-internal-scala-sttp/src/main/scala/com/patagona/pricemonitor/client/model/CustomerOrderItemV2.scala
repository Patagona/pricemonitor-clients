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

  /**
   * A ordered item
   */
case class CustomerOrderItemV2(
  /* Id of the item in the customer's system. It is expected to be the customerProductId. It should be guaranteed that the itemId can be always assigned to only one product or variant. */
  itemId: String,
  /* Unit price of an item */
  unitPrice: Double,
  /* How often the item was purchased */
  quantity: Int,
  /* Tax percentage applied on unit price, e.g. 20 for 20% tax */
  taxPercentage: Double
) extends ApiModel

