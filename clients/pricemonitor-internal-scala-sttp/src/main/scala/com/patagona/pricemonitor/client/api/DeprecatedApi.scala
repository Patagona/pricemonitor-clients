/**
 * Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts and more.
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.6822
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
package com.patagona.pricemonitor.client.api

import com.patagona.pricemonitor.client.model.GetOffersResponse
import com.patagona.pricemonitor.client.model.GetPriceRecommendationsResponse
import com.patagona.pricemonitor.client.model.GetPricingStrategyHistoryApiResponse
import java.time.OffsetDateTime
import com.patagona.pricemonitor.client.model.TaskIdAndUrl
import com.patagona.pricemonitor.client.core._
import alias._
import sttp.client._
import sttp.model.Method

object DeprecatedApi {

  def apply(baseUrl: String = "https://api.patagona.de")(implicit serializer: SttpSerializer) = new DeprecatedApi(baseUrl)
}

class DeprecatedApi(baseUrl: String)(implicit serializer: SttpSerializer) {

  import Helpers._
  import serializer._

  /**
   * Gets a list of all available domains for monitoring.
   * 
   * Expected answers:
   *   code 200 : Seq[String] (A list of all available domains for monitoring.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   */
  def getAllDomainsV2()(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Seq[String]] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/2/domains")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Seq[String]])
}

  /**
   * Expected answers:
   *   code 200 : GetOffersResponse (No response was specified)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId ID of the contract
   * @param start Start product index for pagination
   * @param limit Number of products for pagination
   * @param startDate Timestamp of start of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {endDate} is given, {startDate} is set to {endDate} - 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'.
   * @param endDate Timestamp of end of time range, formatted as ISO Date (i.e. 2018-04-06T13:46:13Z) in UTC. If this value is omitted and {startDate} is given, {endDate} is set to {startDate} + 48 hours. If both values are omitted, the range is 'NOW - 48 hours to NOW'.
   */
  def getOffers(contractId: String, start: Int, limit: Int, startDate: Option[OffsetDateTime] = None, endDate: Option[OffsetDateTime] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[GetOffersResponse] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/2/v/contracts/${contractId}/result/offers?start=$start&limit=$limit&startDate=$startDate&endDate=$endDate")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[GetOffersResponse])
}

  /**
   * Expected answers:
   *   code 200 : GetPriceRecommendationsResponse (No response was specified)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId ID of the contract
   * @param start Where to start fetching the recommendations
   * @param limit Maximal number of results
   * @param since Timestamp of the oldest results
   */
  def getPriceRecommendations(contractId: String, start: Option[Int] = None, limit: Option[Int] = None, since: Option[OffsetDateTime] = None)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[GetPriceRecommendationsResponse] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/1/${contractId}/products/analysis/pricerecommendations?start=$start&limit=$limit&since=$since")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[GetPriceRecommendationsResponse])
}

  /**
   * Expected answers:
   *   code 200 : GetPricingStrategyHistoryApiResponse (List of metadata of all strategy versions)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId ID of the contract
   */
  def getStrategyHistory(contractId: String)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[GetPricingStrategyHistoryApiResponse] =
{
    var r = basicRequest
      .method(Method.GET, uri"$baseUrl/api/v3/vendor/contracts/${contractId}/settings/repricingstrategy/history")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[GetPricingStrategyHistoryApiResponse])
}

  /**
   * Logs a message.
   * 
   * Expected answers:
   *   code 200 : Any (This is a generated entry and needs to be described.)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   */
  def postLogMessage()(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Any] =
{
    var r = basicRequest
      .method(Method.POST, uri"$baseUrl/api/2/log/messages")
      .contentType("application/json")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r.response(asJson[Any])
}

  /**
   * Warning: Deletes all existing products.         <br/>Note that this will not happen immediately. Instead, you receive the ID of a task that has been created.         <br/>Furthermore you receive an URL which you can use to check if the task was executed successfully.         <br>The csv file must contain following columns:         <ul>           <li>productId - arbitrary string, can be used for the systems product id.</li>           <li>gtin - the GTIN of the product           <li>description - name or short description of the product           <li>referencePrice - arbitrary decimal number, usually the current price or recommended retail price (gross)           <li>minPriceBoundary - decimal number defining the lower price boundary (gross)           <li>maxPriceBoundary - decimal number defining the upper price boundary (gross)           <li>Additional columns are added as product tags. Tags are used for repricing strategies and several other           purpose.         </ul>         <br/>Column separator must be semicolon, the decimal separator must be dot. File encoding must be UTF-8.
   * 
   * Expected answers:
   *   code 200 :  (-)
   *   code 202 : TaskIdAndUrl (Accepted)
   * 
   * Available security schemes:
   *   BasicAuth (http)
   *   BearerAuth (http)
   * 
   * @param contractId ID of the contract
   * @param body CSV file containing the products
   */
  def putCSVProducts(contractId: String, body: String)(implicit basicAuth: Option[BasicCredentials], bearerToken: Option[BearerToken]): ApiRequestT[Unit] =
{
    var r = basicRequest
      .method(Method.PUT, uri"$baseUrl/api/2/v/contracts/${contractId}/products/csv")
      .contentType("text/csv")
      basicAuth.foreach(b => r = r.auth.basic(b.user, b.password))
      bearerToken.foreach(b => r = r.auth.bearer(b.token))
      r=r.body(body)
      r.response(asJson[Unit])
}

}
