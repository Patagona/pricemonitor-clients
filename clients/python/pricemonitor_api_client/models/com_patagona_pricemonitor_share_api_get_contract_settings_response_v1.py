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


class ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1(object):
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
        'name': 'str',
        'expiration_date': 'datetime',
        'portals': 'list[str]',
        'include_delivery_costs': 'bool',
        'features': 'ComPatagonaPricemonitorShareApiContractFeatures',
        'image_tag': 'str',
        'company': 'str',
        'id': 'float',
        'monitoring_priority': 'int',
        'currency': 'str',
        'type': 'str',
        'sid': 'str',
        'msrp_tag': 'str',
        'map_tag': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'expiration_date': 'expirationDate',
        'portals': 'portals',
        'include_delivery_costs': 'includeDeliveryCosts',
        'features': 'features',
        'image_tag': 'imageTag',
        'company': 'company',
        'id': 'id',
        'monitoring_priority': 'monitoringPriority',
        'currency': 'currency',
        'type': 'type',
        'sid': 'sid',
        'msrp_tag': 'msrpTag',
        'map_tag': 'mapTag',
        'active': 'active'
    }

    def __init__(self, name=None, expiration_date=None, portals=None, include_delivery_costs=None, features=None, image_tag=None, company=None, id=None, monitoring_priority=None, currency=None, type=None, sid=None, msrp_tag=None, map_tag=None, active=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._expiration_date = None
        self._portals = None
        self._include_delivery_costs = None
        self._features = None
        self._image_tag = None
        self._company = None
        self._id = None
        self._monitoring_priority = None
        self._currency = None
        self._type = None
        self._sid = None
        self._msrp_tag = None
        self._map_tag = None
        self._active = None
        self.discriminator = None

        self.name = name
        if expiration_date is not None:
            self.expiration_date = expiration_date
        self.portals = portals
        self.include_delivery_costs = include_delivery_costs
        self.features = features
        if image_tag is not None:
            self.image_tag = image_tag
        self.company = company
        self.id = id
        self.monitoring_priority = monitoring_priority
        self.currency = currency
        self.type = type
        self.sid = sid
        if msrp_tag is not None:
            self.msrp_tag = msrp_tag
        if map_tag is not None:
            self.map_tag = map_tag
        self.active = active

    @property
    def name(self):
        """Gets the name of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The name of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param name: The name of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def expiration_date(self):
        """Gets the expiration_date of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The expiration_date of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param expiration_date: The expiration_date of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def portals(self):
        """Gets the portals of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The portals of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._portals

    @portals.setter
    def portals(self, portals):
        """Sets the portals of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param portals: The portals of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and portals is None:  # noqa: E501
            raise ValueError("Invalid value for `portals`, must not be `None`")  # noqa: E501

        self._portals = portals

    @property
    def include_delivery_costs(self):
        """Gets the include_delivery_costs of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The include_delivery_costs of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: bool
        """
        return self._include_delivery_costs

    @include_delivery_costs.setter
    def include_delivery_costs(self, include_delivery_costs):
        """Sets the include_delivery_costs of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param include_delivery_costs: The include_delivery_costs of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and include_delivery_costs is None:  # noqa: E501
            raise ValueError("Invalid value for `include_delivery_costs`, must not be `None`")  # noqa: E501

        self._include_delivery_costs = include_delivery_costs

    @property
    def features(self):
        """Gets the features of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The features of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiContractFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param features: The features of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiContractFeatures
        """
        if self.local_vars_configuration.client_side_validation and features is None:  # noqa: E501
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def image_tag(self):
        """Gets the image_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501

        The name of the tag that contains the product image url  # noqa: E501

        :return: The image_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.

        The name of the tag that contains the product image url  # noqa: E501

        :param image_tag: The image_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def company(self):
        """Gets the company of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The company of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param company: The company of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and company is None:  # noqa: E501
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

    @property
    def id(self):
        """Gets the id of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The id of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param id: The id of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def monitoring_priority(self):
        """Gets the monitoring_priority of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501

        Priority of the contract in the monitoring queue  # noqa: E501

        :return: The monitoring_priority of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: int
        """
        return self._monitoring_priority

    @monitoring_priority.setter
    def monitoring_priority(self, monitoring_priority):
        """Sets the monitoring_priority of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.

        Priority of the contract in the monitoring queue  # noqa: E501

        :param monitoring_priority: The monitoring_priority of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and monitoring_priority is None:  # noqa: E501
            raise ValueError("Invalid value for `monitoring_priority`, must not be `None`")  # noqa: E501

        self._monitoring_priority = monitoring_priority

    @property
    def currency(self):
        """Gets the currency of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501

        The contract's currency as three letter code  # noqa: E501

        :return: The currency of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.

        The contract's currency as three letter code  # noqa: E501

        :param currency: The currency of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def type(self):
        """Gets the type of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The type of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param type: The type of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def sid(self):
        """Gets the sid of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The sid of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param sid: The sid of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sid is None:  # noqa: E501
            raise ValueError("Invalid value for `sid`, must not be `None`")  # noqa: E501

        self._sid = sid

    @property
    def msrp_tag(self):
        """Gets the msrp_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501

        The name of the tag that contains the manufacturers suggested retail price  # noqa: E501

        :return: The msrp_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: str
        """
        return self._msrp_tag

    @msrp_tag.setter
    def msrp_tag(self, msrp_tag):
        """Sets the msrp_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.

        The name of the tag that contains the manufacturers suggested retail price  # noqa: E501

        :param msrp_tag: The msrp_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: str
        """

        self._msrp_tag = msrp_tag

    @property
    def map_tag(self):
        """Gets the map_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501

        The name of the tag that contains the minimum advertised price  # noqa: E501

        :return: The map_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: str
        """
        return self._map_tag

    @map_tag.setter
    def map_tag(self, map_tag):
        """Sets the map_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.

        The name of the tag that contains the minimum advertised price  # noqa: E501

        :param map_tag: The map_tag of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: str
        """

        self._map_tag = map_tag

    @property
    def active(self):
        """Gets the active of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501


        :return: The active of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.


        :param active: The active of this ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiGetContractSettingsResponseV1):
            return True

        return self.to_dict() != other.to_dict()
