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


class ComPatagonaPricemonitorShareApiVendorShopMappingV3(object):
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
        'id': 'float',
        'vendor_name': 'str',
        'shops': 'list[ComPatagonaPricemonitorShareApiShopV3]'
    }

    attribute_map = {
        'id': 'id',
        'vendor_name': 'vendorName',
        'shops': 'shops'
    }

    def __init__(self, id=None, vendor_name=None, shops=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiVendorShopMappingV3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._vendor_name = None
        self._shops = None
        self.discriminator = None

        self.id = id
        self.vendor_name = vendor_name
        self.shops = shops

    @property
    def id(self):
        """Gets the id of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.  # noqa: E501

        Unique identifier of a vendor  # noqa: E501

        :return: The id of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.

        Unique identifier of a vendor  # noqa: E501

        :param id: The id of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def vendor_name(self):
        """Gets the vendor_name of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.  # noqa: E501

        Vendor name  # noqa: E501

        :return: The vendor_name of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.  # noqa: E501
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.

        Vendor name  # noqa: E501

        :param vendor_name: The vendor_name of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and vendor_name is None:  # noqa: E501
            raise ValueError("Invalid value for `vendor_name`, must not be `None`")  # noqa: E501

        self._vendor_name = vendor_name

    @property
    def shops(self):
        """Gets the shops of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.  # noqa: E501

        List of shops associated with the specified vendor  # noqa: E501

        :return: The shops of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.  # noqa: E501
        :rtype: list[ComPatagonaPricemonitorShareApiShopV3]
        """
        return self._shops

    @shops.setter
    def shops(self, shops):
        """Sets the shops of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.

        List of shops associated with the specified vendor  # noqa: E501

        :param shops: The shops of this ComPatagonaPricemonitorShareApiVendorShopMappingV3.  # noqa: E501
        :type: list[ComPatagonaPricemonitorShareApiShopV3]
        """
        if self.local_vars_configuration.client_side_validation and shops is None:  # noqa: E501
            raise ValueError("Invalid value for `shops`, must not be `None`")  # noqa: E501

        self._shops = shops

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiVendorShopMappingV3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiVendorShopMappingV3):
            return True

        return self.to_dict() != other.to_dict()