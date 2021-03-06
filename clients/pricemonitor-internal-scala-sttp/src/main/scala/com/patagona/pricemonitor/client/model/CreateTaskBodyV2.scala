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
   * Definition of a task to be created.
   */
case class CreateTaskBodyV2(
  /* The type of the task to be created. Can be any of [alert, backend.tasks.pricemonitor.offers.monitoring, backend.tasks.pricemonitor.offers.preprocessing, backend.tasks.pricemonitor.callback] */
  taskType: String,
  data: Option[Any] = None
) extends ApiModel


