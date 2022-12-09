# ComPatagonaPricemonitorShareApiGetAllDomainsV3Domains

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | domain url | 
**domain_id** | **float** | internal domain id | 
**offer_sources** | **list[str]** | list of offerSources for the domain OfferSource:  Describes the origin of the offers. Domain may have more than one offer sources. Here are the possible offer sources: DEFAULT_MONITORING Offers - which are gathered via the monitoring-pipeline by a standard product search. This is typically done via GTIN. CUSTOM_MONITORING Offers - which are gathered via the monitoring-pipeline by a customized search. For instance via tags. OMNIA_CUSTOM_SPIDERING Offers - which originate from omnia custom spidering sources. The domain needs to be prefixed with \&quot;omnia.custom.spidering.\&quot;. PUSH_API Offers - which originate from services where we have a direct API connection and get informed about offer changes. Example: Offers from Amazon-Repricer OTHER Offers - which originate from other sources e.g. Scripts which publish offers | 
**name** | **str** | display name for the domain | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


