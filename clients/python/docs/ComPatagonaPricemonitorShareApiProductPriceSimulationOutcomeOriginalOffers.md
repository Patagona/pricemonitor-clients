# ComPatagonaPricemonitorShareApiProductPriceSimulationOutcomeOriginalOffers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_by_total_price** | **int** | The position of the offer on the domain when sorted by total price. | 
**delivery_costs** | **float** | The additional charges for delivering the product to the customer&#39;s location (shipping costs). | 
**max_delivery_time** | **int** | Optional maximum time, in hours, it takes for the product to be delivered to the customer. | [optional] 
**url** | **str** | The direct link to the product page on the domain where this offer can be found. | 
**vendor_domain_id** | **str** | An identifier of the vendor on the domain. Identifiers are available for certain domains only. | [optional] 
**domain** | **str** | The website from which the offer originates. | 
**price** | **float** | The unit price of the offer. | 
**min_delivery_time** | **int** | Optional minimum time, in hours, it takes for the product to be delivered to the customer. | [optional] 
**gtin** | **float** | An optional field for the GTIN / EAN of the product. | [optional] 
**position_by_unit_price** | **int** | The position of the offer on the domain when sorted by unit price. | 
**availability** | **bool** | An optional flag indicating whether the product is currently in stock and available for purchase. | [optional] 
**attributes** | [**list[ComPatagonaPricemonitorShareApiOfferAttribute]**](ComPatagonaPricemonitorShareApiOfferAttribute.md) | A list of additional offer details. | 
**vendor_name** | **str** | The display name of the shop which sells the product. In some cases (e.g. marketplaces) with some additional information about the seller: e.g. Amazon NL - Sold By Amazon NL | 
**retrieval_date** | **datetime** | Optional timestamp based on ISO 8601 format, indicating when this offer was fetched from the domain. | [optional] 
**creation_date** | **datetime** | An optional timestamp in ISO 8601 format indicating when this offer was stored in Omnia 2.0. This is not the timestamp when the offer was fetched from the domain; for that, use retrievalDate. | 
**product_name** | **str** | The name of the product as listed on the domain. | 
**currency** | **str** | The currency in which the price and delivery costs are expressed. Provided values are ISO 4217 currency codes like \&quot;EUR\&quot;. | 
**product_id** | **str** | The internal product ID in Omnia 2.0. | 
**ignored** | **bool** | A flag indicating whether the offer has been blacklisted or not by the Omnia 2.0 filters. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


