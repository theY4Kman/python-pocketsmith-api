# coding: utf-8

"""
    PocketSmith

    The public PocketSmith API  # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: api@pocketsmith.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pocketsmith.configuration import Configuration


class Period(object):
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
        'actual_amount': 'float',
        'current': 'bool',
        'end_date': 'date',
        'forecast_amount': 'float',
        'over_budget': 'bool',
        'over_by': 'float',
        'percentage_used': 'float',
        'refund_amound': 'float',
        'start_date': 'date',
        'under_budget': 'bool',
        'under_by': 'float'
    }

    attribute_map = {
        'actual_amount': 'actual_amount',
        'current': 'current',
        'end_date': 'end_date',
        'forecast_amount': 'forecast_amount',
        'over_budget': 'over_budget',
        'over_by': 'over_by',
        'percentage_used': 'percentage_used',
        'refund_amound': 'refund_amound',
        'start_date': 'start_date',
        'under_budget': 'under_budget',
        'under_by': 'under_by'
    }

    def __init__(self, actual_amount=None, current=None, end_date=None, forecast_amount=None, over_budget=None, over_by=None, percentage_used=None, refund_amound=None, start_date=None, under_budget=None, under_by=None, local_vars_configuration=None):  # noqa: E501
        """Period - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._actual_amount = None
        self._current = None
        self._end_date = None
        self._forecast_amount = None
        self._over_budget = None
        self._over_by = None
        self._percentage_used = None
        self._refund_amound = None
        self._start_date = None
        self._under_budget = None
        self._under_by = None
        self.discriminator = None

        if actual_amount is not None:
            self.actual_amount = actual_amount
        if current is not None:
            self.current = current
        if end_date is not None:
            self.end_date = end_date
        if forecast_amount is not None:
            self.forecast_amount = forecast_amount
        if over_budget is not None:
            self.over_budget = over_budget
        if over_by is not None:
            self.over_by = over_by
        if percentage_used is not None:
            self.percentage_used = percentage_used
        if refund_amound is not None:
            self.refund_amound = refund_amound
        if start_date is not None:
            self.start_date = start_date
        if under_budget is not None:
            self.under_budget = under_budget
        if under_by is not None:
            self.under_by = under_by

    @property
    def actual_amount(self):
        """Gets the actual_amount of this Period.  # noqa: E501

        The sum of all actuals (transactions) in the period.  # noqa: E501

        :return: The actual_amount of this Period.  # noqa: E501
        :rtype: float
        """
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, actual_amount):
        """Sets the actual_amount of this Period.

        The sum of all actuals (transactions) in the period.  # noqa: E501

        :param actual_amount: The actual_amount of this Period.  # noqa: E501
        :type: float
        """

        self._actual_amount = actual_amount

    @property
    def current(self):
        """Gets the current of this Period.  # noqa: E501

        Whether this period is current, such that the current date (in the user's time zone) falls within the date range.  # noqa: E501

        :return: The current of this Period.  # noqa: E501
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this Period.

        Whether this period is current, such that the current date (in the user's time zone) falls within the date range.  # noqa: E501

        :param current: The current of this Period.  # noqa: E501
        :type: bool
        """

        self._current = current

    @property
    def end_date(self):
        """Gets the end_date of this Period.  # noqa: E501

        The end date of the period.  # noqa: E501

        :return: The end_date of this Period.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Period.

        The end date of the period.  # noqa: E501

        :param end_date: The end_date of this Period.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def forecast_amount(self):
        """Gets the forecast_amount of this Period.  # noqa: E501

        The sum of all forecast sources (budget events) in the period, for comparison against the actual amount.  # noqa: E501

        :return: The forecast_amount of this Period.  # noqa: E501
        :rtype: float
        """
        return self._forecast_amount

    @forecast_amount.setter
    def forecast_amount(self, forecast_amount):
        """Sets the forecast_amount of this Period.

        The sum of all forecast sources (budget events) in the period, for comparison against the actual amount.  # noqa: E501

        :param forecast_amount: The forecast_amount of this Period.  # noqa: E501
        :type: float
        """

        self._forecast_amount = forecast_amount

    @property
    def over_budget(self):
        """Gets the over_budget of this Period.  # noqa: E501

        Whether the budget has been exceeded in the period.  # noqa: E501

        :return: The over_budget of this Period.  # noqa: E501
        :rtype: bool
        """
        return self._over_budget

    @over_budget.setter
    def over_budget(self, over_budget):
        """Sets the over_budget of this Period.

        Whether the budget has been exceeded in the period.  # noqa: E501

        :param over_budget: The over_budget of this Period.  # noqa: E501
        :type: bool
        """

        self._over_budget = over_budget

    @property
    def over_by(self):
        """Gets the over_by of this Period.  # noqa: E501

        How much the budget has been exceeded by in the period.  # noqa: E501

        :return: The over_by of this Period.  # noqa: E501
        :rtype: float
        """
        return self._over_by

    @over_by.setter
    def over_by(self, over_by):
        """Sets the over_by of this Period.

        How much the budget has been exceeded by in the period.  # noqa: E501

        :param over_by: The over_by of this Period.  # noqa: E501
        :type: float
        """

        self._over_by = over_by

    @property
    def percentage_used(self):
        """Gets the percentage_used of this Period.  # noqa: E501

        The percentage of the budget that has been used in the period.  # noqa: E501

        :return: The percentage_used of this Period.  # noqa: E501
        :rtype: float
        """
        return self._percentage_used

    @percentage_used.setter
    def percentage_used(self, percentage_used):
        """Sets the percentage_used of this Period.

        The percentage of the budget that has been used in the period.  # noqa: E501

        :param percentage_used: The percentage_used of this Period.  # noqa: E501
        :type: float
        """

        self._percentage_used = percentage_used

    @property
    def refund_amound(self):
        """Gets the refund_amound of this Period.  # noqa: E501

        This attribute tracks the amount that has been refunded or deducted to the actual amount. When a category is set to \"always expense\", any credit transactions are treated as refunds and when set to \"always income\", any debit transactions are treated as deductions.  # noqa: E501

        :return: The refund_amound of this Period.  # noqa: E501
        :rtype: float
        """
        return self._refund_amound

    @refund_amound.setter
    def refund_amound(self, refund_amound):
        """Sets the refund_amound of this Period.

        This attribute tracks the amount that has been refunded or deducted to the actual amount. When a category is set to \"always expense\", any credit transactions are treated as refunds and when set to \"always income\", any debit transactions are treated as deductions.  # noqa: E501

        :param refund_amound: The refund_amound of this Period.  # noqa: E501
        :type: float
        """

        self._refund_amound = refund_amound

    @property
    def start_date(self):
        """Gets the start_date of this Period.  # noqa: E501

        The start date of the period.  # noqa: E501

        :return: The start_date of this Period.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Period.

        The start date of the period.  # noqa: E501

        :param start_date: The start_date of this Period.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def under_budget(self):
        """Gets the under_budget of this Period.  # noqa: E501

        Whether the budget has not been exceeded in the period.  # noqa: E501

        :return: The under_budget of this Period.  # noqa: E501
        :rtype: bool
        """
        return self._under_budget

    @under_budget.setter
    def under_budget(self, under_budget):
        """Sets the under_budget of this Period.

        Whether the budget has not been exceeded in the period.  # noqa: E501

        :param under_budget: The under_budget of this Period.  # noqa: E501
        :type: bool
        """

        self._under_budget = under_budget

    @property
    def under_by(self):
        """Gets the under_by of this Period.  # noqa: E501

        How much there is left in the budget for the period.  # noqa: E501

        :return: The under_by of this Period.  # noqa: E501
        :rtype: float
        """
        return self._under_by

    @under_by.setter
    def under_by(self, under_by):
        """Sets the under_by of this Period.

        How much there is left in the budget for the period.  # noqa: E501

        :param under_by: The under_by of this Period.  # noqa: E501
        :type: float
        """

        self._under_by = under_by

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
        if not isinstance(other, Period):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Period):
            return True

        return self.to_dict() != other.to_dict()