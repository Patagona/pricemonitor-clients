# DkronExecutorConfig

Dkron: Executor plugin parameters
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Request method in uppercase | [optional] 
**url** | **str** | Request url | [optional] 
**headers** | **str** | Json string, such as \&quot;[\&quot;Content-Type: application/json\&quot;]\&quot; | [optional] 
**body** | **str** | POST body | [optional] 
**timeout** | **str** | Request timeout, unit seconds | [optional] 
**expect_code** | **str** | Expect response code, such as 200,206 | [optional] 
**expect_body** | **str** | Expect response body, support regexp, such as /success/ | [optional] 
**debug** | **str** | Debug option, will log everything when this option is not empty | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


