# ComPatagonaPricemonitorShareApiPriceCalculationResult

The detailed result of the price calculation. Exactly one of the results will be defined. This class exists only in this shape to be able to generate the correct JSON schema. Ideally, we get rid of it in future and solely rely on a sealed trait for the price recommendation results. Or we differentiate between internal and external representation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**competitive_pricing_recommendation_result** | [**ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult**](ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.md) |  | [optional] 
**no_price_calculated** | [**ComPatagonaPricemonitorShareApiPriceCalculationResultNoPriceCalculated**](ComPatagonaPricemonitorShareApiPriceCalculationResultNoPriceCalculated.md) |  | [optional] 
**formula_recommendation_result** | [**ComPatagonaPricemonitorShareApiPriceCalculationResultFormulaRecommendationResult**](ComPatagonaPricemonitorShareApiPriceCalculationResultFormulaRecommendationResult.md) |  | [optional] 
**rounding_price_recommendation_result** | [**ComPatagonaPricemonitorShareApiRoundingPriceRecommendationResult**](ComPatagonaPricemonitorShareApiRoundingPriceRecommendationResult.md) |  | [optional] 
**price_calculation_failure** | [**ComPatagonaPricemonitorShareApiPriceCalculationResultPriceCalculationFailure**](ComPatagonaPricemonitorShareApiPriceCalculationResultPriceCalculationFailure.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


