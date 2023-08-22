# ComPatagonaPricemonitorShareApiPostProductOfferRequest

Represents a single request to post offers for a snapshot. A snapshot is a unique combination of productId, creationDate, and domain.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Patagona&#39;s internal product id. | 
**creation_date** | **datetime** | ISO 8601 timestamp when the offers have been gathered. This timestamp needs to be more recent compared to already existing offers. Otherwise, the offers will be rejected. | 
**domain** | **str** | Origin of the offers. | 
**offers** | [**list[ComPatagonaPricemonitorShareApiApiOfferV2]**](ComPatagonaPricemonitorShareApiApiOfferV2.md) | Non-empty list of offers. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


