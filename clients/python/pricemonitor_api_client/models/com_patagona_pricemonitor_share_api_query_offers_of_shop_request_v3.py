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


class ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3(object):
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
        'shop': 'str',
        'end_date': 'datetime',
        'start': 'int',
        'limit': 'int',
        'start_date': 'datetime'
    }

    attribute_map = {
        'shop': 'shop',
        'end_date': 'endDate',
        'start': 'start',
        'limit': 'limit',
        'start_date': 'startDate'
    }

    def __init__(self, shop=None, end_date=None, start=None, limit=None, start_date=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._shop = None
        self._end_date = None
        self._start = None
        self._limit = None
        self._start_date = None
        self.discriminator = None

        self.shop = shop
        self.end_date = end_date
        self.start = start
        self.limit = limit
        self.start_date = start_date

    @property
    def shop(self):
        """Gets the shop of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501


        :return: The shop of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.


        :param shop: The shop of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and shop is None:  # noqa: E501
            raise ValueError("Invalid value for `shop`, must not be `None`")  # noqa: E501

        self._shop = shop

    @property
    def end_date(self):
        """Gets the end_date of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501


        :return: The end_date of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.


        :param end_date: The end_date of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and end_date is None:  # noqa: E501
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def start(self):
        """Gets the start of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501


        :return: The start of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.


        :param start: The start of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and start is None:  # noqa: E501
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501


        :return: The limit of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.


        :param limit: The limit of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def start_date(self):
        """Gets the start_date of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501


        :return: The start_date of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.


        :param start_date: The start_date of this ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiQueryOffersOfShopRequestV3):
            return True

        return self.to_dict() != other.to_dict()
