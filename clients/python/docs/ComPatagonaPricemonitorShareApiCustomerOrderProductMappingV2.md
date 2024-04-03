# ComPatagonaPricemonitorShareApiCustomerOrderProductMappingV2

We originally planned to support complex mappings, but for sake of maintainability we restrict the mappings to itemId-> (customerProductId or productId)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Identifier field within item. Only valid value is &#39;itemId&#39; | 
**target** | **str** | Must be &#39;customerProductId&#39; or &#39;productId&#39; since plugins are still publishing both values. The semantics are actually the same. In both cases they address the customerProductId. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


