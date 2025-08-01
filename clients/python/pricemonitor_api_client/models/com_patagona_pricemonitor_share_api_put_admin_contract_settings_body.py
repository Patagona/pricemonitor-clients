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


class ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody(object):
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
        'features': 'ComPatagonaPricemonitorShareApiContractFeatures',
        'id': 'float',
        'monitoring_priority': 'int',
        'type': 'str',
        'sid': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'expiration_date': 'expirationDate',
        'portals': 'portals',
        'features': 'features',
        'id': 'id',
        'monitoring_priority': 'monitoringPriority',
        'type': 'type',
        'sid': 'sid',
        'active': 'active'
    }

    def __init__(self, name=None, expiration_date=None, portals=None, features=None, id=None, monitoring_priority=None, type=None, sid=None, active=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._expiration_date = None
        self._portals = None
        self._features = None
        self._id = None
        self._monitoring_priority = None
        self._type = None
        self._sid = None
        self._active = None
        self.discriminator = None

        self.name = name
        if expiration_date is not None:
            self.expiration_date = expiration_date
        self.portals = portals
        self.features = features
        self.id = id
        if monitoring_priority is not None:
            self.monitoring_priority = monitoring_priority
        self.type = type
        self.sid = sid
        self.active = active

    @property
    def name(self):
        """Gets the name of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501


        :return: The name of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.


        :param name: The name of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def expiration_date(self):
        """Gets the expiration_date of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501


        :return: The expiration_date of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.


        :param expiration_date: The expiration_date of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def portals(self):
        """Gets the portals of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501


        :return: The portals of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._portals

    @portals.setter
    def portals(self, portals):
        """Sets the portals of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.


        :param portals: The portals of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and portals is None:  # noqa: E501
            raise ValueError("Invalid value for `portals`, must not be `None`")  # noqa: E501

        self._portals = portals

    @property
    def features(self):
        """Gets the features of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501


        :return: The features of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiContractFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.


        :param features: The features of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiContractFeatures
        """
        if self.local_vars_configuration.client_side_validation and features is None:  # noqa: E501
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def id(self):
        """Gets the id of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501


        :return: The id of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.


        :param id: The id of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def monitoring_priority(self):
        """Gets the monitoring_priority of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501


        :return: The monitoring_priority of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :rtype: int
        """
        return self._monitoring_priority

    @monitoring_priority.setter
    def monitoring_priority(self, monitoring_priority):
        """Sets the monitoring_priority of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.


        :param monitoring_priority: The monitoring_priority of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :type: int
        """

        self._monitoring_priority = monitoring_priority

    @property
    def type(self):
        """Gets the type of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501


        :return: The type of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.


        :param type: The type of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def sid(self):
        """Gets the sid of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501


        :return: The sid of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.


        :param sid: The sid of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sid is None:  # noqa: E501
            raise ValueError("Invalid value for `sid`, must not be `None`")  # noqa: E501

        self._sid = sid

    @property
    def active(self):
        """Gets the active of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501


        :return: The active of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.


        :param active: The active of this ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody.  # noqa: E501
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
        if not isinstance(other, ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiPutAdminContractSettingsBody):
            return True

        return self.to_dict() != other.to_dict()
