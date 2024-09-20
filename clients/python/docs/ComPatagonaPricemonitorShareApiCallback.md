# ComPatagonaPricemonitorShareApiCallback

Defines an HTTP(S) callback that can be registered to respond to system events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The HTTP method to use when making the request. Supported methods are GET and POST. If not provided, the default method is GET. | [optional] 
**name** | **str** | An optional name for the callback, used for identification purposes. | [optional] 
**body_template** | **str** | An optional Mustache template to define the body of the request.&lt;br&gt; The following placeholders are available in the template:&lt;br&gt; - startTime: The time when the monitoring task started (in ISO 8601 format).&lt;br&gt; - contractId: The unique identifier of the contract.&lt;br&gt; Example default template: {\&quot;startTime\&quot;:\&quot;{{startTime}}\&quot;}. | [optional] 
**url** | **str** | The URL to which the callback request will be sent. | 
**headers** | **dict(str, str)** | A map of HTTP headers to be included in the request. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


