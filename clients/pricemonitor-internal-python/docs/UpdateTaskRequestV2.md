# UpdateTaskRequestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **datetime** | The creation date of this task | 
**start_date** | **datetime** | The timestamp of when processing of this task was started | [optional] 
**finish_date** | **datetime** | The timestamp of when processing of this task finished | [optional] 
**state** | **str** | The current processing state of this task | 
**failures** | **list[object]** | Schemaless. If any errors occured during processing, these will be contained here. | [optional] 
**task_id** | **str** | The unique ID of this task | 
**parent_id** | **str** | The parents unique taskId, if any parent exists | [optional] 
**task_type** | **str** | The identifier string for the type of task | 
**data** | [**object**](.md) | Schemaless. Contains the payload of the task given during task creation. | [optional] 
**result** | [**object**](.md) | Schemaless. Contains the processing result for this task. Type is dependent on task type. | [optional] 
**failure_code** | **str** | If any error occured the error code for this error will be contained here. | [optional] 
**contract_id** | **str** | The contract SID to update the task for | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


