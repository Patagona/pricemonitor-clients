# ComPatagonaPricemonitorShareApiExtendedTag

Tags represent additional information of a product. Extended tags can contain evaluated values like numbers which are determined during product import. The `stringValue` is used for deriving the evaluated values. Example: You provide a tag with label \"strategy\" and `stringValue` \"1\" during product import. This will be evaluated to these extended values: - integerValue  1 - doubleValue   1.0 - booleanValue  true
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**double_value** | **float** | The double value depends on the decimal separator which has been provided during product import. | [optional] 
**integer_value** | **int** | The integer value of the tag. It&#39;s only defined when the &#x60;stringValue&#x60; consists solely of digits. | [optional] 
**label** | **str** | The name of the tag. It can&#39;t be empty. | 
**string_value** | **str** | The text value of the tag. | 
**boolean_value** | **bool** | The boolean value of the tag. It&#39;s only set to true when the &#x60;stringValue&#x60; is \&quot;1\&quot; or \&quot;true\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


