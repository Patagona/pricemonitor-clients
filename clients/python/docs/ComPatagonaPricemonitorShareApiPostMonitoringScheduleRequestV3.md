# ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3

A request body containing monitoring schedule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quota** | **float** | Defines how many products should get monitored. Default to 1.0 which means that all products are monitored. Allowed values: 0.0 &lt; quota &lt;&#x3D; 1.0 | 
**unfulfilled_only** | **bool** | When it&#39;s set to true, then the monitoring considers only products on domains where no offers are found within 24h. Default false. | 
**product_query** | [**ComPatagonaPricemonitorShareApiQuery**](ComPatagonaPricemonitorShareApiQuery.md) |  | [optional] 
**schedule** | **str** | Only valid CRON expressions are allowed. See Cron spec [[https://www.alonsodomin.me/cron4s/userguide/index.html]] | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

