# ComPatagonaPricemonitorShareApiRoundingPriceRecommendationResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**own_offers** | [**ComPatagonaPricemonitorShareApiApiOffer**](ComPatagonaPricemonitorShareApiApiOffer.md) |  | [optional] 
**competitor_offers** | [**ComPatagonaPricemonitorShareApiApiOffer**](ComPatagonaPricemonitorShareApiApiOffer.md) |  | [optional] 
**price_steps** | **list[str]** | List of values to round against. They are in unit&#39;s of cent (100th of the base currency). They are defined as strings and may contain leading zeroes to indicate allowed increments. For example:&lt;br&gt;                    - [\&quot;5\&quot;] allows prices of 0.05€, 0.15€, 0.25€, 0.35€, ... (increments of 10 cents)&lt;br&gt;                    - [\&quot;05\&quot;] allows prices of 0.05€, 1.05€, 2.05€, 3.05€ ... (increments of 100 cents)&lt;br&gt;                    - [\&quot;00\&quot;, \&quot;50\&quot;] allows prices of 0.50€, 1.00€, 1.50€, 2.00€ | 
**step_selection** | **str** | Defines how to select the price step to round to. Allowed values are: &#x60;nextLower&#x60;, &#x60;nextHigher&#x60; and &#x60;closest&#x60; | 
**min_price_boundary** | [**ComPatagonaPricemonitorShareApiPriceBoundaryDetails**](ComPatagonaPricemonitorShareApiPriceBoundaryDetails.md) |  | 
**original_price_recommendation** | [**ComPatagonaPricemonitorShareApiPriceCalculationResult**](ComPatagonaPricemonitorShareApiPriceCalculationResult.md) |  | 
**unit_price_recommendation** | **float** | The calculated price recommendation. | 
**max_price_boundary** | [**ComPatagonaPricemonitorShareApiPriceBoundaryDetails**](ComPatagonaPricemonitorShareApiPriceBoundaryDetails.md) |  | 
**adjust_to_next_reachable_price_step** | **bool** | Implements the behavior that happens when the original price calculation is in the min-/max price  boundary and the rounding would cause it to violate the price boundary. If set to true, the price  step will be adjusted to the next reachable price step. Defaults to false, in which case the  original price recommendation will be used as the fallback. | [optional] 
**node_id** | **float** | The ID of the node which calculated the price. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


