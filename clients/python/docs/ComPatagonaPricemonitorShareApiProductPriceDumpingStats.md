# ComPatagonaPricemonitorShareApiProductPriceDumpingStats

This class contains the number of price dumping events. The counts prefixed with \"uniqueProduct\" only count the events once per product, the non prefixed counts count every event. If we are unable to detect which vendor reduced the price first, because we only sampled the price when multiple vendors are at the same price, those events are counted in the fields infixed with \"potetially\".
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products_at_min_price** | **int** | This field denotes the number of products at the min price from the queried vendors, at the respective newest timestamp per domain and product. | 
**unique_product_initiated_price_dumpings** | **int** |  | 
**unique_product_potentially_initiated_price_dumpings** | **int** |  | 
**initiated_price_dumpings** | **int** |  | 
**potentially_initiated_price_dumpings** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


