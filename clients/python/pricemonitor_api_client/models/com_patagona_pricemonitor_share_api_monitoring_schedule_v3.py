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


class ComPatagonaPricemonitorShareApiMonitoringScheduleV3(object):
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
        'product_query': 'ComPatagonaPricemonitorShareApiQuery',
        'quota': 'float',
        'unfulfilled_only': 'bool',
        'id': 'float',
        'schedule': 'str',
        'scheduler_job_id': 'str'
    }

    attribute_map = {
        'product_query': 'productQuery',
        'quota': 'quota',
        'unfulfilled_only': 'unfulfilledOnly',
        'id': 'id',
        'schedule': 'schedule',
        'scheduler_job_id': 'schedulerJobId'
    }

    def __init__(self, product_query=None, quota=None, unfulfilled_only=None, id=None, schedule=None, scheduler_job_id=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiMonitoringScheduleV3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._product_query = None
        self._quota = None
        self._unfulfilled_only = None
        self._id = None
        self._schedule = None
        self._scheduler_job_id = None
        self.discriminator = None

        if product_query is not None:
            self.product_query = product_query
        self.quota = quota
        self.unfulfilled_only = unfulfilled_only
        self.id = id
        self.schedule = schedule
        self.scheduler_job_id = scheduler_job_id

    @property
    def product_query(self):
        """Gets the product_query of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501


        :return: The product_query of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiQuery
        """
        return self._product_query

    @product_query.setter
    def product_query(self, product_query):
        """Sets the product_query of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.


        :param product_query: The product_query of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiQuery
        """

        self._product_query = product_query

    @property
    def quota(self):
        """Gets the quota of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501

        Defines how many products should get monitored. Default to 1.0 which means that all products are monitored. Allowed values: 0.0 < quota <= 1.0  # noqa: E501

        :return: The quota of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :rtype: float
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.

        Defines how many products should get monitored. Default to 1.0 which means that all products are monitored. Allowed values: 0.0 < quota <= 1.0  # noqa: E501

        :param quota: The quota of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and quota is None:  # noqa: E501
            raise ValueError("Invalid value for `quota`, must not be `None`")  # noqa: E501

        self._quota = quota

    @property
    def unfulfilled_only(self):
        """Gets the unfulfilled_only of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501

        When it's set to true, then the monitoring considers only products on domains where no offers are found within 24h. Default false.  # noqa: E501

        :return: The unfulfilled_only of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :rtype: bool
        """
        return self._unfulfilled_only

    @unfulfilled_only.setter
    def unfulfilled_only(self, unfulfilled_only):
        """Sets the unfulfilled_only of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.

        When it's set to true, then the monitoring considers only products on domains where no offers are found within 24h. Default false.  # noqa: E501

        :param unfulfilled_only: The unfulfilled_only of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and unfulfilled_only is None:  # noqa: E501
            raise ValueError("Invalid value for `unfulfilled_only`, must not be `None`")  # noqa: E501

        self._unfulfilled_only = unfulfilled_only

    @property
    def id(self):
        """Gets the id of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501

        Id that uniquely identifies a monitoring schedule.  # noqa: E501

        :return: The id of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.

        Id that uniquely identifies a monitoring schedule.  # noqa: E501

        :param id: The id of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def schedule(self):
        """Gets the schedule of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501

        Only valid CRON expressions are allowed. See Cron spec [[https://www.alonsodomin.me/cron4s/userguide/index.html]].  # noqa: E501

        :return: The schedule of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.

        Only valid CRON expressions are allowed. See Cron spec [[https://www.alonsodomin.me/cron4s/userguide/index.html]].  # noqa: E501

        :param schedule: The schedule of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and schedule is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def scheduler_job_id(self):
        """Gets the scheduler_job_id of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501

        Internal job id used by the scheduler.  # noqa: E501

        :return: The scheduler_job_id of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :rtype: str
        """
        return self._scheduler_job_id

    @scheduler_job_id.setter
    def scheduler_job_id(self, scheduler_job_id):
        """Sets the scheduler_job_id of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.

        Internal job id used by the scheduler.  # noqa: E501

        :param scheduler_job_id: The scheduler_job_id of this ComPatagonaPricemonitorShareApiMonitoringScheduleV3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scheduler_job_id is None:  # noqa: E501
            raise ValueError("Invalid value for `scheduler_job_id`, must not be `None`")  # noqa: E501

        self._scheduler_job_id = scheduler_job_id

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiMonitoringScheduleV3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiMonitoringScheduleV3):
            return True

        return self.to_dict() != other.to_dict()