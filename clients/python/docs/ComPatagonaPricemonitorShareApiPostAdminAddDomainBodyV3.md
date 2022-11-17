# ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3

Request body that contains information about adding a new domain
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | the domain being added. Allowed domain pattern: \&quot;&lt;domain-name&gt;.&lt;top-level-domain&gt;\&quot;. Example:\&quot;google.com\&quot;, \&quot;amazon.co.uk\&quot; (valid), \&quot;_google_com\&quot; (invalid). For omnia custom monitoring, the domain name must be prefixed with \&quot;omnia.custom.spidering.\&quot; | 
**offer_sources** | **list[str]** | sources of offers on this domain. Allowed sources: \&quot;DEFAULT_MONITORING\&quot;, \&quot;CUSTOM_MONITORING\&quot;, \&quot;OMNIA_CUSTOM_SPIDERING\&quot;, \&quot;PUSH_API\&quot;, \&quot;OTHER\&quot; @example domain &#x3D; \&quot;google.de\&quot;, offerSources &#x3D; Set(\&quot;DEFAULT_MONITORING\&quot;) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


