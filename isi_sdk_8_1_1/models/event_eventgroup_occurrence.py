# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EventEventgroupOccurrence(object):
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
        'ignore': 'bool',
        'resolved': 'bool'
    }

    attribute_map = {
        'ignore': 'ignore',
        'resolved': 'resolved'
    }

    def __init__(self, ignore=None, resolved=None):  # noqa: E501
        """EventEventgroupOccurrence - a model defined in Swagger"""  # noqa: E501

        self._ignore = None
        self._resolved = None
        self.discriminator = None

        if ignore is not None:
            self.ignore = ignore
        if resolved is not None:
            self.resolved = resolved

    @property
    def ignore(self):
        """Gets the ignore of this EventEventgroupOccurrence.  # noqa: E501

        True if eventgroup is to be ignored  # noqa: E501

        :return: The ignore of this EventEventgroupOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._ignore

    @ignore.setter
    def ignore(self, ignore):
        """Sets the ignore of this EventEventgroupOccurrence.

        True if eventgroup is to be ignored  # noqa: E501

        :param ignore: The ignore of this EventEventgroupOccurrence.  # noqa: E501
        :type: bool
        """

        self._ignore = ignore

    @property
    def resolved(self):
        """Gets the resolved of this EventEventgroupOccurrence.  # noqa: E501

        True if eventgroup is to be resolved  # noqa: E501

        :return: The resolved of this EventEventgroupOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """Sets the resolved of this EventEventgroupOccurrence.

        True if eventgroup is to be resolved  # noqa: E501

        :param resolved: The resolved of this EventEventgroupOccurrence.  # noqa: E501
        :type: bool
        """

        self._resolved = resolved

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
        if issubclass(EventEventgroupOccurrence, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventEventgroupOccurrence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
