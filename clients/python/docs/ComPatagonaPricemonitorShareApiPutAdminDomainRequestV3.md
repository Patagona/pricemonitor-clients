# ComPatagonaPricemonitorShareApiPutAdminDomainRequestV3

Request body that contains information about updating an existing domain with new offerSources or adding a new domain
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | display name for the domain in the UI. (Must be unique and non-empty) | 
**offer_sources** | **list[str]** | sources of offers on this domain. Allowed sources: \&quot;DEFAULT_MONITORING\&quot;, \&quot;CUSTOM_MONITORING\&quot;, \&quot;OMNIA_CUSTOM_SPIDERING\&quot;, \&quot;PUSH_API\&quot;, \&quot;OTHER\&quot; @example name &#x3D; \&quot;google\&quot;, offerSources &#x3D; Set(\&quot;DEFAULT_MONITORING\&quot;) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


