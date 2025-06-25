# LogMessage

Individual log message with severity level and contextual information
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The actual log message content to be published | 
**severity** | **str** | Log message severity level, ordered by priority (highest to lowest):  - **fatal**: Critical errors causing system termination - **error**: Serious errors requiring immediate attention - **warn**: Deprecated APIs, poor API usage, or unexpected situations - **info**: General progress and state information for end users - **debug**: Detailed information for application developers and support - **trace**: Most detailed information for deep debugging  | 
**component** | **str** | Name of the integrated system or application component generating the log | 
**source** | **str** | Specific entity or source within the component for additional categorization | 
**contract_id** | **str** | The contract identifier associated with this log message | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


