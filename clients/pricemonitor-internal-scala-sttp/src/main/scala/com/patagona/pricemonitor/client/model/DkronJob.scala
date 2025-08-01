/**
 * Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts, and more.  This API supports both public endpoints for customer integration and internal endpoints for platform management. All endpoints are authenticated using either Basic Authentication or JWT Bearer tokens.
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.7216
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.patagona.pricemonitor.client.model

import java.time.OffsetDateTime
import com.patagona.pricemonitor.client.core.ApiModel

  /**
   * Dkron: A Job represents a scheduled task to execute.
   */
case class DkronJob(
  /* Name for the job. */
  name: String,
  /* Cron expression for the job. */
  schedule: String,
  /* Timezone where the job will be executed. By default and when field is set to empty string, the job will run in local time. */
  timezone: Option[String] = None,
  /* Owner of the job */
  owner: Option[String] = None,
  /* Email of the owner */
  ownerEmail: Option[String] = None,
  /* Number of successful executions */
  successCount: Option[Int] = None,
  /* Number of failed executions */
  errorCount: Option[Int] = None,
  /* Last time this job executed successfully */
  lastSuccess: Option[OffsetDateTime] = None,
  /* Last time this job failed */
  lastError: Option[OffsetDateTime] = None,
  /* Disabled state of the job */
  disabled: Option[Boolean] = None,
  /* Target nodes tags of this job */
  tags: Option[Map[String, String]] = None,
  /* Number of times to retry a failed job execution */
  retries: Option[Int] = None,
  /* The name/id of the job that will trigger the execution of this job */
  parentJob: Option[String] = None,
  /* Array containing the jobs that depends on this one */
  dependentJobs: Option[Seq[String]] = None,
  processors: Option[Any] = None,
  /* Concurrency policy for the job allow/forbid */
  concurrency: Option[String] = None,
  /* Executor plugin used to run the job */
  executor: Option[String] = None,
  executorConfig: Option[DkronExecutorConfig] = None,
  /* Status of the job */
  status: Option[String] = None
) extends ApiModel


