# ComPatagonaPricemonitorShareApiPriceApprovalDecisionV3

Represents a single decision made by a user regarding a price recommendation approval.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_email** | **str** | The email address of the user who made the decision. | 
**decision** | **str** | The decision made by the user. &lt;br&gt; Allowed values: \&quot;approved\&quot;, \&quot;rejected\&quot;, or \&quot;overwritten\&quot;. | 
**comment** | **str** | An optional comment provided by the user. | [optional] 
**created_at** | **datetime** | The timestamp when the decision was made. | 
**user_id** | **int** | The unique identifier of the user who made the decision. | 
**superseded** | **bool** | Indicates if this decision was superseded by a later decision. | 
**overwrite_price** | **float** | The manual price set by the user when the recommendation was overwritten, if applicable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


