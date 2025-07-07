# ComPatagonaPricemonitorShareApiPostProductOfferRequest

Represents a single request to post offers for a snapshot. A snapshot is a unique combination of productId, creationDate, and domain. It must contain the complete set of offers for that product and domain at the given time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Omnia&#39;s internal product id. | 
**creation_date** | **datetime** | ISO 8601 timestamp when the offers have been gathered. Must be more recent than existing snapshots for the same product and domain, otherwise the request will be rejected. | 
**domain** | **str** | Domain from which the offers originate (e.g., \&quot;example.com\&quot;). | 
**offers** | [**list[ComPatagonaPricemonitorShareApiApiOfferV2]**](ComPatagonaPricemonitorShareApiApiOfferV2.md) | Non-empty list of offers. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


