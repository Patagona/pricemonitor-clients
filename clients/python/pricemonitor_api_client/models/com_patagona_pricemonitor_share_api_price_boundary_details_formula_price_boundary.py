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


class ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary(object):
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
        'price': 'float',
        'formula': 'str',
        'variables': 'list[ComPatagonaPricemonitorShareApiFormulaVariable]'
    }

    attribute_map = {
        'price': 'price',
        'formula': 'formula',
        'variables': 'variables'
    }

    def __init__(self, price=None, formula=None, variables=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._price = None
        self._formula = None
        self._variables = None
        self.discriminator = None

        self.price = price
        self.formula = formula
        self.variables = variables

    @property
    def price(self):
        """Gets the price of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.  # noqa: E501

        The price boundary.  # noqa: E501

        :return: The price of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.

        The price boundary.  # noqa: E501

        :param price: The price of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and price is None:  # noqa: E501
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def formula(self):
        """Gets the formula of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.  # noqa: E501

        The formula which has been used to calculate the price boundary.  # noqa: E501

        :return: The formula of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.  # noqa: E501
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.

        The formula which has been used to calculate the price boundary.  # noqa: E501

        :param formula: The formula of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and formula is None:  # noqa: E501
            raise ValueError("Invalid value for `formula`, must not be `None`")  # noqa: E501

        self._formula = formula

    @property
    def variables(self):
        """Gets the variables of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.  # noqa: E501

        The relevant variables used in the formula.  # noqa: E501

        :return: The variables of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.  # noqa: E501
        :rtype: list[ComPatagonaPricemonitorShareApiFormulaVariable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.

        The relevant variables used in the formula.  # noqa: E501

        :param variables: The variables of this ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary.  # noqa: E501
        :type: list[ComPatagonaPricemonitorShareApiFormulaVariable]
        """
        if self.local_vars_configuration.client_side_validation and variables is None:  # noqa: E501
            raise ValueError("Invalid value for `variables`, must not be `None`")  # noqa: E501

        self._variables = variables

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiPriceBoundaryDetailsFormulaPriceBoundary):
            return True

        return self.to_dict() != other.to_dict()
