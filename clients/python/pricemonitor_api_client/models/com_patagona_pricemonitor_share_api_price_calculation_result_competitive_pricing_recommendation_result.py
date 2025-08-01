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


class ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult(object):
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
        'adjust_to_next_pricier': 'bool',
        'target_position': 'int',
        'include_delivery_costs': 'bool',
        'own_offers': 'list[ComPatagonaPricemonitorShareApiApiOffer]',
        'competitor_offers': 'list[ComPatagonaPricemonitorShareApiApiOffer]',
        'price_gap': 'float',
        'min_price_boundary': 'ComPatagonaPricemonitorShareApiPriceBoundaryDetails',
        'own_delivery_costs': 'float',
        'unit_price_recommendation': 'float',
        'max_price_boundary': 'ComPatagonaPricemonitorShareApiPriceBoundaryDetails',
        'price_gap_unit': 'ComPatagonaPricemonitorShareApiPriceGapUnit',
        'node_id': 'int'
    }

    attribute_map = {
        'adjust_to_next_pricier': 'adjustToNextPricier',
        'target_position': 'targetPosition',
        'include_delivery_costs': 'includeDeliveryCosts',
        'own_offers': 'ownOffers',
        'competitor_offers': 'competitorOffers',
        'price_gap': 'priceGap',
        'min_price_boundary': 'minPriceBoundary',
        'own_delivery_costs': 'ownDeliveryCosts',
        'unit_price_recommendation': 'unitPriceRecommendation',
        'max_price_boundary': 'maxPriceBoundary',
        'price_gap_unit': 'priceGapUnit',
        'node_id': 'nodeId'
    }

    def __init__(self, adjust_to_next_pricier=None, target_position=None, include_delivery_costs=None, own_offers=None, competitor_offers=None, price_gap=None, min_price_boundary=None, own_delivery_costs=None, unit_price_recommendation=None, max_price_boundary=None, price_gap_unit=None, node_id=None, local_vars_configuration=None):  # noqa: E501
        """ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._adjust_to_next_pricier = None
        self._target_position = None
        self._include_delivery_costs = None
        self._own_offers = None
        self._competitor_offers = None
        self._price_gap = None
        self._min_price_boundary = None
        self._own_delivery_costs = None
        self._unit_price_recommendation = None
        self._max_price_boundary = None
        self._price_gap_unit = None
        self._node_id = None
        self.discriminator = None

        self.adjust_to_next_pricier = adjust_to_next_pricier
        self.target_position = target_position
        self.include_delivery_costs = include_delivery_costs
        self.own_offers = own_offers
        self.competitor_offers = competitor_offers
        self.price_gap = price_gap
        self.min_price_boundary = min_price_boundary
        if own_delivery_costs is not None:
            self.own_delivery_costs = own_delivery_costs
        self.unit_price_recommendation = unit_price_recommendation
        self.max_price_boundary = max_price_boundary
        self.price_gap_unit = price_gap_unit
        self.node_id = node_id

    @property
    def adjust_to_next_pricier(self):
        """Gets the adjust_to_next_pricier of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501

        When a target position can't be reached due to the price boundary, the target position gets realigned to the next reachable one (within the price boundary) by this setting.  # noqa: E501

        :return: The adjust_to_next_pricier of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: bool
        """
        return self._adjust_to_next_pricier

    @adjust_to_next_pricier.setter
    def adjust_to_next_pricier(self, adjust_to_next_pricier):
        """Sets the adjust_to_next_pricier of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.

        When a target position can't be reached due to the price boundary, the target position gets realigned to the next reachable one (within the price boundary) by this setting.  # noqa: E501

        :param adjust_to_next_pricier: The adjust_to_next_pricier of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and adjust_to_next_pricier is None:  # noqa: E501
            raise ValueError("Invalid value for `adjust_to_next_pricier`, must not be `None`")  # noqa: E501

        self._adjust_to_next_pricier = adjust_to_next_pricier

    @property
    def target_position(self):
        """Gets the target_position of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501

        The target position which has been considered.  # noqa: E501

        :return: The target_position of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: int
        """
        return self._target_position

    @target_position.setter
    def target_position(self, target_position):
        """Sets the target_position of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.

        The target position which has been considered.  # noqa: E501

        :param target_position: The target_position of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and target_position is None:  # noqa: E501
            raise ValueError("Invalid value for `target_position`, must not be `None`")  # noqa: E501

        self._target_position = target_position

    @property
    def include_delivery_costs(self):
        """Gets the include_delivery_costs of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501

        Determines if the delivery costs should be included in the price calculation.  # noqa: E501

        :return: The include_delivery_costs of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: bool
        """
        return self._include_delivery_costs

    @include_delivery_costs.setter
    def include_delivery_costs(self, include_delivery_costs):
        """Sets the include_delivery_costs of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.

        Determines if the delivery costs should be included in the price calculation.  # noqa: E501

        :param include_delivery_costs: The include_delivery_costs of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and include_delivery_costs is None:  # noqa: E501
            raise ValueError("Invalid value for `include_delivery_costs`, must not be `None`")  # noqa: E501

        self._include_delivery_costs = include_delivery_costs

    @property
    def own_offers(self):
        """Gets the own_offers of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501

        The own offers which have been considered for the price calculation.  # noqa: E501

        :return: The own_offers of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: list[ComPatagonaPricemonitorShareApiApiOffer]
        """
        return self._own_offers

    @own_offers.setter
    def own_offers(self, own_offers):
        """Sets the own_offers of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.

        The own offers which have been considered for the price calculation.  # noqa: E501

        :param own_offers: The own_offers of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: list[ComPatagonaPricemonitorShareApiApiOffer]
        """
        if self.local_vars_configuration.client_side_validation and own_offers is None:  # noqa: E501
            raise ValueError("Invalid value for `own_offers`, must not be `None`")  # noqa: E501

        self._own_offers = own_offers

    @property
    def competitor_offers(self):
        """Gets the competitor_offers of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501

        The offers of the competitors which have been considered for the price calculation.  # noqa: E501

        :return: The competitor_offers of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: list[ComPatagonaPricemonitorShareApiApiOffer]
        """
        return self._competitor_offers

    @competitor_offers.setter
    def competitor_offers(self, competitor_offers):
        """Sets the competitor_offers of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.

        The offers of the competitors which have been considered for the price calculation.  # noqa: E501

        :param competitor_offers: The competitor_offers of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: list[ComPatagonaPricemonitorShareApiApiOffer]
        """
        if self.local_vars_configuration.client_side_validation and competitor_offers is None:  # noqa: E501
            raise ValueError("Invalid value for `competitor_offers`, must not be `None`")  # noqa: E501

        self._competitor_offers = competitor_offers

    @property
    def price_gap(self):
        """Gets the price_gap of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501

        The price gap which has been considered.<br> - A positive value means to underbid the target position.<br> - A zero value means to match the target position.<br> - A negative value means to overbid the target position.  # noqa: E501

        :return: The price_gap of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: float
        """
        return self._price_gap

    @price_gap.setter
    def price_gap(self, price_gap):
        """Sets the price_gap of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.

        The price gap which has been considered.<br> - A positive value means to underbid the target position.<br> - A zero value means to match the target position.<br> - A negative value means to overbid the target position.  # noqa: E501

        :param price_gap: The price_gap of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and price_gap is None:  # noqa: E501
            raise ValueError("Invalid value for `price_gap`, must not be `None`")  # noqa: E501

        self._price_gap = price_gap

    @property
    def min_price_boundary(self):
        """Gets the min_price_boundary of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501


        :return: The min_price_boundary of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiPriceBoundaryDetails
        """
        return self._min_price_boundary

    @min_price_boundary.setter
    def min_price_boundary(self, min_price_boundary):
        """Sets the min_price_boundary of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.


        :param min_price_boundary: The min_price_boundary of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiPriceBoundaryDetails
        """
        if self.local_vars_configuration.client_side_validation and min_price_boundary is None:  # noqa: E501
            raise ValueError("Invalid value for `min_price_boundary`, must not be `None`")  # noqa: E501

        self._min_price_boundary = min_price_boundary

    @property
    def own_delivery_costs(self):
        """Gets the own_delivery_costs of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501

        The own delivery costs which have been considered. Only relevant if 'includeDeliveryCosts' is set to true.  # noqa: E501

        :return: The own_delivery_costs of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: float
        """
        return self._own_delivery_costs

    @own_delivery_costs.setter
    def own_delivery_costs(self, own_delivery_costs):
        """Sets the own_delivery_costs of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.

        The own delivery costs which have been considered. Only relevant if 'includeDeliveryCosts' is set to true.  # noqa: E501

        :param own_delivery_costs: The own_delivery_costs of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: float
        """

        self._own_delivery_costs = own_delivery_costs

    @property
    def unit_price_recommendation(self):
        """Gets the unit_price_recommendation of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501

        The calculated price recommendation.  # noqa: E501

        :return: The unit_price_recommendation of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: float
        """
        return self._unit_price_recommendation

    @unit_price_recommendation.setter
    def unit_price_recommendation(self, unit_price_recommendation):
        """Sets the unit_price_recommendation of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.

        The calculated price recommendation.  # noqa: E501

        :param unit_price_recommendation: The unit_price_recommendation of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and unit_price_recommendation is None:  # noqa: E501
            raise ValueError("Invalid value for `unit_price_recommendation`, must not be `None`")  # noqa: E501

        self._unit_price_recommendation = unit_price_recommendation

    @property
    def max_price_boundary(self):
        """Gets the max_price_boundary of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501


        :return: The max_price_boundary of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiPriceBoundaryDetails
        """
        return self._max_price_boundary

    @max_price_boundary.setter
    def max_price_boundary(self, max_price_boundary):
        """Sets the max_price_boundary of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.


        :param max_price_boundary: The max_price_boundary of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiPriceBoundaryDetails
        """
        if self.local_vars_configuration.client_side_validation and max_price_boundary is None:  # noqa: E501
            raise ValueError("Invalid value for `max_price_boundary`, must not be `None`")  # noqa: E501

        self._max_price_boundary = max_price_boundary

    @property
    def price_gap_unit(self):
        """Gets the price_gap_unit of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501


        :return: The price_gap_unit of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: ComPatagonaPricemonitorShareApiPriceGapUnit
        """
        return self._price_gap_unit

    @price_gap_unit.setter
    def price_gap_unit(self, price_gap_unit):
        """Sets the price_gap_unit of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.


        :param price_gap_unit: The price_gap_unit of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: ComPatagonaPricemonitorShareApiPriceGapUnit
        """
        if self.local_vars_configuration.client_side_validation and price_gap_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `price_gap_unit`, must not be `None`")  # noqa: E501

        self._price_gap_unit = price_gap_unit

    @property
    def node_id(self):
        """Gets the node_id of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501

        The ID of the node which calculated the price.  # noqa: E501

        :return: The node_id of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :rtype: int
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.

        The ID of the node which calculated the price.  # noqa: E501

        :param node_id: The node_id of this ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and node_id is None:  # noqa: E501
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

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
        if not isinstance(other, ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComPatagonaPricemonitorShareApiPriceCalculationResultCompetitivePricingRecommendationResult):
            return True

        return self.to_dict() != other.to_dict()
