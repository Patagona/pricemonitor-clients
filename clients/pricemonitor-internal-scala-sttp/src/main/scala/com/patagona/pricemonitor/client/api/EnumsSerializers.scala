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
package com.patagona.pricemonitor.client.api

import com.patagona.pricemonitor.client.model._
import org.json4s._
import scala.reflect.ClassTag

object EnumsSerializers {

  def all: Seq[Serializer[_]] = Seq[Serializer[_]]() :+
    new EnumNameSerializer(AdminContractV2Enums.`Type`) :+
    new EnumNameSerializer(AndFilterEnums.`Type`) :+
    new EnumNameSerializer(BooleanConstantValueProviderEnums.`Type`) :+
    new EnumNameSerializer(BooleanEqualityEnums.`Type`) :+
    new EnumNameSerializer(BooleanValueProviderEnums.`Type`) :+
    new EnumNameSerializer(ConstantFilterEnums.`Type`) :+
    new EnumNameSerializer(DateTimeAfterEnums.`Type`) :+
    new EnumNameSerializer(DateTimeBeforeEnums.`Type`) :+
    new EnumNameSerializer(DateTimeConstantValueProviderEnums.`Type`) :+
    new EnumNameSerializer(DateTimeValueProviderEnums.`Type`) :+
    new EnumNameSerializer(GenericTaskEnums.State) :+
    new EnumNameSerializer(GenericTaskWithUrlEnums.State) :+
    new EnumNameSerializer(GetContractResponseV3Enums.ContractType) :+
    new EnumNameSerializer(LogMessageEnums.Severity) :+
    new EnumNameSerializer(LogMessagesEnums.Version) :+
    new EnumNameSerializer(NotFilterEnums.`Type`) :+
    new EnumNameSerializer(NumberConstantValueProviderEnums.`Type`) :+
    new EnumNameSerializer(NumberEqualityEnums.`Type`) :+
    new EnumNameSerializer(NumberGreaterThanEnums.`Type`) :+
    new EnumNameSerializer(NumberInSequenceEnums.`Type`) :+
    new EnumNameSerializer(NumberLessThanEnums.`Type`) :+
    new EnumNameSerializer(NumberValueProviderEnums.`Type`) :+
    new EnumNameSerializer(OffersQuerySortOrderV30Enums.Metric) :+
    new EnumNameSerializer(OffersQuerySortOrderV30Enums.Order) :+
    new EnumNameSerializer(OrFilterEnums.`Type`) :+
    new EnumNameSerializer(PostProductsRequestEnums.Version) :+
    new EnumNameSerializer(ProductsFilterEnums.`Type`) :+
    new EnumNameSerializer(ProductsFilterEnums.Comparison) :+
    new EnumNameSerializer(PutPluginRegistrationRequestEnums.Version) :+
    new EnumNameSerializer(PutPluginRegistrationRequestAllOfEnums.Version) :+
    new EnumNameSerializer(RegularExpressionEnums.`Type`) :+
    new EnumNameSerializer(SequenceOfNumberConstantValueProviderEnums.`Type`) :+
    new EnumNameSerializer(SequenceOfNumberValueProviderEnums.`Type`) :+
    new EnumNameSerializer(SequenceOfStringConstantValueProviderEnums.`Type`) :+
    new EnumNameSerializer(SequenceOfStringValueProviderEnums.`Type`) :+
    new EnumNameSerializer(StringConstantValueProviderEnums.`Type`) :+
    new EnumNameSerializer(StringEqualityEnums.`Type`) :+
    new EnumNameSerializer(StringInSequenceEnums.`Type`) :+
    new EnumNameSerializer(StringValueProviderEnums.`Type`) :+
    new EnumNameSerializer(UpdateTaskRequestV2Enums.State)

  private class EnumNameSerializer[E <: Enumeration: ClassTag](enum: E)
    extends Serializer[E#Value] {
    import JsonDSL._

    val EnumerationClass: Class[E#Value] = classOf[E#Value]

    def deserialize(implicit format: Formats):
    PartialFunction[(TypeInfo, JValue), E#Value] = {
      case (t @ TypeInfo(EnumerationClass, _), json) if isValid(json) =>
        json match {
          case JString(value) =>
            enum.withName(value)
          case value =>
            throw new MappingException(s"Can't convert $value to $EnumerationClass")
        }
    }

    private[this] def isValid(json: JValue) = json match {
      case JString(value) if enum.values.exists(_.toString == value) => true
      case _ => false
    }

    def serialize(implicit format: Formats): PartialFunction[Any, JValue] = {
      case i: E#Value => i.toString
    }
  }

}