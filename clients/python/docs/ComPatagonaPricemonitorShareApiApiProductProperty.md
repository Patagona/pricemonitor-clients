# ComPatagonaPricemonitorShareApiApiProductProperty

Product properties represent additional information for a product. The `stringValue` is used for deriving further evaluated values at server-side: - **Date Properties**: Submit dates in the `stringValue` field using the ISO 8601 format (e.g., `YYYY-MM-DDTHH:MM:SSZ`). This ensures that the server correctly interprets the date and time. - **Numeric Properties**: Submit numbers in the `stringValue` field by using dot as decimal separator.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of the property. It can&#39;t be empty. At maximum 100 characters are allowed. | 
**string_value** | **str** | The text value of the property. At maximum 10,000 characters are allowed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


