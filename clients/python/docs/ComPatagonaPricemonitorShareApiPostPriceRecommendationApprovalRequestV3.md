# ComPatagonaPricemonitorShareApiPostPriceRecommendationApprovalRequestV3

Represents a request to make a decision on a price recommendation approval for a specific product. This request is used to submit an approval decision (approve, reject, or overwrite) for a given product and price recommendation approval instance, identified by its product id and creation timestamp.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | **str** | The decision made on the approval.&lt;br&gt; Allowed values: \&quot;approved\&quot;, \&quot;rejected\&quot;, or \&quot;overwritten\&quot;. | 
**approval_created_at** | **datetime** | The timestamp when the approval was created, in ISO 8601 format. | 
**comment** | **str** | An optional comment regarding the decision. | [optional] 
**product_id** | **str** | The internal unique product identifier of Omnia 2.0. | 
**overwrite_price** | **float** | The manual price set by the user when the decision is \&quot;overwritten\&quot;, if applicable.&lt;br&gt; Must be provided and be ≥ 0.01 when decision is \&quot;overwritten\&quot;.&lt;br&gt; Must **not** be set for other decision values. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


