# ComPatagonaPricemonitorShareApiPriceSimulationBulkResponseV3

Represents a bulk response with simulated price recommendations for multiple products.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_builder** | [**object**](.md) |  | 
**calculation_timestamp** | **datetime** | The timestamp for which the price calculation has been simulated. If specified in the request this will be &#x60;simulationTimestamp&#x60;. | 
**simulation_results** | [**list[ComPatagonaPricemonitorShareApiProductPriceSimulationOutcome]**](ComPatagonaPricemonitorShareApiProductPriceSimulationOutcome.md) | The simulation results. All results are in order with respect to the input list of product simulation requests. | 
**data_time_range** | [**ComPatagonaPricemonitorShareApiOffsetTimeRange**](ComPatagonaPricemonitorShareApiOffsetTimeRange.md) |  | 
**own_shops** | [**list[ComPatagonaPricemonitorShareApiOwnShopMapping]**](ComPatagonaPricemonitorShareApiOwnShopMapping.md) | The considered own shops. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


