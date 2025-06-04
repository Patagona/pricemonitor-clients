# ComPatagonaPricemonitorShareApiPriceRecommendationsApprovalQueryResponseV3

Represents the approval details for a price recommendation for a specific product and timestamp.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decisions** | [**list[ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3]**](ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3.md) | The sequence of decisions made regarding this approval. | 
**updated_at** | **datetime** | The timestamp when the approval was last updated, in ISO 8601 format,. | 
**required_approvals** | **int** | The number of approvals required for a pricing decision (must be ≥ 1). | 
**price_recommendation** | [**ComPatagonaPricemonitorShareApiApiPriceRecommendation**](ComPatagonaPricemonitorShareApiApiPriceRecommendation.md) |  | 
**status** | **str** | The current approval status. &lt;br&gt; Allowed values: \&quot;pending\&quot;, \&quot;approved\&quot;, \&quot;rejected\&quot;, \&quot;outdated\&quot;, or \&quot;overwritten\&quot;. | 
**created_at** | **datetime** | The timestamp when the approval was created, in ISO 8601 format,. | 
**product_id** | **str** | The internal unique product identifier of Omnia 2.0. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


