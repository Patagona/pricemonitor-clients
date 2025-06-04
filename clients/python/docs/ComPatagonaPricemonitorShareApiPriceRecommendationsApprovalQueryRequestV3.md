# ComPatagonaPricemonitorShareApiPriceRecommendationsApprovalQueryRequestV3

Represents a paginated query for price recommendation approvals. <br> If no filter is provided, the response will contain all available data, paginated according to the `pagination` parameter. <br> <br> Notes: <br> - At maximum it's allowed to query 1,000 records (pagination limit). - If `status` is not provided, all statuses are included in the results.<br> - If `latestOnly` is true, only the most recent approval per product is returned. If false, all matching records are returned.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_filter** | [**ComPatagonaPricemonitorShareApiOneOfProductsQuery**](ComPatagonaPricemonitorShareApiOneOfProductsQuery.md) |  | [optional] 
**latest_only** | **bool** | Boolean indicating whether to return only the most recent approval per product. &lt;br&gt; If true, only the most recent record per product within the time range is returned. &lt;br&gt; If false, all records within the time range are returned. | 
**range** | [**ComPatagonaPricemonitorShareApiOffsetTimeRange**](ComPatagonaPricemonitorShareApiOffsetTimeRange.md) |  | 
**status** | **list[str]** | Optional set of statuses to filter the approvals by their current status. &lt;br&gt; If omitted, all statuses are included. | [optional] 
**pagination** | [**ComPatagonaPricemonitorShareApiPagination**](ComPatagonaPricemonitorShareApiPagination.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


