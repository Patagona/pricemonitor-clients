# PostProduct

Product data structure for creating or updating products in the system
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Product name or title as displayed to customers | 
**customer_product_id** | **str** | Customer-specific product identifier. This can be your internal SKU or product ID. Used for mapping products between your system and the pricemonitor.  | [optional] 
**gtin** | **int** | Global Trade Item Number (GTIN) - typically EAN-13, UPC-A, or GTIN-14. Must be a valid positive number representing the product&#39;s global identifier.  | [optional] 
**reference_price** | **float** | Reference price for the product.  **For Omnia 2.0:** This represents the selling price - the actual price at which you sell the product. **For Pricemonitor:** One of the use cases is to treat this as MSRP (Manufacturer&#39;s Suggested Retail Price).  Used as a baseline for pricing strategies and recommendations. Will be rounded to two decimal places using half-up rounding.  | 
**min_price_boundary** | **float** | Minimum allowed price boundary for automated pricing. Must be less than or equal to maxPriceBoundary. Will be rounded to two decimal places using half-up rounding.  | 
**max_price_boundary** | **float** | Maximum allowed price boundary for automated pricing. Must be greater than or equal to minPriceBoundary. Will be rounded to two decimal places using half-up rounding.  | 
**tags** | [**list[TagInput]**](TagInput.md) | Product tags for categorization and strategy application. Used by pricing strategies to group and target specific products.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


