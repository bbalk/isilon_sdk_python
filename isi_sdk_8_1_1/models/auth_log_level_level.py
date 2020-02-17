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


class AuthLogLevelLevel(object):
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
        'lsass_level': 'str',
        'netlogon_level': 'str'
    }

    attribute_map = {
        'lsass_level': 'lsass-level',
        'netlogon_level': 'netlogon-level'
    }

    def __init__(self, lsass_level=None, netlogon_level=None):  # noqa: E501
        """AuthLogLevelLevel - a model defined in Swagger"""  # noqa: E501

        self._lsass_level = None
        self._netlogon_level = None
        self.discriminator = None

        if lsass_level is not None:
            self.lsass_level = lsass_level
        if netlogon_level is not None:
            self.netlogon_level = netlogon_level

    @property
    def lsass_level(self):
        """Gets the lsass_level of this AuthLogLevelLevel.  # noqa: E501

        Valid auth logging levels  # noqa: E501

        :return: The lsass_level of this AuthLogLevelLevel.  # noqa: E501
        :rtype: str
        """
        return self._lsass_level

    @lsass_level.setter
    def lsass_level(self, lsass_level):
        """Sets the lsass_level of this AuthLogLevelLevel.

        Valid auth logging levels  # noqa: E501

        :param lsass_level: The lsass_level of this AuthLogLevelLevel.  # noqa: E501
        :type: str
        """
        allowed_values = ["always", "error", "warning", "info", "verbose", "debug", "trace"]  # noqa: E501
        if lsass_level not in allowed_values:
            raise ValueError(
                "Invalid value for `lsass_level` ({0}), must be one of {1}"  # noqa: E501
                .format(lsass_level, allowed_values)
            )

        self._lsass_level = lsass_level

    @property
    def netlogon_level(self):
        """Gets the netlogon_level of this AuthLogLevelLevel.  # noqa: E501

        Valid auth logging levels  # noqa: E501

        :return: The netlogon_level of this AuthLogLevelLevel.  # noqa: E501
        :rtype: str
        """
        return self._netlogon_level

    @netlogon_level.setter
    def netlogon_level(self, netlogon_level):
        """Sets the netlogon_level of this AuthLogLevelLevel.

        Valid auth logging levels  # noqa: E501

        :param netlogon_level: The netlogon_level of this AuthLogLevelLevel.  # noqa: E501
        :type: str
        """
        allowed_values = ["always", "error", "warning", "info", "verbose", "debug", "trace"]  # noqa: E501
        if netlogon_level not in allowed_values:
            raise ValueError(
                "Invalid value for `netlogon_level` ({0}), must be one of {1}"  # noqa: E501
                .format(netlogon_level, allowed_values)
            )

        self._netlogon_level = netlogon_level

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
        if issubclass(AuthLogLevelLevel, dict):
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
        if not isinstance(other, AuthLogLevelLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
