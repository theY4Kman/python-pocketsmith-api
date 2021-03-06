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


class InlineObject10(object):
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
        'currency_code': 'str',
        'institution_id': 'int',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'institution_id': 'institution_id',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, currency_code=None, institution_id=None, title=None, type=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject10 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_code = None
        self._institution_id = None
        self._title = None
        self._type = None
        self.discriminator = None

        self.currency_code = currency_code
        self.institution_id = institution_id
        self.title = title
        self.type = type

    @property
    def currency_code(self):
        """Gets the currency_code of this InlineObject10.  # noqa: E501

        A currency code for the account.  # noqa: E501

        :return: The currency_code of this InlineObject10.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this InlineObject10.

        A currency code for the account.  # noqa: E501

        :param currency_code: The currency_code of this InlineObject10.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency_code is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def institution_id(self):
        """Gets the institution_id of this InlineObject10.  # noqa: E501

        The ID of the institution to create this account in.  # noqa: E501

        :return: The institution_id of this InlineObject10.  # noqa: E501
        :rtype: int
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this InlineObject10.

        The ID of the institution to create this account in.  # noqa: E501

        :param institution_id: The institution_id of this InlineObject10.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and institution_id is None:  # noqa: E501
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def title(self):
        """Gets the title of this InlineObject10.  # noqa: E501

        A title for the account.  # noqa: E501

        :return: The title of this InlineObject10.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineObject10.

        A title for the account.  # noqa: E501

        :param title: The title of this InlineObject10.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def type(self):
        """Gets the type of this InlineObject10.  # noqa: E501

        The type of the account.  # noqa: E501

        :return: The type of this InlineObject10.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineObject10.

        The type of the account.  # noqa: E501

        :param type: The type of this InlineObject10.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["bank", "credits", "loans", "mortgage", "stocks", "vehicle", "property", "other_asset", "other_liability"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, InlineObject10):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject10):
            return True

        return self.to_dict() != other.to_dict()
