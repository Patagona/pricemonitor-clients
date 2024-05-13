# ComPatagonaPricemonitorShareApiPostMonitoringScheduleRequestV3

A request body containing monitoring schedule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_query** | [**ComPatagonaPricemonitorShareApiQuery**](ComPatagonaPricemonitorShareApiQuery.md) |  | [optional] 
**quota** | **float** | Defines how many products should get monitored. Default to 1.0 which means that all products are monitored. Allowed values: 0.0 &lt; quota &lt;&#x3D; 1.0 | 
**domain_query** | [**ComPatagonaPricemonitorShareApiQuery**](ComPatagonaPricemonitorShareApiQuery.md) |  | [optional] 
**unfulfilled_only** | **bool** | When it&#39;s set to true, then the monitoring considers only products on domains where no offers are found within 24h. Default false. | 
**schedule** | **str** | Only valid CRON expressions are allowed. Expression such as \&quot;@every 5s\&quot; is not allowed. Cron expressions that go from seconds to day of week in the following order: - Seconds (Allowed value: 0-59 and Allowed Special Characters: * , - /) - Minutes (Allowed value: 0-59 and Allowed Special Characters: * , - /) - Hour Of Day (Allowed value: 0-23 and Allowed Special Characters: * , - /) - Day Of Month (Allowed value: 1-31 and Allowed Special Characters: * ? , - /) - Month (Allowed value: 1-12 and Allowed Special Characters: * , -) - Day Of Week (Allowed value: 0-7 and Allowed Special Characters: * ? , - / ). Please note that 0 represents Sunday and 7 represents Saturday. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


