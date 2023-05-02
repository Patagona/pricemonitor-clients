# PostProduct

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**list[TagInput]**](TagInput.md) |  | 
**customer_product_id** | **str** |  | [optional] 
**gtin** | **int** | Must not be negative | [optional] 
**min_price_boundary** | **float** | Must not be less than 0.01. Must not be larger than maxPriceBoundary. Will be rounded to the second decimal digit (half up) | 
**max_price_boundary** | **float** | Must not be less than minPriceBoundary. Must not be larger than 9,999,999,999,999.99. Will be rounded to the second decimal digit (half up) | 
**name** | **str** | Must not have more than 999 characters. Will be rounded to the second decimal digit (half up) | 
**reference_price** | **float** | Must not be less than 0.01. Must not be larger than 9,999,999,999,999.99. Will be rounded to the second decimal digit (half up) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


