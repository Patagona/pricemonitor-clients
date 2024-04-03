# ComPatagonaPricemonitorShareApiApiOfferV2

Represents an offer for a product on a certain domain.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_costs** | **float** | The additional charges for delivering the product to the customer&#39;s location. | 
**url** | **str** | The direct link to the product page on the domain where this offer can be found. | 
**vendor_domain_id** | **str** | Optional identifier representing the vendor on a certain domain. | [optional] 
**price** | **float** | The current listed unit price of the product. | 
**availability** | **bool** | An optional flag indicating whether the product is currently in stock and available for purchase. | [optional] 
**attributes** | [**list[ComPatagonaPricemonitorShareApiApiOfferAttributeV2]**](ComPatagonaPricemonitorShareApiApiOfferAttributeV2.md) | A list of additional offer details. | 
**vendor_name** | **str** | The display name of the shop which sells the product. | 
**retrieval_date** | **datetime** | Optional timestamp based on ISO 8601 when this offer information was last fetched from the domain. | [optional] 
**id** | **str** | A unique identifier for the offer. It&#39;s crucial that it&#39;s unique across all offers independent of the timestamp. If you don&#39;t have a unique identifier then please use a UUID. | 
**product_name** | **str** | The name of the product as listed on the domain. | 
**currency** | **str** | The currency in which the price and delivery costs are expressed. Allowed values are ISO 4217 currency codes like \&quot;EUR\&quot;. | 
**min_delivery_hours** | **int** | Optional minimum time, in hours, it takes for the product to be delivered to the customer. | [optional] 
**max_delivery_hours** | **int** | Optional maximum time, in hours, it takes for the product to be delivered to the customer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


