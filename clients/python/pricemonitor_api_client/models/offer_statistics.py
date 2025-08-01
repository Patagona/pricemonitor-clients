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


class OfferStatistics(object):
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
        'average_price': 'float',
        'min_price': 'float',
        'offer_count': 'int',
        'own_position': 'ShopRank'
    }

    attribute_map = {
        'average_price': 'averagePrice',
        'min_price': 'minPrice',
        'offer_count': 'offerCount',
        'own_position': 'ownPosition'
    }

    def __init__(self, average_price=None, min_price=None, offer_count=None, own_position=None, local_vars_configuration=None):  # noqa: E501
        """OfferStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._average_price = None
        self._min_price = None
        self._offer_count = None
        self._own_position = None
        self.discriminator = None

        self.average_price = average_price
        self.min_price = min_price
        self.offer_count = offer_count
        if own_position is not None:
            self.own_position = own_position

    @property
    def average_price(self):
        """Gets the average_price of this OfferStatistics.  # noqa: E501

        The average price of the offers, always be provided with two decimal places  # noqa: E501

        :return: The average_price of this OfferStatistics.  # noqa: E501
        :rtype: float
        """
        return self._average_price

    @average_price.setter
    def average_price(self, average_price):
        """Sets the average_price of this OfferStatistics.

        The average price of the offers, always be provided with two decimal places  # noqa: E501

        :param average_price: The average_price of this OfferStatistics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and average_price is None:  # noqa: E501
            raise ValueError("Invalid value for `average_price`, must not be `None`")  # noqa: E501

        self._average_price = average_price

    @property
    def min_price(self):
        """Gets the min_price of this OfferStatistics.  # noqa: E501

        The lowest price of the offers, always be provided with two decimal places  # noqa: E501

        :return: The min_price of this OfferStatistics.  # noqa: E501
        :rtype: float
        """
        return self._min_price

    @min_price.setter
    def min_price(self, min_price):
        """Sets the min_price of this OfferStatistics.

        The lowest price of the offers, always be provided with two decimal places  # noqa: E501

        :param min_price: The min_price of this OfferStatistics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and min_price is None:  # noqa: E501
            raise ValueError("Invalid value for `min_price`, must not be `None`")  # noqa: E501

        self._min_price = min_price

    @property
    def offer_count(self):
        """Gets the offer_count of this OfferStatistics.  # noqa: E501

        The number of the found offers  # noqa: E501

        :return: The offer_count of this OfferStatistics.  # noqa: E501
        :rtype: int
        """
        return self._offer_count

    @offer_count.setter
    def offer_count(self, offer_count):
        """Sets the offer_count of this OfferStatistics.

        The number of the found offers  # noqa: E501

        :param offer_count: The offer_count of this OfferStatistics.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offer_count is None:  # noqa: E501
            raise ValueError("Invalid value for `offer_count`, must not be `None`")  # noqa: E501

        self._offer_count = offer_count

    @property
    def own_position(self):
        """Gets the own_position of this OfferStatistics.  # noqa: E501


        :return: The own_position of this OfferStatistics.  # noqa: E501
        :rtype: ShopRank
        """
        return self._own_position

    @own_position.setter
    def own_position(self, own_position):
        """Sets the own_position of this OfferStatistics.


        :param own_position: The own_position of this OfferStatistics.  # noqa: E501
        :type: ShopRank
        """

        self._own_position = own_position

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
        if not isinstance(other, OfferStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OfferStatistics):
            return True

        return self.to_dict() != other.to_dict()
