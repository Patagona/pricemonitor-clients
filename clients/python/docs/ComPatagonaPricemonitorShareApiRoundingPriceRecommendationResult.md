# ComPatagonaPricemonitorShareApiRoundingPriceRecommendationResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**own_offers** | [**ComPatagonaPricemonitorShareApiApiOffer**](ComPatagonaPricemonitorShareApiApiOffer.md) |  | [optional] 
**competitor_offers** | [**ComPatagonaPricemonitorShareApiApiOffer**](ComPatagonaPricemonitorShareApiApiOffer.md) |  | [optional] 
**price_steps** | **list[float]** |  | 
**step_selection** | **str** |  | 
**min_price_boundary** | [**ComPatagonaPricemonitorShareApiPriceBoundaryDetails**](ComPatagonaPricemonitorShareApiPriceBoundaryDetails.md) |  | 
**original_price_recommendation** | [**ComPatagonaPricemonitorShareApiPriceCalculationResult**](ComPatagonaPricemonitorShareApiPriceCalculationResult.md) |  | 
**unit_price_recommendation** | **float** | The calculated price recommendation. | 
**max_price_boundary** | [**ComPatagonaPricemonitorShareApiPriceBoundaryDetails**](ComPatagonaPricemonitorShareApiPriceBoundaryDetails.md) |  | 
**adjust_to_next_reachable_price_step** | **bool** |  | [optional] 
**node_id** | **float** | The ID of the node which calculated the price. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


