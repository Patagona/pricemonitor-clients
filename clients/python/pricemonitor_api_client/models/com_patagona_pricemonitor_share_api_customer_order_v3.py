# coding: utf-8

"""
    Pricemonitor API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.6712
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pricemonitor_api_client.configuration import Configuration


class ComPatagonaPricemonitorShareApiCustomerOrderV3(object):
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
        'shipping_costs': 'float',
        'order_id': 'str',
        'items': 'list[ComPatagonaPricemonitorShareApiCustomerOrderItemV2]',
        'total_price': 'float',
        'origin': 'str',
        'creation_date': 'datetime',
        'currency': 'str',
        'referrer': 'str'
    }

    attribute_map = {
        'shipping_costs': 'shippingCosts',
        'order_id': 'orderId',
        'items': 'items',
        'total_price': 'totalPrice',
        'origin': 'origin',
        'creation_date': 'creationDate',
        'currency': 'currency',
        'referrer': 'referrer'
    }

    def __init__(self, shipping_costs=None, order_id=None, items=None, total_price=None, origin=None, creation_date=None, currency=None, referrer=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiCustomerOrderV3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._shipping_costs = None
        self._order_id = None
        self._items = None
        self._total_price = None
        self._origin = None
        self._creation_date = None
        self._currency = None
        self._referrer = None
        self.discriminator = None

        self.shipping_costs = shipping_costs
        self.order_id = order_id
        self.items = items
        self.total_price = total_price
        self.origin = origin
        self.creation_date = creation_date
        self.currency = currency
        if referrer is not None:
            self.referrer = referrer

    @property
    def shipping_costs(self):
        """Gets the shipping_costs of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501

        Shipping costs of the order  # noqa: E501

        :return: The shipping_costs of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :rtype: float
        """
        return self._shipping_costs

    @shipping_costs.setter
    def shipping_costs(self, shipping_costs):
        """Sets the shipping_costs of this ComPatagonaPricemonitorShareApiCustomerOrderV3.

        Shipping costs of the order  # noqa: E501

        :param shipping_costs: The shipping_costs of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and shipping_costs is None:  # noqa: E501
            raise ValueError("Invalid value for `shipping_costs`, must not be `None`")  # noqa: E501

        self._shipping_costs = shipping_costs

    @property
    def order_id(self):
        """Gets the order_id of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501

        Unique id of an order. It must mean unique in the contract, not in the pricemonitor.  # noqa: E501

        :return: The order_id of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ComPatagonaPricemonitorShareApiCustomerOrderV3.

        Unique id of an order. It must mean unique in the contract, not in the pricemonitor.  # noqa: E501

        :param order_id: The order_id of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and order_id is None:  # noqa: E501
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def items(self):
        """Gets the items of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501

        List of bought items  # noqa: E501

        :return: The items of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :rtype: list[ComPatagonaPricemonitorShareApiCustomerOrderItemV2]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ComPatagonaPricemonitorShareApiCustomerOrderV3.

        List of bought items  # noqa: E501

        :param items: The items of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :type: list[ComPatagonaPricemonitorShareApiCustomerOrderItemV2]
        """
        if self.local_vars_configuration.client_side_validation and items is None:  # noqa: E501
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def total_price(self):
        """Gets the total_price of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501

        Total price of the order  # noqa: E501

        :return: The total_price of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this ComPatagonaPricemonitorShareApiCustomerOrderV3.

        Total price of the order  # noqa: E501

        :param total_price: The total_price of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_price is None:  # noqa: E501
            raise ValueError("Invalid value for `total_price`, must not be `None`")  # noqa: E501

        self._total_price = total_price

    @property
    def origin(self):
        """Gets the origin of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501

        Origin of an order, e.g. the online shop where the order is placed  # noqa: E501

        :return: The origin of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this ComPatagonaPricemonitorShareApiCustomerOrderV3.

        Origin of an order, e.g. the online shop where the order is placed  # noqa: E501

        :param origin: The origin of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and origin is None:  # noqa: E501
            raise ValueError("Invalid value for `origin`, must not be `None`")  # noqa: E501

        self._origin = origin

    @property
    def creation_date(self):
        """Gets the creation_date of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501

        Date when the order is created  # noqa: E501

        :return: The creation_date of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ComPatagonaPricemonitorShareApiCustomerOrderV3.

        Date when the order is created  # noqa: E501

        :param creation_date: The creation_date of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and creation_date is None:  # noqa: E501
            raise ValueError("Invalid value for `creation_date`, must not be `None`")  # noqa: E501

        self._creation_date = creation_date

    @property
    def currency(self):
        """Gets the currency of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501

        Currency used in the order. ISO 4217 Currency Codes: e.g. EUR  # noqa: E501

        :return: The currency of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ComPatagonaPricemonitorShareApiCustomerOrderV3.

        Currency used in the order. ISO 4217 Currency Codes: e.g. EUR  # noqa: E501

        :param currency: The currency of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def referrer(self):
        """Gets the referrer of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501

        Referrer of an order. Third party (e.g. marketplace) which referred the customer to the online shop  # noqa: E501

        :return: The referrer of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """Sets the referrer of this ComPatagonaPricemonitorShareApiCustomerOrderV3.

        Referrer of an order. Third party (e.g. marketplace) which referred the customer to the online shop  # noqa: E501

        :param referrer: The referrer of this ComPatagonaPricemonitorShareApiCustomerOrderV3.  # noqa: E501
        :type: str
        """

        self._referrer = referrer

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiCustomerOrderV3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiCustomerOrderV3):
            return True

        return self.to_dict() != other.to_dict()