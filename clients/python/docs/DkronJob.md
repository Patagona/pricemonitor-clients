# DkronJob

Dkron: A Job represents a scheduled task to execute.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the job. | 
**schedule** | **str** | Cron expression for the job. | 
**timezone** | **str** | Timezone where the job will be executed. By default and when field is set to empty string, the job will run in local time. | [optional] 
**owner** | **str** | Owner of the job | [optional] 
**owner_email** | **str** | Email of the owner | [optional] 
**success_count** | **int** | Number of successful executions | [optional] [readonly] 
**error_count** | **int** | Number of failed executions | [optional] [readonly] 
**last_success** | **datetime** | Last time this job executed successfully | [optional] [readonly] 
**last_error** | **datetime** | Last time this job failed | [optional] [readonly] 
**disabled** | **bool** | Disabled state of the job | [optional] 
**tags** | **dict(str, str)** | Target nodes tags of this job | [optional] 
**retries** | **int** | Number of times to retry a failed job execution | [optional] 
**parent_job** | **str** | The name/id of the job that will trigger the execution of this job | [optional] 
**dependent_jobs** | **list[str]** | Array containing the jobs that depends on this one | [optional] [readonly] 
**processors** | [**object**](.md) |  | [optional] 
**concurrency** | **str** | Concurrency policy for the job allow/forbid | [optional] 
**executor** | **str** | Executor plugin used to run the job | [optional] 
**executor_config** | [**DkronExecutorConfig**](DkronExecutorConfig.md) |  | [optional] 
**status** | **str** | Status of the job | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


