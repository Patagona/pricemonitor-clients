# ComPatagonaPricemonitorShareApiPriceDumpingStatsRequest

A request for price dumping statistics for the given shops.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Start of the timerange in which we search for price dumping events | 
**end_date** | **datetime** | End of the timerange in which we search for price dumping events | 
**include_delivery_costs** | **bool** | Indicates if we consider price + delivery cost to detect price changes or only price | 
**shops** | [**list[ComPatagonaPricemonitorShareApiShopV3]**](ComPatagonaPricemonitorShareApiShopV3.md) | Specifies for which shops we detect price dumping events | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


