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

import com.patagona.pricemonitor.client.core.ApiModel

  /**
   * Online shops can have different names per domain despite they belong to the same entity. This entity is further called \"vendor\". A vendor shop mapping represents shops which are associated to a vendor.
   */
case class VendorShopMappingV3(
  /* Unique identifier of a vendor */
  id: Double,
  /* Vendor name */
  vendorName: String,
  /* List of shops associated with the specified vendor */
  shops: Set[ShopV3]
) extends ApiModel


