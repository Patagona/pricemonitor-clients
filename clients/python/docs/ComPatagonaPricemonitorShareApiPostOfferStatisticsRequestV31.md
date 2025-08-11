# ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31

Represents a paginated query with an optional product filter and a specified time range. <br> If no filter is provided, the response will contain all available data, paginated according to the `pagination` parameter. <br> <br> Notes: <br> - At maximum it's allowed to query 10,000 records (pagination limit). <br> - The maximum time span between the start and end should not exceed 48 hours (timerange limit).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**ComPatagonaPricemonitorShareApiPagination**](ComPatagonaPricemonitorShareApiPagination.md) |  | 
**range** | [**ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31Range**](ComPatagonaPricemonitorShareApiPostOfferStatisticsRequestV31Range.md) |  | 
**filter** | [**ComPatagonaPricemonitorShareApiOneOfProductsQuery**](ComPatagonaPricemonitorShareApiOneOfProductsQuery.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


