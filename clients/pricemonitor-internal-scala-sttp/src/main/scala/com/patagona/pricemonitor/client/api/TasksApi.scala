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
package com.patagona.pricemonitor.client.api

import com.patagona.pricemonitor.client.model.CreateTaskBodyV2
import com.patagona.pricemonitor.client.model.GenericTask
import com.patagona.pricemonitor.client.model.GenericTaskWithUrl
import java.time.OffsetDateTime
import com.patagona.pricemonitor.client.model.TaskWithContractResourceApiResponse
import com.patagona.pricemonitor.client.core._
import alias._
import sttp.client._
import sttp.model.Method

object TasksApi {

  def apply(baseUrl: String = "https://api.patagona.de")(implicit serializer: SttpSerializer) = new TasksApi(baseUrl)
}

class TasksApi(baseUrl: String)(implicit serializer: SttpSerializer) {

  import Helpers._
  import serializer._

  /**
   * Create a new task
   * 
   * Expected answers:
   *   code 200 : Any (This is a generated entry and needs to be described.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param createTaskBodyV2 Create a new task
   */
  def createTask(contractId: String, createTaskBodyV2: Option[CreateTaskBodyV2] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Any] =
{
    var r = basicRequest
      .method(Method.POST, uri"$baseUrl/api/1/${contractId}/tasks")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r=r.body(createTaskBodyV2)
      r.response(asJson[Any])
}

  /**
   * Creates a new task for a manufacturer contract
   * 
   * Expected answers:
   *   code 200 : GenericTaskWithUrl (The new task was successfully created)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param createTaskBodyV2 This is a generated entry and needs to be described.
   */
  def createTaskManufacturerV2(contractId: String, createTaskBodyV2: Option[CreateTaskBodyV2] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[GenericTaskWithUrl] =
{
    var r = basicRequest
      .method(Method.POST, uri"$baseUrl/api/2/m/contracts/${contractId}/tasks")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r=r.body(createTaskBodyV2)
      r.response(asJson[GenericTaskWithUrl])
}

  /**
   * Creates a new task for a vendor contract.
   * 
   * Expected answers:
   *   code 200 : Any (Task has been created successfully)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param createTaskBodyV2 Create a new task
   */
  def createTaskVendorV2(contractId: String, createTaskBodyV2: Option[CreateTaskBodyV2] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Any] =
{
    var r = basicRequest
      .method(Method.POST, uri"$baseUrl/api/2/v/contracts/${contractId}/tasks")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r=r.body(createTaskBodyV2)
      r.response(asJson[Any])
}

  /**
   * Get a task by id
   * 
   * Expected answers:
   *   code 200 : Any (This is a generated entry and needs to be described.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param taskId 
   */
  def getTask(contractId: String, taskId: String)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Any] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/1/${contractId}/tasks/${taskId}")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Any])
}

  /**
   * Expected answers:
   *   code 200 : Any (The payload data of the requested task is returned)
   *   code 404 :  (The task with the given ID could not be found)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param taskId 
   */
  def getTaskDataManufacturerV2(contractId: String, taskId: String)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Any] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/2/m/contracts/${contractId}/tasks/${taskId}/data")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Any])
}

  /**
   * Expected answers:
   *   code 200 : Any (This is a generated entry and needs to be described.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param taskId 
   */
  def getTaskDataVendorV2(contractId: String, taskId: String)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Any] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/2/v/contracts/${contractId}/tasks/${taskId}/data")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Any])
}

  /**
   * Get the task with the specified id.
   * 
   * Expected answers:
   *   code 200 : GenericTask (The task was found and is returned)
   *   code 404 :  (No task with given taskId was found)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param taskId 
   */
  def getTaskManufacturerV2(contractId: String, taskId: String)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[GenericTask] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/2/m/contracts/${contractId}/tasks/${taskId}")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[GenericTask])
}

  /**
   * Gets the state of a task.
   * 
   * Expected answers:
   *   code 200 : Any (This is a generated entry and needs to be described.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param taskId 
   */
  def getTaskState(contractId: String, taskId: String)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Any] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/1/${contractId}/tasks/${taskId}/state")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Any])
}

  /**
   * Finds a task with the specified id for the given contract.
   * 
   * Expected answers:
   *   code 200 : TaskWithContractResourceApiResponse (No response was specified)
   *   code 404 :  (Not found)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param taskId Id of the task
   */
  def getTaskVendorV2(contractId: String, taskId: String)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[TaskWithContractResourceApiResponse] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/2/v/contracts/${contractId}/tasks/${taskId}")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[TaskWithContractResourceApiResponse])
}

  /**
   * Expected answers:
   *   code 200 : Any (This is a generated entry and needs to be described.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param tasks 
   * @param attributes 
   * @param limit 
   * @param taskType 
   */
  def getTasks(contractId: String, tasks: String, attributes: String, limit: Int, taskType: Option[String] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Any] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/1/${contractId}/tasks?tasks=$tasks&attributes=$attributes&limit=$limit&taskType=$taskType")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Any])
}

  /**
   * Returns a list of task objects for the given contract
   * 
   * Expected answers:
   *   code 200 : Seq[GenericTask] (The list of tasks for the given contract)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param taskTypeFilter A list of task types to filter for
   * @param taskState A list of task states to filter for
   * @param limit The maximum number of tasks returned
   * @param includeFailures Include failed tasks
   * @param taskIdsFilter Comma separated list of task IDs to filter for
   * @param minCreationDate Ignore all tasks created earlier than this date (ISO 8601)
   * @param maxCreationDate Ignore all tasks created later than this date (ISO 8601)
   */
  def getTasksManufacturerV2(contractId: String, taskTypeFilter: Seq[String], taskState: Seq[String], limit: Int, includeFailures: Boolean, taskIdsFilter: Option[String] = None, minCreationDate: Option[OffsetDateTime] = None, maxCreationDate: Option[OffsetDateTime] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Seq[GenericTask]] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/2/m/contracts/${contractId}/tasks?taskIdsFilter=$taskIdsFilter&taskTypeFilter=$taskTypeFilter&taskState=$taskState&minCreationDate=$minCreationDate&maxCreationDate=$maxCreationDate&limit=$limit&includeFailures=$includeFailures")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Seq[GenericTask]])
}

  /**
   * The search can be narrowed down by providing the IDs of the tasks, separated by comma
   * 
   * Expected answers:
   *   code 200 : Set[TaskWithContractResourceApiResponse] (No response was specified)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param taskIdsFilter Ids of the tasks
   * @param taskTypeFilter Desired task type
   * @param limit Maximal number of results
   * @param includeFailures Flag whether to include failures in the response
   * @param taskState Comma separated task state filter
   * @param minCreationDate Oldest returned creation date in UTC
   * @param maxCreationDate Newest returned creation date in UTC
   */
  def getTasksVendorV2(contractId: String, taskIdsFilter: Option[String] = None, taskTypeFilter: Option[String] = None, limit: Option[Int] = None, includeFailures: Option[Boolean] = None, taskState: Option[String] = None, minCreationDate: Option[OffsetDateTime] = None, maxCreationDate: Option[OffsetDateTime] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Set[TaskWithContractResourceApiResponse]] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/2/v/contracts/${contractId}/tasks?taskIdsFilter=$taskIdsFilter&taskTypeFilter=$taskTypeFilter&limit=$limit&includeFailures=$includeFailures&taskState=$taskState&minCreationDate=$minCreationDate&maxCreationDate=$maxCreationDate")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Set[TaskWithContractResourceApiResponse]])
}

  /**
   * Update the task with the specified id for the given contract.
   * 
   * Expected answers:
   *   code 200 : Any (This is a generated entry and needs to be described.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId Unique identifier of the contract
   * @param taskId 
   * @param body This is a generated entry and needs to be described.
   */
  def updateTaskVendorV2(contractId: String, taskId: String, body: Option[Any] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Any] =
{
    var r = basicRequest
      .method(Method.PUT, uri"$baseUrl/api/2/v/contracts/${contractId}/tasks/${taskId}")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r=r.body(body)
      r.response(asJson[Any])
}

}

