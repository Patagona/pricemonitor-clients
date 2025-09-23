# GenericTask

A basic task type that represents the stored task document. Additional fields can be contained depending on specific task type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **datetime** | ISO 8601 timestamp (UTC) when the task was created. | 
**start_date** | **datetime** | ISO 8601 timestamp (UTC) when processing of this task started. | [optional] 
**finish_date** | **datetime** | ISO 8601 timestamp (UTC) when processing of this task finished. | [optional] 
**state** | **str** | The current processing state of this task | 
**failures** | **list[object]** | Schemaless. If any errors occured during processing, these will be contained here. Only store a preview (up to 1,000 entries) to prevent overloading the database. | [optional] 
**task_id** | **str** | The unique ID of this task | 
**parent_id** | **str** | The parents unique taskId, if any parent exists | [optional] 
**task_type** | **str** | The identifier string for the type of task | 
**data** | [**object**](.md) | Schemaless. Contains the payload of the task given during task creation. | [optional] 
**result** | [**object**](.md) | Schemaless. Contains the processing result for this task. Type is dependent on task type. Avoid persisting excessively large results; prefer concise summaries. | [optional] 
**failure_code** | **str** | If any error occured the error code for this error will be contained here. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


