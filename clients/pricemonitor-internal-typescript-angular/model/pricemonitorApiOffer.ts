/**
 * Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts and more.
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.7015
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { PricemonitorOfferAttribute } from './pricemonitorOfferAttribute';


export interface PricemonitorApiOffer { 
    positionByTotalPrice: number;
    deliveryCosts: number;
    maxDeliveryTime?: number;
    url: string;
    vendorDomainId?: string;
    domain: string;
    price: number;
    minDeliveryTime?: number;
    gtin?: number;
    positionByUnitPrice: number;
    availability?: boolean;
    attributes: Array<PricemonitorOfferAttribute>;
    vendorName: string;
    retrievalDate?: string;
    creationDate: string;
    productName: string;
    currency: string;
    productId: string;
    ignored: boolean;
}

