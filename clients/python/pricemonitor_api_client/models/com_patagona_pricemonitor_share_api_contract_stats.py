# coding: utf-8

"""
    Pricemonitor API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.5838
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pricemonitor_api_client.configuration import Configuration


class ComPatagonaPricemonitorShareApiContractStats(object):
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
        'product_count': 'int',
        'portal_count': 'int',
        'all_offer_count': 'float',
        'offer_count': 'float',
        'vendor_count': 'float'
    }

    attribute_map = {
        'product_count': 'productCount',
        'portal_count': 'portalCount',
        'all_offer_count': 'allOfferCount',
        'offer_count': 'offerCount',
        'vendor_count': 'vendorCount'
    }

    def __init__(self, product_count=None, portal_count=None, all_offer_count=None, offer_count=None, vendor_count=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiContractStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._product_count = None
        self._portal_count = None
        self._all_offer_count = None
        self._offer_count = None
        self._vendor_count = None
        self.discriminator = None

        self.product_count = product_count
        self.portal_count = portal_count
        self.all_offer_count = all_offer_count
        self.offer_count = offer_count
        self.vendor_count = vendor_count

    @property
    def product_count(self):
        """Gets the product_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501

        The count of currently monitored products  # noqa: E501

        :return: The product_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :rtype: int
        """
        return self._product_count

    @product_count.setter
    def product_count(self, product_count):
        """Sets the product_count of this ComPatagonaPricemonitorShareApiContractStats.

        The count of currently monitored products  # noqa: E501

        :param product_count: The product_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and product_count is None:  # noqa: E501
            raise ValueError("Invalid value for `product_count`, must not be `None`")  # noqa: E501

        self._product_count = product_count

    @property
    def portal_count(self):
        """Gets the portal_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501

        The number of actively monitored domains  # noqa: E501

        :return: The portal_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :rtype: int
        """
        return self._portal_count

    @portal_count.setter
    def portal_count(self, portal_count):
        """Sets the portal_count of this ComPatagonaPricemonitorShareApiContractStats.

        The number of actively monitored domains  # noqa: E501

        :param portal_count: The portal_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and portal_count is None:  # noqa: E501
            raise ValueError("Invalid value for `portal_count`, must not be `None`")  # noqa: E501

        self._portal_count = portal_count

    @property
    def all_offer_count(self):
        """Gets the all_offer_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501

        The number of offers found for the monitored products without any filters applied  # noqa: E501

        :return: The all_offer_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :rtype: float
        """
        return self._all_offer_count

    @all_offer_count.setter
    def all_offer_count(self, all_offer_count):
        """Sets the all_offer_count of this ComPatagonaPricemonitorShareApiContractStats.

        The number of offers found for the monitored products without any filters applied  # noqa: E501

        :param all_offer_count: The all_offer_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and all_offer_count is None:  # noqa: E501
            raise ValueError("Invalid value for `all_offer_count`, must not be `None`")  # noqa: E501

        self._all_offer_count = all_offer_count

    @property
    def offer_count(self):
        """Gets the offer_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501

        The number of offers found for the monitored products after filtering  # noqa: E501

        :return: The offer_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :rtype: float
        """
        return self._offer_count

    @offer_count.setter
    def offer_count(self, offer_count):
        """Sets the offer_count of this ComPatagonaPricemonitorShareApiContractStats.

        The number of offers found for the monitored products after filtering  # noqa: E501

        :param offer_count: The offer_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and offer_count is None:  # noqa: E501
            raise ValueError("Invalid value for `offer_count`, must not be `None`")  # noqa: E501

        self._offer_count = offer_count

    @property
    def vendor_count(self):
        """Gets the vendor_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501

        The count of vendors found for the monitored products  # noqa: E501

        :return: The vendor_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :rtype: float
        """
        return self._vendor_count

    @vendor_count.setter
    def vendor_count(self, vendor_count):
        """Sets the vendor_count of this ComPatagonaPricemonitorShareApiContractStats.

        The count of vendors found for the monitored products  # noqa: E501

        :param vendor_count: The vendor_count of this ComPatagonaPricemonitorShareApiContractStats.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and vendor_count is None:  # noqa: E501
            raise ValueError("Invalid value for `vendor_count`, must not be `None`")  # noqa: E501

        self._vendor_count = vendor_count

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiContractStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiContractStats):
            return True

        return self.to_dict() != other.to_dict()