# PostProductsRequest

Request body which contains products
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**list[PostProduct]**](PostProduct.md) | Products which should be added to the pricemonitor | 
**version** | **str** | Version of the request body. Only version 2 is supported. | 
**identifying_attributes** | [**list[PostProductsIdentifyingAttribute]**](PostProductsIdentifyingAttribute.md) | Non-empty list of product attributes which identify your products uniquely. Please ensure that you specify only one attribute in the list. Avoid using tags as an identifier, as this feature will soon be deprecated. By doing so, may loose historical market data during product import. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


