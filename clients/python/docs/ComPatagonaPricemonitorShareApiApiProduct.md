# ComPatagonaPricemonitorShareApiApiProduct

Represents a product in Omnia 2.0.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the product. | 
**tags** | [**list[ComPatagonaPricemonitorShareApiTag]**](ComPatagonaPricemonitorShareApiTag.md) | Additional imported information as key-value pairs about this product. | 
**min_price_boundary** | **float** | The minimum price that Omnia 2.0 can recommend for the product. Omnia 2.0 won&#39;t recommend any price below this boundary. | [optional] 
**gtin** | **float** | GTIN / EAN of the product. This field is optional. | [optional] 
**customer_product_id** | **str** | Your ID of the product. This field allows to link products in Omnia 2.0 to products in your system. | [optional] 
**id** | **str** | The internal product ID in Omnia 2.0. | 
**max_price_boundary** | **float** | The maximum price that Omnia 2.0 can recommend for the product. Omnia 2.0 won&#39;t recommend any price above this boundary. | [optional] 
**reference_price** | **float** | The current selling price of the product. This price will be used as benchmark or variable for certain components in Omnia 2.0. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


