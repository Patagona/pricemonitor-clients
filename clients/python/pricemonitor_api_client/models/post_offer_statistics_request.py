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


class PostOfferStatisticsRequest(object):
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
        'filter': 'ProductsFilter',
        'include_delivery_costs': 'bool',
        'own_shop_names': 'dict(str, list[str])',
        'range': 'TimeRange'
    }

    attribute_map = {
        'filter': 'filter',
        'include_delivery_costs': 'includeDeliveryCosts',
        'own_shop_names': 'ownShopNames',
        'range': 'range'
    }

    def __init__(self, filter=None, include_delivery_costs=None, own_shop_names=None, range=None, local_vars_configuration=None):  # noqa: E501
        """PostOfferStatisticsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._filter = None
        self._include_delivery_costs = None
        self._own_shop_names = None
        self._range = None
        self.discriminator = None

        self.filter = filter
        self.include_delivery_costs = include_delivery_costs
        self.own_shop_names = own_shop_names
        self.range = range

    @property
    def filter(self):
        """Gets the filter of this PostOfferStatisticsRequest.  # noqa: E501


        :return: The filter of this PostOfferStatisticsRequest.  # noqa: E501
        :rtype: ProductsFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this PostOfferStatisticsRequest.


        :param filter: The filter of this PostOfferStatisticsRequest.  # noqa: E501
        :type: ProductsFilter
        """
        if self.local_vars_configuration.client_side_validation and filter is None:  # noqa: E501
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def include_delivery_costs(self):
        """Gets the include_delivery_costs of this PostOfferStatisticsRequest.  # noqa: E501


        :return: The include_delivery_costs of this PostOfferStatisticsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_delivery_costs

    @include_delivery_costs.setter
    def include_delivery_costs(self, include_delivery_costs):
        """Sets the include_delivery_costs of this PostOfferStatisticsRequest.


        :param include_delivery_costs: The include_delivery_costs of this PostOfferStatisticsRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and include_delivery_costs is None:  # noqa: E501
            raise ValueError("Invalid value for `include_delivery_costs`, must not be `None`")  # noqa: E501

        self._include_delivery_costs = include_delivery_costs

    @property
    def own_shop_names(self):
        """Gets the own_shop_names of this PostOfferStatisticsRequest.  # noqa: E501

        Providing own shops names enables calculating shop positions. The keys are domain names. The values are lists of shop names.  # noqa: E501

        :return: The own_shop_names of this PostOfferStatisticsRequest.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._own_shop_names

    @own_shop_names.setter
    def own_shop_names(self, own_shop_names):
        """Sets the own_shop_names of this PostOfferStatisticsRequest.

        Providing own shops names enables calculating shop positions. The keys are domain names. The values are lists of shop names.  # noqa: E501

        :param own_shop_names: The own_shop_names of this PostOfferStatisticsRequest.  # noqa: E501
        :type: dict(str, list[str])
        """
        if self.local_vars_configuration.client_side_validation and own_shop_names is None:  # noqa: E501
            raise ValueError("Invalid value for `own_shop_names`, must not be `None`")  # noqa: E501

        self._own_shop_names = own_shop_names

    @property
    def range(self):
        """Gets the range of this PostOfferStatisticsRequest.  # noqa: E501


        :return: The range of this PostOfferStatisticsRequest.  # noqa: E501
        :rtype: TimeRange
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this PostOfferStatisticsRequest.


        :param range: The range of this PostOfferStatisticsRequest.  # noqa: E501
        :type: TimeRange
        """
        if self.local_vars_configuration.client_side_validation and range is None:  # noqa: E501
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

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
        if not isinstance(other, PostOfferStatisticsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostOfferStatisticsRequest):
            return True

        return self.to_dict() != other.to_dict()
