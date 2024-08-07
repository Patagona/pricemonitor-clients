# ComPatagonaPricemonitorShareApiCustomerOrderV2

An order placed in a shop.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_costs** | **float** | Shipping costs of the order | 
**order_id** | **str** | Unique id of an order. It must mean unique in the shop, not in the pricemonitor. | 
**items** | [**list[ComPatagonaPricemonitorShareApiCustomerOrderItemV2]**](ComPatagonaPricemonitorShareApiCustomerOrderItemV2.md) | List of bought items | 
**total_price** | **float** | Total price of the order | 
**product_mappings** | [**list[ComPatagonaPricemonitorShareApiCustomerOrderProductMappingV2]**](ComPatagonaPricemonitorShareApiCustomerOrderProductMappingV2.md) | A relation from the products in your system to the pricemonitor. Currently it must contain exactly one element. | 
**origin** | **str** | Origin of an order, e.g. the online shop were the order is placed | 
**creation_date** | **datetime** | Date when the order is created in UTC | 
**currency** | **str** | Currency used in the order. ISO 4217 Currency Codes: e.g. EUR | 
**referrer** | **str** | Referrer of an order. Third party (e.g. marketplace) which referred the customer to the online shop | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


