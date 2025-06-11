# BooleanBulkApiResponse

Response for bulk operations, containing one result per item in the request body (order preserved). Each result object contains either:   - `data: true` if the operation succeeded,   - or `errors`: a list of `ApiError` objects if it failed. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[BooleanBulkApiResponseData]**](BooleanBulkApiResponseData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


