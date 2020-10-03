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


class InlineObject2(object):
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
        'colour': 'str',
        'parent_id': 'int',
        'title': 'str'
    }

    attribute_map = {
        'colour': 'colour',
        'parent_id': 'parent_id',
        'title': 'title'
    }

    def __init__(self, colour=None, parent_id=None, title=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._colour = None
        self._parent_id = None
        self._title = None
        self.discriminator = None

        if colour is not None:
            self.colour = colour
        if parent_id is not None:
            self.parent_id = parent_id
        if title is not None:
            self.title = title

    @property
    def colour(self):
        """Gets the colour of this InlineObject2.  # noqa: E501

        A new CSS-style hex colour for the category.  # noqa: E501

        :return: The colour of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._colour

    @colour.setter
    def colour(self, colour):
        """Sets the colour of this InlineObject2.

        A new CSS-style hex colour for the category.  # noqa: E501

        :param colour: The colour of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._colour = colour

    @property
    def parent_id(self):
        """Gets the parent_id of this InlineObject2.  # noqa: E501

        The unique identifier of a parent category for the category, making this category a child of that category.  # noqa: E501

        :return: The parent_id of this InlineObject2.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this InlineObject2.

        The unique identifier of a parent category for the category, making this category a child of that category.  # noqa: E501

        :param parent_id: The parent_id of this InlineObject2.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def title(self):
        """Gets the title of this InlineObject2.  # noqa: E501

        A new title for the category.  # noqa: E501

        :return: The title of this InlineObject2.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineObject2.

        A new title for the category.  # noqa: E501

        :param title: The title of this InlineObject2.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if not isinstance(other, InlineObject2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject2):
            return True

        return self.to_dict() != other.to_dict()