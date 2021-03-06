/**
 * Pricemonitor API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.5687
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { OfferAttribute } from './offerAttribute';


export interface ApiOffer { 
    attributes?: Array<OfferAttribute>;
    availability?: boolean;
    creationDate: string;
    contractId: string;
    currency: string;
    deliveryCosts: number;
    domain: string;
    gtin?: number;
    ignored: boolean;
    maxDeliveryTime?: number;
    minDeliveryTime?: number;
    positionByUnitPrice?: number;
    positionByTotalPrice?: number;
    price: number;
    productId: string;
    productName: string;
    retrievalDate?: string;
    url: string;
    vendorDomainId?: string;
    vendorName: string;
}

