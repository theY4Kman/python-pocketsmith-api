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


class BudgetAnalysis(object):
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
        'average_actual_amount': 'float',
        'average_forecast_amount': 'float',
        'end_date': 'date',
        'currency_code': 'str',
        'periods': 'list[Period]',
        'start_date': 'date',
        'total_actual_amount': 'float',
        'total_forecast_amount': 'float',
        'total_over_by': 'float',
        'total_under_by': 'float'
    }

    attribute_map = {
        'average_actual_amount': 'average_actual_amount',
        'average_forecast_amount': 'average_forecast_amount',
        'end_date': 'end_date',
        'currency_code': 'currency_code',
        'periods': 'periods',
        'start_date': 'start_date',
        'total_actual_amount': 'total_actual_amount',
        'total_forecast_amount': 'total_forecast_amount',
        'total_over_by': 'total_over_by',
        'total_under_by': 'total_under_by'
    }

    def __init__(self, average_actual_amount=None, average_forecast_amount=None, end_date=None, currency_code=None, periods=None, start_date=None, total_actual_amount=None, total_forecast_amount=None, total_over_by=None, total_under_by=None, local_vars_configuration=None):  # noqa: E501
        """BudgetAnalysis - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._average_actual_amount = None
        self._average_forecast_amount = None
        self._end_date = None
        self._currency_code = None
        self._periods = None
        self._start_date = None
        self._total_actual_amount = None
        self._total_forecast_amount = None
        self._total_over_by = None
        self._total_under_by = None
        self.discriminator = None

        if average_actual_amount is not None:
            self.average_actual_amount = average_actual_amount
        if average_forecast_amount is not None:
            self.average_forecast_amount = average_forecast_amount
        if end_date is not None:
            self.end_date = end_date
        if currency_code is not None:
            self.currency_code = currency_code
        if periods is not None:
            self.periods = periods
        if start_date is not None:
            self.start_date = start_date
        if total_actual_amount is not None:
            self.total_actual_amount = total_actual_amount
        if total_forecast_amount is not None:
            self.total_forecast_amount = total_forecast_amount
        if total_over_by is not None:
            self.total_over_by = total_over_by
        if total_under_by is not None:
            self.total_under_by = total_under_by

    @property
    def average_actual_amount(self):
        """Gets the average_actual_amount of this BudgetAnalysis.  # noqa: E501

        The average actual (transactions) amount across all periods.  # noqa: E501

        :return: The average_actual_amount of this BudgetAnalysis.  # noqa: E501
        :rtype: float
        """
        return self._average_actual_amount

    @average_actual_amount.setter
    def average_actual_amount(self, average_actual_amount):
        """Sets the average_actual_amount of this BudgetAnalysis.

        The average actual (transactions) amount across all periods.  # noqa: E501

        :param average_actual_amount: The average_actual_amount of this BudgetAnalysis.  # noqa: E501
        :type: float
        """

        self._average_actual_amount = average_actual_amount

    @property
    def average_forecast_amount(self):
        """Gets the average_forecast_amount of this BudgetAnalysis.  # noqa: E501

        The average budgeted amount across all periods.  # noqa: E501

        :return: The average_forecast_amount of this BudgetAnalysis.  # noqa: E501
        :rtype: float
        """
        return self._average_forecast_amount

    @average_forecast_amount.setter
    def average_forecast_amount(self, average_forecast_amount):
        """Sets the average_forecast_amount of this BudgetAnalysis.

        The average budgeted amount across all periods.  # noqa: E501

        :param average_forecast_amount: The average_forecast_amount of this BudgetAnalysis.  # noqa: E501
        :type: float
        """

        self._average_forecast_amount = average_forecast_amount

    @property
    def end_date(self):
        """Gets the end_date of this BudgetAnalysis.  # noqa: E501

        The end date of the budget analysis.  # noqa: E501

        :return: The end_date of this BudgetAnalysis.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this BudgetAnalysis.

        The end date of the budget analysis.  # noqa: E501

        :param end_date: The end_date of this BudgetAnalysis.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def currency_code(self):
        """Gets the currency_code of this BudgetAnalysis.  # noqa: E501

        The currency code for this BudgetAnalysis.  # noqa: E501

        :return: The currency_code of this BudgetAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this BudgetAnalysis.

        The currency code for this BudgetAnalysis.  # noqa: E501

        :param currency_code: The currency_code of this BudgetAnalysis.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def periods(self):
        """Gets the periods of this BudgetAnalysis.  # noqa: E501

        The period analyses that this budget analysis comprises.  # noqa: E501

        :return: The periods of this BudgetAnalysis.  # noqa: E501
        :rtype: list[Period]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this BudgetAnalysis.

        The period analyses that this budget analysis comprises.  # noqa: E501

        :param periods: The periods of this BudgetAnalysis.  # noqa: E501
        :type: list[Period]
        """

        self._periods = periods

    @property
    def start_date(self):
        """Gets the start_date of this BudgetAnalysis.  # noqa: E501

        The start date of the budget analysis.  # noqa: E501

        :return: The start_date of this BudgetAnalysis.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this BudgetAnalysis.

        The start date of the budget analysis.  # noqa: E501

        :param start_date: The start_date of this BudgetAnalysis.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def total_actual_amount(self):
        """Gets the total_actual_amount of this BudgetAnalysis.  # noqa: E501

        The total actual (transactions) amount across all periods.  # noqa: E501

        :return: The total_actual_amount of this BudgetAnalysis.  # noqa: E501
        :rtype: float
        """
        return self._total_actual_amount

    @total_actual_amount.setter
    def total_actual_amount(self, total_actual_amount):
        """Sets the total_actual_amount of this BudgetAnalysis.

        The total actual (transactions) amount across all periods.  # noqa: E501

        :param total_actual_amount: The total_actual_amount of this BudgetAnalysis.  # noqa: E501
        :type: float
        """

        self._total_actual_amount = total_actual_amount

    @property
    def total_forecast_amount(self):
        """Gets the total_forecast_amount of this BudgetAnalysis.  # noqa: E501

        The total budgeted amount across all periods.  # noqa: E501

        :return: The total_forecast_amount of this BudgetAnalysis.  # noqa: E501
        :rtype: float
        """
        return self._total_forecast_amount

    @total_forecast_amount.setter
    def total_forecast_amount(self, total_forecast_amount):
        """Sets the total_forecast_amount of this BudgetAnalysis.

        The total budgeted amount across all periods.  # noqa: E501

        :param total_forecast_amount: The total_forecast_amount of this BudgetAnalysis.  # noqa: E501
        :type: float
        """

        self._total_forecast_amount = total_forecast_amount

    @property
    def total_over_by(self):
        """Gets the total_over_by of this BudgetAnalysis.  # noqa: E501

        The total amount the budget was exceeded across all periods.  # noqa: E501

        :return: The total_over_by of this BudgetAnalysis.  # noqa: E501
        :rtype: float
        """
        return self._total_over_by

    @total_over_by.setter
    def total_over_by(self, total_over_by):
        """Sets the total_over_by of this BudgetAnalysis.

        The total amount the budget was exceeded across all periods.  # noqa: E501

        :param total_over_by: The total_over_by of this BudgetAnalysis.  # noqa: E501
        :type: float
        """

        self._total_over_by = total_over_by

    @property
    def total_under_by(self):
        """Gets the total_under_by of this BudgetAnalysis.  # noqa: E501

        The total amount the budget was under by across all periods.  # noqa: E501

        :return: The total_under_by of this BudgetAnalysis.  # noqa: E501
        :rtype: float
        """
        return self._total_under_by

    @total_under_by.setter
    def total_under_by(self, total_under_by):
        """Sets the total_under_by of this BudgetAnalysis.

        The total amount the budget was under by across all periods.  # noqa: E501

        :param total_under_by: The total_under_by of this BudgetAnalysis.  # noqa: E501
        :type: float
        """

        self._total_under_by = total_under_by

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
        if not isinstance(other, BudgetAnalysis):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BudgetAnalysis):
            return True

        return self.to_dict() != other.to_dict()
