# ComPatagonaPricemonitorShareApiCustomerOrderV3

An order placed in a shop.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_costs** | **float** | Shipping costs of the order. This amount is included in totalPrice. | 
**order_id** | **str** | Unique ID of an order. This ID must be unique within the contract. | 
**items** | [**list[ComPatagonaPricemonitorShareApiCustomerOrderItemV2]**](ComPatagonaPricemonitorShareApiCustomerOrderItemV2.md) | List of purchased items. | 
**total_price** | **float** | Total price of the order, including all items, applicable taxes, and shipping costs. | 
**origin** | **str** | Origin of an order, e.g., the online shop where the order is placed. | 
**creation_date** | **datetime** | Timestamp in ISO 8601 format indicating when the order is placed. | 
**currency** | **str** | Currency used in the order, represented by ISO 4217 Currency Codes (e.g., EUR). | 
**referrer** | **str** | Optional referrer of an order. Third party (e.g. marketplace) which referred the customer to the online shop. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


