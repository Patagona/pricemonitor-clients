# ComPatagonaPricemonitorShareApiPriceSimulationBulkRequestV3

Represents a bulk request to simulate the price calculation for multiple products. The optional parameters can be used for testing/simulating scenarios. If they are not provided, then the current pricing settings will be used.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_builder** | [**object**](.md) |  | [optional] 
**simulation_requests** | [**list[ComPatagonaPricemonitorShareApiProductPriceSimulationRequest]**](ComPatagonaPricemonitorShareApiProductPriceSimulationRequest.md) | List of product price simulation requests. The list may have a maximum 10 requests. | 
**simulation_timestamp** | **datetime** | If provided, then strategies act as if &#x60;simulationTimestamp&#x60; is the current date and time. This can be useful for testing time based strategies. If not provided, it will try to fall back to &#x60;calculationTimestamp&#x60;. If not provided and &#x60;calculationTimestamp&#x60; is also not provided, the current timestamp will be used. | [optional] 
**calculation_timestamp** | **datetime** | Timestamp of the original price calculation. Can be used to reproduce a price calculation. This timestamp is used to retrieve product tags, which we store for each successful price calculation. | [optional] 
**data_time_range** | [**ComPatagonaPricemonitorShareApiOffsetTimeRange**](ComPatagonaPricemonitorShareApiOffsetTimeRange.md) |  | [optional] 
**own_shops** | [**list[ComPatagonaPricemonitorShareApiOwnShopMapping]**](ComPatagonaPricemonitorShareApiOwnShopMapping.md) | Useful for detecting own offers of our customers. This ensures the separation between own and competitor offers. If not provided, the own offers will be detected based on the currently configured own shop mappings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


