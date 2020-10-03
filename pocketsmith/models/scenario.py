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


class Scenario(object):
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
        'achieve_date': 'str',
        'closing_balance': 'float',
        'closing_balance_date': 'date',
        'created_at': 'datetime',
        'current_balance': 'float',
        'current_balance_date': 'date',
        'description': 'str',
        'id': 'int',
        'interest_rate': 'float',
        'interest_rate_repeat_id': 'int',
        'maximum_value': 'float',
        'minimum_value': 'float',
        'starting_balance': 'float',
        'starting_balance_date': 'date',
        'title': 'str',
        'type': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'achieve_date': 'achieve_date',
        'closing_balance': 'closing_balance',
        'closing_balance_date': 'closing_balance_date',
        'created_at': 'created_at',
        'current_balance': 'current_balance',
        'current_balance_date': 'current_balance_date',
        'description': 'description',
        'id': 'id',
        'interest_rate': 'interest_rate',
        'interest_rate_repeat_id': 'interest_rate_repeat_id',
        'maximum_value': 'maximum-value',
        'minimum_value': 'minimum-value',
        'starting_balance': 'starting_balance',
        'starting_balance_date': 'starting_balance_date',
        'title': 'title',
        'type': 'type',
        'updated_at': 'updated_at'
    }

    def __init__(self, achieve_date=None, closing_balance=None, closing_balance_date=None, created_at=None, current_balance=None, current_balance_date=None, description=None, id=None, interest_rate=None, interest_rate_repeat_id=None, maximum_value=None, minimum_value=None, starting_balance=None, starting_balance_date=None, title=None, type=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Scenario - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._achieve_date = None
        self._closing_balance = None
        self._closing_balance_date = None
        self._created_at = None
        self._current_balance = None
        self._current_balance_date = None
        self._description = None
        self._id = None
        self._interest_rate = None
        self._interest_rate_repeat_id = None
        self._maximum_value = None
        self._minimum_value = None
        self._starting_balance = None
        self._starting_balance_date = None
        self._title = None
        self._type = None
        self._updated_at = None
        self.discriminator = None

        if achieve_date is not None:
            self.achieve_date = achieve_date
        if closing_balance is not None:
            self.closing_balance = closing_balance
        if closing_balance_date is not None:
            self.closing_balance_date = closing_balance_date
        if created_at is not None:
            self.created_at = created_at
        if current_balance is not None:
            self.current_balance = current_balance
        if current_balance_date is not None:
            self.current_balance_date = current_balance_date
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if interest_rate is not None:
            self.interest_rate = interest_rate
        if interest_rate_repeat_id is not None:
            self.interest_rate_repeat_id = interest_rate_repeat_id
        if maximum_value is not None:
            self.maximum_value = maximum_value
        if minimum_value is not None:
            self.minimum_value = minimum_value
        if starting_balance is not None:
            self.starting_balance = starting_balance
        if starting_balance_date is not None:
            self.starting_balance_date = starting_balance_date
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def achieve_date(self):
        """Gets the achieve_date of this Scenario.  # noqa: E501

        For goals, the date that they should be achieved by.  # noqa: E501

        :return: The achieve_date of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._achieve_date

    @achieve_date.setter
    def achieve_date(self, achieve_date):
        """Sets the achieve_date of this Scenario.

        For goals, the date that they should be achieved by.  # noqa: E501

        :param achieve_date: The achieve_date of this Scenario.  # noqa: E501
        :type: str
        """

        self._achieve_date = achieve_date

    @property
    def closing_balance(self):
        """Gets the closing_balance of this Scenario.  # noqa: E501

        The closing balance of the scenario.  # noqa: E501

        :return: The closing_balance of this Scenario.  # noqa: E501
        :rtype: float
        """
        return self._closing_balance

    @closing_balance.setter
    def closing_balance(self, closing_balance):
        """Sets the closing_balance of this Scenario.

        The closing balance of the scenario.  # noqa: E501

        :param closing_balance: The closing_balance of this Scenario.  # noqa: E501
        :type: float
        """

        self._closing_balance = closing_balance

    @property
    def closing_balance_date(self):
        """Gets the closing_balance_date of this Scenario.  # noqa: E501

        The date of the closing balance.  # noqa: E501

        :return: The closing_balance_date of this Scenario.  # noqa: E501
        :rtype: date
        """
        return self._closing_balance_date

    @closing_balance_date.setter
    def closing_balance_date(self, closing_balance_date):
        """Sets the closing_balance_date of this Scenario.

        The date of the closing balance.  # noqa: E501

        :param closing_balance_date: The closing_balance_date of this Scenario.  # noqa: E501
        :type: date
        """

        self._closing_balance_date = closing_balance_date

    @property
    def created_at(self):
        """Gets the created_at of this Scenario.  # noqa: E501

        When the scenario was created.  # noqa: E501

        :return: The created_at of this Scenario.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Scenario.

        When the scenario was created.  # noqa: E501

        :param created_at: The created_at of this Scenario.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def current_balance(self):
        """Gets the current_balance of this Scenario.  # noqa: E501

        The current balance of the scenario.  # noqa: E501

        :return: The current_balance of this Scenario.  # noqa: E501
        :rtype: float
        """
        return self._current_balance

    @current_balance.setter
    def current_balance(self, current_balance):
        """Sets the current_balance of this Scenario.

        The current balance of the scenario.  # noqa: E501

        :param current_balance: The current_balance of this Scenario.  # noqa: E501
        :type: float
        """

        self._current_balance = current_balance

    @property
    def current_balance_date(self):
        """Gets the current_balance_date of this Scenario.  # noqa: E501

        The date of the current balance.  # noqa: E501

        :return: The current_balance_date of this Scenario.  # noqa: E501
        :rtype: date
        """
        return self._current_balance_date

    @current_balance_date.setter
    def current_balance_date(self, current_balance_date):
        """Sets the current_balance_date of this Scenario.

        The date of the current balance.  # noqa: E501

        :param current_balance_date: The current_balance_date of this Scenario.  # noqa: E501
        :type: date
        """

        self._current_balance_date = current_balance_date

    @property
    def description(self):
        """Gets the description of this Scenario.  # noqa: E501

        A short description of what the scenario is modelling.  # noqa: E501

        :return: The description of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Scenario.

        A short description of what the scenario is modelling.  # noqa: E501

        :param description: The description of this Scenario.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Scenario.  # noqa: E501

        The unique identifier of the scenario.  # noqa: E501

        :return: The id of this Scenario.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scenario.

        The unique identifier of the scenario.  # noqa: E501

        :param id: The id of this Scenario.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def interest_rate(self):
        """Gets the interest_rate of this Scenario.  # noqa: E501

        The amount of interest to apply to the balance. Will apply periodically depending on what `interest_rate_repeat_id` is set to.  # noqa: E501

        :return: The interest_rate of this Scenario.  # noqa: E501
        :rtype: float
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this Scenario.

        The amount of interest to apply to the balance. Will apply periodically depending on what `interest_rate_repeat_id` is set to.  # noqa: E501

        :param interest_rate: The interest_rate of this Scenario.  # noqa: E501
        :type: float
        """

        self._interest_rate = interest_rate

    @property
    def interest_rate_repeat_id(self):
        """Gets the interest_rate_repeat_id of this Scenario.  # noqa: E501

        A number representing how often the interest should be applied. 0 is used for no interest, 2 is weekly, 3 is fortnightly, 4 is monthly, 5 is yearly and 7 for quarterly.  # noqa: E501

        :return: The interest_rate_repeat_id of this Scenario.  # noqa: E501
        :rtype: int
        """
        return self._interest_rate_repeat_id

    @interest_rate_repeat_id.setter
    def interest_rate_repeat_id(self, interest_rate_repeat_id):
        """Sets the interest_rate_repeat_id of this Scenario.

        A number representing how often the interest should be applied. 0 is used for no interest, 2 is weekly, 3 is fortnightly, 4 is monthly, 5 is yearly and 7 for quarterly.  # noqa: E501

        :param interest_rate_repeat_id: The interest_rate_repeat_id of this Scenario.  # noqa: E501
        :type: int
        """

        self._interest_rate_repeat_id = interest_rate_repeat_id

    @property
    def maximum_value(self):
        """Gets the maximum_value of this Scenario.  # noqa: E501


        :return: The maximum_value of this Scenario.  # noqa: E501
        :rtype: float
        """
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        """Sets the maximum_value of this Scenario.


        :param maximum_value: The maximum_value of this Scenario.  # noqa: E501
        :type: float
        """

        self._maximum_value = maximum_value

    @property
    def minimum_value(self):
        """Gets the minimum_value of this Scenario.  # noqa: E501


        :return: The minimum_value of this Scenario.  # noqa: E501
        :rtype: float
        """
        return self._minimum_value

    @minimum_value.setter
    def minimum_value(self, minimum_value):
        """Sets the minimum_value of this Scenario.


        :param minimum_value: The minimum_value of this Scenario.  # noqa: E501
        :type: float
        """

        self._minimum_value = minimum_value

    @property
    def starting_balance(self):
        """Gets the starting_balance of this Scenario.  # noqa: E501

        The starting balance of the scenario.  # noqa: E501

        :return: The starting_balance of this Scenario.  # noqa: E501
        :rtype: float
        """
        return self._starting_balance

    @starting_balance.setter
    def starting_balance(self, starting_balance):
        """Sets the starting_balance of this Scenario.

        The starting balance of the scenario.  # noqa: E501

        :param starting_balance: The starting_balance of this Scenario.  # noqa: E501
        :type: float
        """

        self._starting_balance = starting_balance

    @property
    def starting_balance_date(self):
        """Gets the starting_balance_date of this Scenario.  # noqa: E501

        The date of the starting balance.  # noqa: E501

        :return: The starting_balance_date of this Scenario.  # noqa: E501
        :rtype: date
        """
        return self._starting_balance_date

    @starting_balance_date.setter
    def starting_balance_date(self, starting_balance_date):
        """Sets the starting_balance_date of this Scenario.

        The date of the starting balance.  # noqa: E501

        :param starting_balance_date: The starting_balance_date of this Scenario.  # noqa: E501
        :type: date
        """

        self._starting_balance_date = starting_balance_date

    @property
    def title(self):
        """Gets the title of this Scenario.  # noqa: E501

        The title of the scenario.  # noqa: E501

        :return: The title of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Scenario.

        The title of the scenario.  # noqa: E501

        :param title: The title of this Scenario.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this Scenario.  # noqa: E501

        The type of the scenario.  # noqa: E501

        :return: The type of this Scenario.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Scenario.

        The type of the scenario.  # noqa: E501

        :param type: The type of this Scenario.  # noqa: E501
        :type: str
        """
        allowed_values = ["no-interest", "savings", "debt"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this Scenario.  # noqa: E501

        When the scenario was last updated.  # noqa: E501

        :return: The updated_at of this Scenario.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Scenario.

        When the scenario was last updated.  # noqa: E501

        :param updated_at: The updated_at of this Scenario.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Scenario):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Scenario):
            return True

        return self.to_dict() != other.to_dict()
