# ComPatagonaPricemonitorShareApiPriceSimulationBulkRequestV3

Represents a bulk request to simulate the price calculation for multiple products. The optional parameters can be used for testing/simulating scenarios. If they are not provided, then the current pricing settings will be used.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_builder** | [**object**](.md) |  | [optional] 
**simulation_requests** | [**list[ComPatagonaPricemonitorShareApiProductPriceSimulationRequest]**](ComPatagonaPricemonitorShareApiProductPriceSimulationRequest.md) | List of product price simulation requests. | 
**calculation_timestamp** | **datetime** | If provided, then the price calculation will be simulated with the specified timestamp. This can be useful for simulating time-based strategies. If not provided, the current timestamp will be used. | [optional] 
**data_time_range** | [**ComPatagonaPricemonitorShareApiOffsetTimeRange**](ComPatagonaPricemonitorShareApiOffsetTimeRange.md) |  | [optional] 
**own_shops** | [**list[ComPatagonaPricemonitorShareApiOwnShopMapping]**](ComPatagonaPricemonitorShareApiOwnShopMapping.md) | Useful for detecting own offers of our customers. This ensures the separation between own and competitor offers. If not provided, the own offers will be detected based on the currently configured own shop mappings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


