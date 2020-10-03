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


class AttachmentVariants(object):
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
        'large_url': 'str',
        'thumb_url': 'str'
    }

    attribute_map = {
        'large_url': 'large_url',
        'thumb_url': 'thumb_url'
    }

    def __init__(self, large_url=None, thumb_url=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentVariants - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._large_url = None
        self._thumb_url = None
        self.discriminator = None

        if large_url is not None:
            self.large_url = large_url
        if thumb_url is not None:
            self.thumb_url = thumb_url

    @property
    def large_url(self):
        """Gets the large_url of this AttachmentVariants.  # noqa: E501

        The url of the large version of the attachment  # noqa: E501

        :return: The large_url of this AttachmentVariants.  # noqa: E501
        :rtype: str
        """
        return self._large_url

    @large_url.setter
    def large_url(self, large_url):
        """Sets the large_url of this AttachmentVariants.

        The url of the large version of the attachment  # noqa: E501

        :param large_url: The large_url of this AttachmentVariants.  # noqa: E501
        :type: str
        """

        self._large_url = large_url

    @property
    def thumb_url(self):
        """Gets the thumb_url of this AttachmentVariants.  # noqa: E501

        The url of the thumb version of the attachment  # noqa: E501

        :return: The thumb_url of this AttachmentVariants.  # noqa: E501
        :rtype: str
        """
        return self._thumb_url

    @thumb_url.setter
    def thumb_url(self, thumb_url):
        """Sets the thumb_url of this AttachmentVariants.

        The url of the thumb version of the attachment  # noqa: E501

        :param thumb_url: The thumb_url of this AttachmentVariants.  # noqa: E501
        :type: str
        """

        self._thumb_url = thumb_url

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
        if not isinstance(other, AttachmentVariants):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentVariants):
            return True

        return self.to_dict() != other.to_dict()
