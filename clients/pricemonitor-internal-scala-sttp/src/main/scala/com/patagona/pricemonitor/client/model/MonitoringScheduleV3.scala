/**
 * Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts and more.
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.6776
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.patagona.pricemonitor.client.model

import com.patagona.pricemonitor.client.core.ApiModel

  /**
   * MonitoringScheduleV3 represents monitoring schedule that can be adjustable by the price-monitor customers.
   */
case class MonitoringScheduleV3(
  productQuery: Option[Query] = None,
  /* Defines how many products should get monitored. Default to 1.0 which means that all products are monitored. Allowed values: 0.0 < quota <= 1.0 */
  quota: Double,
  domainQuery: Option[Query] = None,
  /* When it's set to true, then the monitoring considers only products on domains where no offers are found within 24h. Default false. */
  unfulfilledOnly: Boolean,
  /* Id that uniquely identifies a monitoring schedule. */
  id: Double,
  /* Only valid CRON expressions are allowed. See Cron spec [[https://www.alonsodomin.me/cron4s/userguide/index.html]]. */
  schedule: String,
  /* Internal job id used by the scheduler. */
  schedulerJobId: String
) extends ApiModel


