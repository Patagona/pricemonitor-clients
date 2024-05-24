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
**schedule** | **str** | Only valid CRON expressions are allowed. Expressions such as \&quot;@every 5s\&quot; are not allowed. Cron expressions that go from seconds to day of week in the following order:&lt;br/&gt; &lt;ul&gt; &lt;li&gt;Seconds (Allowed value: 0-59 and Allowed Special Characters: * , - /).&lt;/li&gt; &lt;li&gt;Minutes (Allowed value: 0-59 and Allowed Special Characters: * , - /).&lt;/li&gt; &lt;li&gt;Hour Of Day (Allowed value: 0-23 and Allowed Special Characters: * , - /).&lt;/li&gt; &lt;li&gt;Day Of Month (Allowed value: 1-31 and Allowed Special Characters: * ? , - /).&lt;/li&gt; &lt;li&gt;Month (Allowed value: 1-12 and Allowed Special Characters: * , -).&lt;/li&gt; &lt;li&gt;Day Of Week (Allowed value: 0-7 and Allowed Special Characters: * ? , - / ).&lt;/li&gt; &lt;/ul&gt; Please note that 0 and 7 represent Sunday and 6 represents Saturday. | 
**scheduler_job_id** | **str** | Internal job id used by the scheduler. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


