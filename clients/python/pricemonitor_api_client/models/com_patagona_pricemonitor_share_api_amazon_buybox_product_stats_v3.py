# coding: utf-8

"""
    Omnia 2.0 API The Omnia 2.0 API is RESTful and provides access to the backend of Omnia 2.0 and Pricemonitor. It is used to manage products, offers, contracts, and more.  This API supports both public endpoints for customer integration and internal endpoints for platform management. All endpoints are authenticated using either Basic Authentication or JWT Bearer tokens.

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.7216
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pricemonitor_api_client.configuration import Configuration


class ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'product_id': 'float',
        'is_in_prime_buybox': 'bool',
        'is_in_non_prime_buybox': 'bool'
    }

    attribute_map = {
        'product_id': 'productId',
        'is_in_prime_buybox': 'isInPrimeBuybox',
        'is_in_non_prime_buybox': 'isInNonPrimeBuybox'
    }

    def __init__(self, product_id=None, is_in_prime_buybox=None, is_in_non_prime_buybox=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._product_id = None
        self._is_in_prime_buybox = None
        self._is_in_non_prime_buybox = None
        self.discriminator = None

        self.product_id = product_id
        self.is_in_prime_buybox = is_in_prime_buybox
        self.is_in_non_prime_buybox = is_in_non_prime_buybox

    @property
    def product_id(self):
        """Gets the product_id of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.  # noqa: E501

        Internal product identifier  # noqa: E501

        :return: The product_id of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.  # noqa: E501
        :rtype: float
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.

        Internal product identifier  # noqa: E501

        :param product_id: The product_id of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and product_id is None:  # noqa: E501
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def is_in_prime_buybox(self):
        """Gets the is_in_prime_buybox of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.  # noqa: E501

        Indicates if product is Amazon Prime product and is in Amazon Buybox  # noqa: E501

        :return: The is_in_prime_buybox of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_prime_buybox

    @is_in_prime_buybox.setter
    def is_in_prime_buybox(self, is_in_prime_buybox):
        """Sets the is_in_prime_buybox of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.

        Indicates if product is Amazon Prime product and is in Amazon Buybox  # noqa: E501

        :param is_in_prime_buybox: The is_in_prime_buybox of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_in_prime_buybox is None:  # noqa: E501
            raise ValueError("Invalid value for `is_in_prime_buybox`, must not be `None`")  # noqa: E501

        self._is_in_prime_buybox = is_in_prime_buybox

    @property
    def is_in_non_prime_buybox(self):
        """Gets the is_in_non_prime_buybox of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.  # noqa: E501

        Indicates if product is in Amazon Buybox  # noqa: E501

        :return: The is_in_non_prime_buybox of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_non_prime_buybox

    @is_in_non_prime_buybox.setter
    def is_in_non_prime_buybox(self, is_in_non_prime_buybox):
        """Sets the is_in_non_prime_buybox of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.

        Indicates if product is in Amazon Buybox  # noqa: E501

        :param is_in_non_prime_buybox: The is_in_non_prime_buybox of this ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_in_non_prime_buybox is None:  # noqa: E501
            raise ValueError("Invalid value for `is_in_non_prime_buybox`, must not be `None`")  # noqa: E501

        self._is_in_non_prime_buybox = is_in_non_prime_buybox

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiAmazonBuyboxProductStatsV3):
            return True

        return self.to_dict() != other.to_dict()
