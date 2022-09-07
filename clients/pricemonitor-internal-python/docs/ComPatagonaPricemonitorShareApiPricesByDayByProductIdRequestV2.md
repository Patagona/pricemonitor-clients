# ComPatagonaPricemonitorShareApiPricesByDayByProductIdRequestV2

A request for all known prices for a given day & product ID. Provides the option to filter the results using the `offerSelectors`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **datetime** | The day for which to return the prices in ISO 8601 | 
**offers** | [**list[ComPatagonaPricemonitorShareApiOfferSelector]**](ComPatagonaPricemonitorShareApiOfferSelector.md) | A list of &#x60;OfferSelector&#x60;s that allows filtering down the results. The selectors are combined using an OR operation. The list must contain at least one element. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


