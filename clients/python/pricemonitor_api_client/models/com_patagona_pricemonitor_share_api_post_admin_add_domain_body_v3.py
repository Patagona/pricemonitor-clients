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


class ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3(object):
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
        'domain': 'str',
        'name': 'str',
        'offer_sources': 'list[str]'
    }

    attribute_map = {
        'domain': 'domain',
        'name': 'name',
        'offer_sources': 'offerSources'
    }

    def __init__(self, domain=None, name=None, offer_sources=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain = None
        self._name = None
        self._offer_sources = None
        self.discriminator = None

        self.domain = domain
        self.name = name
        self.offer_sources = offer_sources

    @property
    def domain(self):
        """Gets the domain of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.  # noqa: E501

        the domain being added. (Must be unique and non-empty) Allowed domain pattern: \"&lt;domain-name&gt;.&lt;top-level-domain&gt;\". Example:\"google.com\", \"amazon.co.uk\" (valid), \"_google_com\" (invalid). For omnia custom monitoring, the domain name must be prefixed with \"omnia.custom.spidering.\"  # noqa: E501

        :return: The domain of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.

        the domain being added. (Must be unique and non-empty) Allowed domain pattern: \"&lt;domain-name&gt;.&lt;top-level-domain&gt;\". Example:\"google.com\", \"amazon.co.uk\" (valid), \"_google_com\" (invalid). For omnia custom monitoring, the domain name must be prefixed with \"omnia.custom.spidering.\"  # noqa: E501

        :param domain: The domain of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def name(self):
        """Gets the name of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.  # noqa: E501

        display name for the domain in the UI. (Must be unique and non-empty)  # noqa: E501

        :return: The name of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.

        display name for the domain in the UI. (Must be unique and non-empty)  # noqa: E501

        :param name: The name of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def offer_sources(self):
        """Gets the offer_sources of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.  # noqa: E501

        sources of offers on this domain. (Must be non-empty) Allowed sources: \"DEFAULT_MONITORING\", \"CUSTOM_MONITORING\", \"OMNIA_CUSTOM_SPIDERING\", \"PUSH_API\", \"OTHER\" @example domain = \"google.de\", offerSources = Set(\"DEFAULT_MONITORING\")  # noqa: E501

        :return: The offer_sources of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.  # noqa: E501
        :rtype: list[str]
        """
        return self._offer_sources

    @offer_sources.setter
    def offer_sources(self, offer_sources):
        """Sets the offer_sources of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.

        sources of offers on this domain. (Must be non-empty) Allowed sources: \"DEFAULT_MONITORING\", \"CUSTOM_MONITORING\", \"OMNIA_CUSTOM_SPIDERING\", \"PUSH_API\", \"OTHER\" @example domain = \"google.de\", offerSources = Set(\"DEFAULT_MONITORING\")  # noqa: E501

        :param offer_sources: The offer_sources of this ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and offer_sources is None:  # noqa: E501
            raise ValueError("Invalid value for `offer_sources`, must not be `None`")  # noqa: E501

        self._offer_sources = offer_sources

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiPostAdminAddDomainBodyV3):
            return True

        return self.to_dict() != other.to_dict()
