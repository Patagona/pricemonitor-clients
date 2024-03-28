# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The types are fixed and defined in the scheduler code.  | 
**id** | **str** | The internal job id. **Not** needed when creating a job.  | [optional] 
**timezone** | **str** | See [tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).  | 
**contract_id** | **str** | Each job **must** be attached to a specific contract SID.  | [optional] 
**schedule** | **str** | See [CRON spec](https://www.alonsodomin.me/cron4s/userguide/index.html)  Only valid CRON expressions are allowed. Extra expressions from Dkron, e.g. \&quot;@every 5s\&quot;, are not allowed.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


