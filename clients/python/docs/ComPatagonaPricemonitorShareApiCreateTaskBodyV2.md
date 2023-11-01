# ComPatagonaPricemonitorShareApiCreateTaskBodyV2

Definition of a task to be created.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_type** | **str** | The type of the task to be created. Can be any of [alert, backend.tasks.pricemonitor.offers.monitoring, backend.tasks.pricemonitor.offers.preprocessing, backend.tasks.pricemonitor.callback] | 
**data** | [**object**](.md) |  | [optional] 
**trigger_follow_up_task** | **bool** | optional flag to specify whether or not to trigger the next task. Currently only integrated to trigger callbacks after preprocessing | [optional] 
**include_for_billing** | **bool** | optional flag to specify whether or not to include the task in billing. This is especially useful when manual monitoring is triggered by our admins | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


