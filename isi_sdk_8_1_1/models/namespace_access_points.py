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


class NamespaceAccessPoints(object):
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
        'namespaces': 'list[NamespaceAccessPointsNamespaces]',
        'versions': 'list[str]'
    }

    attribute_map = {
        'namespaces': 'namespaces',
        'versions': 'versions'
    }

    def __init__(self, namespaces=None, versions=None):  # noqa: E501
        """NamespaceAccessPoints - a model defined in Swagger"""  # noqa: E501

        self._namespaces = None
        self._versions = None
        self.discriminator = None

        if namespaces is not None:
            self.namespaces = namespaces
        if versions is not None:
            self.versions = versions

    @property
    def namespaces(self):
        """Gets the namespaces of this NamespaceAccessPoints.  # noqa: E501


        :return: The namespaces of this NamespaceAccessPoints.  # noqa: E501
        :rtype: list[NamespaceAccessPointsNamespaces]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this NamespaceAccessPoints.


        :param namespaces: The namespaces of this NamespaceAccessPoints.  # noqa: E501
        :type: list[NamespaceAccessPointsNamespaces]
        """

        self._namespaces = namespaces

    @property
    def versions(self):
        """Gets the versions of this NamespaceAccessPoints.  # noqa: E501


        :return: The versions of this NamespaceAccessPoints.  # noqa: E501
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this NamespaceAccessPoints.


        :param versions: The versions of this NamespaceAccessPoints.  # noqa: E501
        :type: list[str]
        """

        self._versions = versions

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
        if issubclass(NamespaceAccessPoints, dict):
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
        if not isinstance(other, NamespaceAccessPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
