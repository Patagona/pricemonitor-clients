# ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult

A price recommendation has been calculated by competitive pricing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjust_to_next_pricier** | **bool** | When a target position can&#39;t be reached due to the price boundary, the target position gets realigned to the next reachable one (within the price boundary) by this setting. | 
**target_position** | **int** | The target position which has been considered. | 
**include_delivery_costs** | **bool** | Determines if the delivery costs should be included in the price calculation. | 
**own_offers** | [**list[ComPatagonaPricemonitorShareApiApiOffer]**](ComPatagonaPricemonitorShareApiApiOffer.md) | The own offers which have been considered for the price calculation. | 
**competitor_offers** | [**list[ComPatagonaPricemonitorShareApiApiOffer]**](ComPatagonaPricemonitorShareApiApiOffer.md) | The offers of the competitors which have been considered for the price calculation. | 
**price_gap** | **float** | The price gap which has been considered.&lt;br&gt; - A positive value means to underbid the target position.&lt;br&gt; - A zero value means to match the target position.&lt;br&gt; - A negative value means to overbid the target position. | 
**min_price_boundary** | [**ComPatagonaPricemonitorShareApiPriceBoundaryDetails**](ComPatagonaPricemonitorShareApiPriceBoundaryDetails.md) |  | 
**own_delivery_costs** | **float** | The own delivery costs which have been considered. Only relevant if &#39;includeDeliveryCosts&#39; is set to true. | [optional] 
**unit_price_recommendation** | **float** | The calculated price recommendation. | 
**max_price_boundary** | [**ComPatagonaPricemonitorShareApiPriceBoundaryDetails**](ComPatagonaPricemonitorShareApiPriceBoundaryDetails.md) |  | 
**price_gap_unit** | [**ComPatagonaPricemonitorShareApiPriceGapUnit**](ComPatagonaPricemonitorShareApiPriceGapUnit.md) |  | 
**node_id** | **int** | The ID of the node which calculated the price. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


