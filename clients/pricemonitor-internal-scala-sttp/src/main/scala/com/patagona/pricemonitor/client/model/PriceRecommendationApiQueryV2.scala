/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.5542
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.patagona.pricemonitor.client.model

import com.patagona.pricemonitor.client.core.ApiModel

case class PriceRecommendationApiQueryV2(
  /* This is a placeholder for filter expressions. They are using advanced features and are not covered by openapi. If you need to use filter expressions please contract us. */
  filter: Option[Any] = None,
  pagination: Pagination,
  range: TimeRange,
  sort: Option[PriceRecommendationQuerySortOrderV2] = None
) extends ApiModel

