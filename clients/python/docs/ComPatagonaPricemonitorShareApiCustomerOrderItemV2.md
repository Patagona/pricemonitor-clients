# ComPatagonaPricemonitorShareApiCustomerOrderItemV2

An ordered item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | ID of the item in the customer&#39;s system. It is expected to be the customerProductId. It should be guaranteed that the itemId can be always assigned to only one product or variant. | 
**unit_price** | **float** | Gross unit price of a single item, including applicable taxes. | 
**quantity** | **int** | How often the item was purchased. | 
**tax_percentage** | **float** | Tax percentage applied on the unit price, e.g. 20 for 20% tax. This percentage is used to determine the tax component of the unitPrice, but the unitPrice itself already includes this tax. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


