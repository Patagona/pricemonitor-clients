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

import java.time.OffsetDateTime
import com.patagona.pricemonitor.client.core.ApiModel

  /**
   * A basic task type. Additional fields can be contained depending on specific task type.
   */
case class GenericTask(
  /* The creation date of this task */
  creationDate: OffsetDateTime,
  /* The timestamp of when processing of this task was started */
  startDate: Option[OffsetDateTime] = None,
  /* The timestamp of when processing of this task finished */
  finishDate: Option[OffsetDateTime] = None,
  /* The current processing state of this task */
  state: GenericTaskEnums.State,
  /* Schemaless. If any errors occured during processing, these will be contained here. */
  failures: Option[Seq[Any]] = None,
  /* The unique ID of this task */
  taskId: String,
  /* The parents unique taskId, if any parent exists */
  parentId: Option[String] = None,
  /* The identifier string for the type of task */
  taskType: String,
  /* Schemaless. Contains the payload of the task given during task creation. */
  data: Option[Any] = None,
  /* Schemaless. Contains the processing result for this task. Type is dependent on task type. */
  result: Option[Any] = None,
  /* If any error occured the error code for this error will be contained here. */
  failureCode: Option[String] = None
) extends ApiModel

object GenericTaskEnums {

  type State = State.Value
  object State extends Enumeration {
    val Pending = Value("pending")
    val Executing = Value("executing")
    val Succeeded = Value("succeeded")
    val Failed = Value("failed")
  }

}
