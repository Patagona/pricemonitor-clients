# ComPatagonaPricemonitorShareApiApiPriceRecommendation

Represents a price recommendation of the pricemonitor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_price** | **float** | The price of the cheapest offer of the own shop(s) on the relevant domain | [optional] 
**delivery_costs** | **float** | The delivery costs which were considered for the recommended price | [optional] 
**timestamp** | **datetime** | The timestamp when the price recommendation has been calculated | 
**old_delivery_costs** | **float** | The delivery costs corresponding to &#x60;oldPrice&#x60; | [optional] 
**tags** | [**list[ComPatagonaPricemonitorShareApiExtendedTag]**](ComPatagonaPricemonitorShareApiExtendedTag.md) | Additional information on this product | 
**price** | **float** | The recommended price of the relevant domain | 
**old_position** | **int** | The old position on the relevant domain | [optional] 
**gtin** | **float** | GTIN of the product | [optional] 
**relative_price_change_percentage** | **float** | Absolute percentage how the recommended price changed compared to the &#x60;oldPrice&#x60; e.g. 200 stands for 200% which means the recommended price has doubled | [optional] 
**new_position** | **int** | The new position on the relevant domain | [optional] 
**decisive_strategy_branch_name** | **str** | The strategy branch name that calculated the price. This is only filled if the Strategy branch that calculated the price was given a name in the strategy tree. It will have the name that was active at the time the price was calculated (see timestamp) | [optional] 
**customer_product_id** | **str** | The customer&#39;s id of the product | [optional] 
**original_max_price_boundary** | **float** | Max price boundary during the time when the price was calculated | 
**relevant_domain** | **str** | The decisive domain of the price recommendation. It&#39;s been determined by the cheapest price recommendation. | [optional] 
**original_min_price_boundary** | **float** | Min price boundary during the time when the price was calculated | 
**currency** | **str** | The currency of the price recommendation. | 
**product_id** | **str** | The internal product id of the pricemonitor | 
**original_tags** | [**list[ComPatagonaPricemonitorShareApiExtendedTag]**](ComPatagonaPricemonitorShareApiExtendedTag.md) | List of tags which were set during the time when the price has been calculated. ATTENTION: These are historic tags which are maybe outdated or incomplete. | 
**decisive_strategy_tree_leaf_node_id** | **int** | The leaf node of the strategy branch that calculated the price. This id references the node in the strategy branch that was active at the time the price was calculated (see timestamp) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


