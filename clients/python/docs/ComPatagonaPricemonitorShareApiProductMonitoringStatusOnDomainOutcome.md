# ComPatagonaPricemonitorShareApiProductMonitoringStatusOnDomainOutcome

Describes the result of a monitoring attempt.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | Defines if everything worked as expected. This is the case if: - Offers have been found for the product - The product exists on the domain but is currently not available - The product doesn&#39;t exist on the domain | 
**outcome** | **str** | Describes the outcome of the monitoring attempt. Can be one of: ProductNotFound, ProductNotAvailable, ProductFound, CaptchaFailure, LayoutFailure, RequestFailure, UnknownFailure, ProductSearchFailure, MissingTaskData, AlreadyCompletedTask, InvalidTaskSession, MissingContractId, UnsupportedDomainFailure | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


