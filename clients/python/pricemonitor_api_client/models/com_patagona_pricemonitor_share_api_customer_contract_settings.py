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


class ComPatagonaPricemonitorShareApiCustomerContractSettings(object):
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
        'include_delivery_costs': 'bool',
        'domains': 'list[str]',
        'dynamic_monitoring': 'ComPatagonaPricemonitorShareApiDynamicMonitoringSettings',
        'currency': 'str',
        'image_url_tag': 'str',
        'callbacks': 'ComPatagonaPricemonitorShareApiCallbacks',
        'msrp_tag': 'str',
        'map_tag': 'str'
    }

    attribute_map = {
        'include_delivery_costs': 'includeDeliveryCosts',
        'domains': 'domains',
        'dynamic_monitoring': 'dynamicMonitoring',
        'currency': 'currency',
        'image_url_tag': 'imageUrlTag',
        'callbacks': 'callbacks',
        'msrp_tag': 'msrpTag',
        'map_tag': 'mapTag'
    }

    def __init__(self, include_delivery_costs=None, domains=None, dynamic_monitoring=None, currency='EUR', image_url_tag=None, callbacks=None, msrp_tag=None, map_tag=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiCustomerContractSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._include_delivery_costs = None
        self._domains = None
        self._dynamic_monitoring = None
        self._currency = None
        self._image_url_tag = None
        self._callbacks = None
        self._msrp_tag = None
        self._map_tag = None
        self.discriminator = None

        self.include_delivery_costs = include_delivery_costs
        self.domains = domains
        if dynamic_monitoring is not None:
            self.dynamic_monitoring = dynamic_monitoring
        if currency is not None:
            self.currency = currency
        if image_url_tag is not None:
            self.image_url_tag = image_url_tag
        if callbacks is not None:
            self.callbacks = callbacks
        if msrp_tag is not None:
            self.msrp_tag = msrp_tag
        if map_tag is not None:
            self.map_tag = map_tag

    @property
    def include_delivery_costs(self):
        """Gets the include_delivery_costs of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501


        :return: The include_delivery_costs of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :rtype: bool
        """
        return self._include_delivery_costs

    @include_delivery_costs.setter
    def include_delivery_costs(self, include_delivery_costs):
        """Sets the include_delivery_costs of this ComPatagonaPricemonitorShareApiCustomerContractSettings.


        :param include_delivery_costs: The include_delivery_costs of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and include_delivery_costs is None:  # noqa: E501
            raise ValueError("Invalid value for `include_delivery_costs`, must not be `None`")  # noqa: E501

        self._include_delivery_costs = include_delivery_costs

    @property
    def domains(self):
        """Gets the domains of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501


        :return: The domains of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this ComPatagonaPricemonitorShareApiCustomerContractSettings.


        :param domains: The domains of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and domains is None:  # noqa: E501
            raise ValueError("Invalid value for `domains`, must not be `None`")  # noqa: E501

        self._domains = domains

    @property
    def dynamic_monitoring(self):
        """Gets the dynamic_monitoring of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501


        :return: The dynamic_monitoring of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiDynamicMonitoringSettings
        """
        return self._dynamic_monitoring

    @dynamic_monitoring.setter
    def dynamic_monitoring(self, dynamic_monitoring):
        """Sets the dynamic_monitoring of this ComPatagonaPricemonitorShareApiCustomerContractSettings.


        :param dynamic_monitoring: The dynamic_monitoring of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiDynamicMonitoringSettings
        """

        self._dynamic_monitoring = dynamic_monitoring

    @property
    def currency(self):
        """Gets the currency of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501

        The contract's currency as three letter code  # noqa: E501

        :return: The currency of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ComPatagonaPricemonitorShareApiCustomerContractSettings.

        The contract's currency as three letter code  # noqa: E501

        :param currency: The currency of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def image_url_tag(self):
        """Gets the image_url_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501

        The name of the tag that contains the product image url  # noqa: E501

        :return: The image_url_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :rtype: str
        """
        return self._image_url_tag

    @image_url_tag.setter
    def image_url_tag(self, image_url_tag):
        """Sets the image_url_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.

        The name of the tag that contains the product image url  # noqa: E501

        :param image_url_tag: The image_url_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :type: str
        """

        self._image_url_tag = image_url_tag

    @property
    def callbacks(self):
        """Gets the callbacks of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501


        :return: The callbacks of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiCallbacks
        """
        return self._callbacks

    @callbacks.setter
    def callbacks(self, callbacks):
        """Sets the callbacks of this ComPatagonaPricemonitorShareApiCustomerContractSettings.


        :param callbacks: The callbacks of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiCallbacks
        """

        self._callbacks = callbacks

    @property
    def msrp_tag(self):
        """Gets the msrp_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501

        The name of the tag that contains the manufacturers suggested retail price  # noqa: E501

        :return: The msrp_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :rtype: str
        """
        return self._msrp_tag

    @msrp_tag.setter
    def msrp_tag(self, msrp_tag):
        """Sets the msrp_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.

        The name of the tag that contains the manufacturers suggested retail price  # noqa: E501

        :param msrp_tag: The msrp_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :type: str
        """

        self._msrp_tag = msrp_tag

    @property
    def map_tag(self):
        """Gets the map_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501

        The name of the tag that contains the minimum advertised price  # noqa: E501

        :return: The map_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :rtype: str
        """
        return self._map_tag

    @map_tag.setter
    def map_tag(self, map_tag):
        """Sets the map_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.

        The name of the tag that contains the minimum advertised price  # noqa: E501

        :param map_tag: The map_tag of this ComPatagonaPricemonitorShareApiCustomerContractSettings.  # noqa: E501
        :type: str
        """

        self._map_tag = map_tag

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiCustomerContractSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiCustomerContractSettings):
            return True

        return self.to_dict() != other.to_dict()