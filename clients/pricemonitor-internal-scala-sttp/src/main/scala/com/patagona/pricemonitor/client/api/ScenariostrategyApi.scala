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
package com.patagona.pricemonitor.client.api

import com.patagona.pricemonitor.client.model.ApiErrorResponse
import com.patagona.pricemonitor.client.model.PostScenarioStrategyRequest
import com.patagona.pricemonitor.client.model.PostScenarioStrategyResponseApiResponse
import com.patagona.pricemonitor.client.model.ScenarioStrategyMetadataResponseApiResponse
import com.patagona.pricemonitor.client.model.ScenarioStrategyResponse
import com.patagona.pricemonitor.client.core._
import alias._
import sttp.client._
import sttp.model.Method

object ScenariostrategyApi {

  def apply(baseUrl: String = "https://api.patagona.de")(implicit serializer: SttpSerializer) = new ScenariostrategyApi(baseUrl)
}

class ScenariostrategyApi(baseUrl: String)(implicit serializer: SttpSerializer) {

  import Helpers._
  import serializer._

  /**
   * Expected answers:
   *   code 200 : PostScenarioStrategyResponseApiResponse (A new scenario strategy was added)
   *   code 400 : ApiErrorResponse (Strategy must be valid and consistent with the schema version. Required fields need to be filled.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId ID of the contract
   * @param postScenarioStrategyRequest The scenario strategy to be stored. Including the necessary metadata.
   */
  def addPricingStrategyScenario(contractId: String, postScenarioStrategyRequest: Option[PostScenarioStrategyRequest] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[PostScenarioStrategyResponseApiResponse] =
{
    var r = basicRequest
      .method(Method.POST, uri"$baseUrl/api/v3/vendor/contracts/${contractId}/settings/pricingstrategies/scenarios")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r=r.body(postScenarioStrategyRequest)
      r.response(asJson[PostScenarioStrategyResponseApiResponse])
}

  /**
   * Get a list of all scenario strategy metadata for a contract.
   * 
   * Expected answers:
   *   code 200 : Seq[ScenarioStrategyMetadataResponseApiResponse] (List of all scenario strategy metadata)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId ID of the contract
   */
  def getAllScenariosMetadata(contractId: String)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Seq[ScenarioStrategyMetadataResponseApiResponse]] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/v3/vendor/contracts/${contractId}/settings/pricingstrategies/scenarios")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Seq[ScenarioStrategyMetadataResponseApiResponse]])
}

  /**
   * Get a scenario strategy with the provided scenario id.
   * 
   * Expected answers:
   *   code 200 : ScenarioStrategyResponse (A scenario strategy)
   *   code 404 : ApiErrorResponse (Scenario strategy with the provided Id was not found.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId ID of the contract
   * @param scenarioId ID of the required scenario strategy
   */
  def getScenarioById(contractId: String, scenarioId: Int)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[ScenarioStrategyResponse] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/v3/vendor/contracts/${contractId}/settings/pricingstrategies/scenarios/${scenarioId}")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[ScenarioStrategyResponse])
}

}

