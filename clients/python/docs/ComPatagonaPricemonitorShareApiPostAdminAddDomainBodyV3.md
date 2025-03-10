# ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3

Request body that contains information about adding a new domain
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | the domain being added. (Must be unique and non-empty) Allowed domain pattern: \&quot;&amp;lt;domain-name&amp;gt;.&amp;lt;top-level-domain&amp;gt;\&quot;. Example:\&quot;google.com\&quot;, \&quot;amazon.co.uk\&quot; (valid), \&quot;_google_com\&quot; (invalid). For omnia custom monitoring, the domain name must be prefixed with \&quot;omnia.custom.spidering.\&quot; | 
**name** | **str** | display name for the domain in the UI. (Must be unique and non-empty) | 
**offer_sources** | **list[str]** | sources of offers on this domain. (Must be non-empty) Allowed sources: \&quot;DEFAULT_MONITORING\&quot;, \&quot;CUSTOM_MONITORING\&quot;, \&quot;OMNIA_CUSTOM_SPIDERING\&quot;, \&quot;PUSH_API\&quot;, \&quot;OTHER\&quot; @example domain &#x3D; \&quot;google.de\&quot;, offerSources &#x3D; Set(\&quot;DEFAULT_MONITORING\&quot;) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


