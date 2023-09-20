# ComPatagonaPricemonitorShareApiMonitoringScheduleV3

MonitoringScheduleV3 represents monitoring schedule that can be adjustable by the price-monitor customers.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_query** | [**ComPatagonaPricemonitorShareApiQuery**](ComPatagonaPricemonitorShareApiQuery.md) |  | [optional] 
**quota** | **float** | Defines how many products should get monitored. Default to 1.0 which means that all products are monitored. Allowed values: 0.0 &lt; quota &lt;&#x3D; 1.0 | 
**domain_query** | [**ComPatagonaPricemonitorShareApiQuery**](ComPatagonaPricemonitorShareApiQuery.md) |  | [optional] 
**unfulfilled_only** | **bool** | When it&#39;s set to true, then the monitoring considers only products on domains where no offers are found within 24h. Default false. | 
**id** | **float** | Id that uniquely identifies a monitoring schedule. | 
**schedule** | **str** | Only valid CRON expressions are allowed. See Cron spec [[https://www.alonsodomin.me/cron4s/userguide/index.html]]. | 
**scheduler_job_id** | **str** | Internal job id used by the scheduler. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


