# coding: utf-8

"""
    Pricemonitor API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.6671
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pricemonitor_api_client.configuration import Configuration


class ComPatagonaPricemonitorShareApiProductOfferStatisticsV31(object):
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
        'unit_price_stats': 'ComPatagonaPricemonitorShareApiPriceStatisticsV31',
        'total_price_stats': 'ComPatagonaPricemonitorShareApiPriceStatisticsV31'
    }

    attribute_map = {
        'unit_price_stats': 'unitPriceStats',
        'total_price_stats': 'totalPriceStats'
    }

    def __init__(self, unit_price_stats=None, total_price_stats=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiProductOfferStatisticsV31 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._unit_price_stats = None
        self._total_price_stats = None
        self.discriminator = None

        self.unit_price_stats = unit_price_stats
        self.total_price_stats = total_price_stats

    @property
    def unit_price_stats(self):
        """Gets the unit_price_stats of this ComPatagonaPricemonitorShareApiProductOfferStatisticsV31.  # noqa: E501


        :return: The unit_price_stats of this ComPatagonaPricemonitorShareApiProductOfferStatisticsV31.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiPriceStatisticsV31
        """
        return self._unit_price_stats

    @unit_price_stats.setter
    def unit_price_stats(self, unit_price_stats):
        """Sets the unit_price_stats of this ComPatagonaPricemonitorShareApiProductOfferStatisticsV31.


        :param unit_price_stats: The unit_price_stats of this ComPatagonaPricemonitorShareApiProductOfferStatisticsV31.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiPriceStatisticsV31
        """
        if self.local_vars_configuration.client_side_validation and unit_price_stats is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_price_stats`, must not be `None`")  # noqa: E501

        self._unit_price_stats = unit_price_stats

    @property
    def total_price_stats(self):
        """Gets the total_price_stats of this ComPatagonaPricemonitorShareApiProductOfferStatisticsV31.  # noqa: E501


        :return: The total_price_stats of this ComPatagonaPricemonitorShareApiProductOfferStatisticsV31.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiPriceStatisticsV31
        """
        return self._total_price_stats

    @total_price_stats.setter
    def total_price_stats(self, total_price_stats):
        """Sets the total_price_stats of this ComPatagonaPricemonitorShareApiProductOfferStatisticsV31.


        :param total_price_stats: The total_price_stats of this ComPatagonaPricemonitorShareApiProductOfferStatisticsV31.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiPriceStatisticsV31
        """
        if self.local_vars_configuration.client_side_validation and total_price_stats is None:  # noqa: E501
            raise ValueError("Invalid value for `total_price_stats`, must not be `None`")  # noqa: E501

        self._total_price_stats = total_price_stats

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiProductOfferStatisticsV31):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiProductOfferStatisticsV31):
            return True

        return self.to_dict() != other.to_dict()