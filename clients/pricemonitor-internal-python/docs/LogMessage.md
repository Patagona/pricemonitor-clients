# LogMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The information that needs to be published | 
**severity** | **str** | Determines how severe is the information. The ENUM values are listed in the descreasing order of their priority.&lt;br&gt; 1. trace - gives more detailed information than any other level in the hierarchy&lt;br&gt; 2. debug - helps developer to debug application and is generally useful for providing support to the application developers&lt;br&gt; 3. info  - gives the progress and chosen state information and is generally useful for end user&lt;br&gt; 4. warn  - use of deprecated APIs, poor use of API, ‘almost’ errors, other runtime situations that are undesirable or unexpected, but not necessarily “wrong”.&lt;br&gt; 5. error - gives information about a serious error which needs to be addressed and may result in unstable state&lt;br&gt; 6. fatal - such errors result in premature termination and you don’t often get this error&lt;br&gt; | 
**component** | **str** | The name of the integrated system. | 
**source** | **str** | Anything within the component that can be considered as an entity to further categorize the log message. | 
**contract_id** | **str** | The ID of the contract | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


