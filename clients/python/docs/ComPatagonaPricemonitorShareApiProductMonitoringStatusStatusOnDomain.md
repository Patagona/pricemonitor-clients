# ComPatagonaPricemonitorShareApiProductMonitoringStatusStatusOnDomain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain which gets monitored. | 
**started_at** | **datetime** | The last time pricemonitor tried to monitor the product on the given domain. If this doesn&#39;t exist it mean&#39;s that pricemonitor haven&#39;t tried to monitor this product on the domain yet. One reason could be that the product is very new or the domain has just recently been added to the contract. | [optional] 
**completed_at** | **datetime** | The last time pricemonitor completed monitoring the product on the given domain. | [optional] 
**outcome** | [**ComPatagonaPricemonitorShareApiProductMonitoringStatusOnDomainOutcome**](ComPatagonaPricemonitorShareApiProductMonitoringStatusOnDomainOutcome.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


