# ComPatagonaPricemonitorShareApiProductPriceSimulationOutcome

The result of a single price simulation for a product.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_offers** | [**list[ComPatagonaPricemonitorShareApiApiOffer]**](ComPatagonaPricemonitorShareApiApiOffer.md) | All offers which were initially considered for the price calculation. | 
**result** | [**ComPatagonaPricemonitorShareApiPriceCalculationResult**](ComPatagonaPricemonitorShareApiPriceCalculationResult.md) |  | 
**product_id** | **str** | The internal product ID in Omnia 2.0. | 
**decisive_path** | **list[int]** | The decisive path in the strategy tree:&lt;br&gt; From root node down to the node which calculated the price (shortest path). Can be empty when no price has been calculated or the price calculation fails. | 
**full_path** | **list[int]** | All traversed (processed) nodes in the strategy tree. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


