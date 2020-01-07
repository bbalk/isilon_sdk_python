# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_2_1.models.changelist_entry import ChangelistEntry  # noqa: F401,E501


class ChangelistEntries(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entries': 'list[ChangelistEntry]'
    }

    attribute_map = {
        'entries': 'entries'
    }

    def __init__(self, entries=None):  # noqa: E501
        """ChangelistEntries - a model defined in Swagger"""  # noqa: E501

        self._entries = None
        self.discriminator = None

        if entries is not None:
            self.entries = entries

    @property
    def entries(self):
        """Gets the entries of this ChangelistEntries.  # noqa: E501


        :return: The entries of this ChangelistEntries.  # noqa: E501
        :rtype: list[ChangelistEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this ChangelistEntries.


        :param entries: The entries of this ChangelistEntries.  # noqa: E501
        :type: list[ChangelistEntry]
        """

        self._entries = entries

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, ChangelistEntries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
