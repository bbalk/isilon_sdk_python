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


class EventEventgroupDefinitions(object):
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
        'eventgroup_definitions': 'list[EventEventgroupDefinitionsEventgroupDefinition]'
    }

    attribute_map = {
        'eventgroup_definitions': 'eventgroup-definitions'
    }

    def __init__(self, eventgroup_definitions=None):  # noqa: E501
        """EventEventgroupDefinitions - a model defined in Swagger"""  # noqa: E501

        self._eventgroup_definitions = None
        self.discriminator = None

        if eventgroup_definitions is not None:
            self.eventgroup_definitions = eventgroup_definitions

    @property
    def eventgroup_definitions(self):
        """Gets the eventgroup_definitions of this EventEventgroupDefinitions.  # noqa: E501


        :return: The eventgroup_definitions of this EventEventgroupDefinitions.  # noqa: E501
        :rtype: list[EventEventgroupDefinitionsEventgroupDefinition]
        """
        return self._eventgroup_definitions

    @eventgroup_definitions.setter
    def eventgroup_definitions(self, eventgroup_definitions):
        """Sets the eventgroup_definitions of this EventEventgroupDefinitions.


        :param eventgroup_definitions: The eventgroup_definitions of this EventEventgroupDefinitions.  # noqa: E501
        :type: list[EventEventgroupDefinitionsEventgroupDefinition]
        """

        self._eventgroup_definitions = eventgroup_definitions

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
        if issubclass(EventEventgroupDefinitions, dict):
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
        if not isinstance(other, EventEventgroupDefinitions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
