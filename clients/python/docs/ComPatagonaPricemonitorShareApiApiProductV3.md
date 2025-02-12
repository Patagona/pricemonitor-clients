# ComPatagonaPricemonitorShareApiApiProductV3

A product in the pricemonitor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the product. | 
**tags** | [**list[ComPatagonaPricemonitorShareApiApiProductV3Tags]**](ComPatagonaPricemonitorShareApiApiProductV3Tags.md) | Additional information on this product. | 
**min_price_boundary** | **float** | Maximum price which pricemonitor can recommend for the product. It won&#39;t recommend any price above this boundary. | [optional] 
**gtin** | **float** | GTIN of the product. Can be optionally. | [optional] 
**customer_product_id** | **str** | The customer&#39;s id of the product. This field allows to link products in pricemonitor to products in the customer&#39;s system. | [optional] 
**id** | **str** | Id of the product in the pricemonitor. | 
**max_price_boundary** | **float** | Minimum price which pricemonitor can recommend for the product. It won&#39;t recommend any price below this boundary. | [optional] 
**reference_price** | **float** | Some price that will be used as benchmark for certain components in pricemonitor. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


