# ComPatagonaPricemonitorShareApiPriceCalculationResultFormulaRecommendationResult

A price recommendation has been calculated by a formula.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**own_offers** | [**list[ComPatagonaPricemonitorShareApiApiOffer]**](ComPatagonaPricemonitorShareApiApiOffer.md) | The own offers which have been considered for the price calculation. | 
**competitor_offers** | [**list[ComPatagonaPricemonitorShareApiApiOffer]**](ComPatagonaPricemonitorShareApiApiOffer.md) | The offers of the competitors which have been considered for the price calculation. | 
**min_price_boundary** | [**ComPatagonaPricemonitorShareApiPriceBoundaryDetails**](ComPatagonaPricemonitorShareApiPriceBoundaryDetails.md) |  | 
**variables** | [**list[ComPatagonaPricemonitorShareApiFormulaVariable]**](ComPatagonaPricemonitorShareApiFormulaVariable.md) | The relevant variables used in the formula. | 
**unit_price_recommendation** | **float** | The calculated price recommendation. | 
**formula** | **str** | The unevaluated formula. | 
**max_price_boundary** | [**ComPatagonaPricemonitorShareApiPriceBoundaryDetails**](ComPatagonaPricemonitorShareApiPriceBoundaryDetails.md) |  | 
**node_id** | **int** | The ID of the node which calculated the price. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


