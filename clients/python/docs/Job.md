# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**JobType**](JobType.md) |  | 
**id** | **str** | The internal job id. **Not** needed when creating a job.  | [optional] 
**timezone** | **str** | See [tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).  | 
**contract_id** | **str** | Each job **must** be attached to a specific contract SID.  | [optional] 
**schedule** | **str** | Only valid CRON expressions are allowed. Extra expressions from Dkron, e.g. \&quot;@every 5s\&quot;, are not allowed. Cron expressions that go from seconds to day of week in the following order: - Seconds (Allowed value: 0-59) - Minutes (Allowed value: 0-59) - Hour Of Day (Allowed value: 0-23) - Day Of Month (Allowed value: 1-31) - Month (Allowed value: 1-12) - Day Of Week (Allowed value: 0-7). Please note that 0 and 7 represent Sunday and 6 represents Saturday.   | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


