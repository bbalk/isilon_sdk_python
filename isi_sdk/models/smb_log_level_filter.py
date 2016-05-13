# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class SmbLogLevelFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SmbLogLevelFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ip_addrs': 'list[str]',
            'level': 'str',
            'ops': 'list[str]'
        }

        self.attribute_map = {
            'ip_addrs': 'ip_addrs',
            'level': 'level',
            'ops': 'ops'
        }

        self._ip_addrs = None
        self._level = None
        self._ops = None

    @property
    def ip_addrs(self):
        """
        Gets the ip_addrs of this SmbLogLevelFilter.
        Array of client IP addresses to filter against.

        :return: The ip_addrs of this SmbLogLevelFilter.
        :rtype: list[str]
        """
        return self._ip_addrs

    @ip_addrs.setter
    def ip_addrs(self, ip_addrs):
        """
        Sets the ip_addrs of this SmbLogLevelFilter.
        Array of client IP addresses to filter against.

        :param ip_addrs: The ip_addrs of this SmbLogLevelFilter.
        :type: list[str]
        """
        
        self._ip_addrs = ip_addrs

    @property
    def level(self):
        """
        Gets the level of this SmbLogLevelFilter.
        Logging level of the filter.

        :return: The level of this SmbLogLevelFilter.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this SmbLogLevelFilter.
        Logging level of the filter.

        :param level: The level of this SmbLogLevelFilter.
        :type: str
        """
        allowed_values = ["always", "error", "warning", "info", "verbose", "debug", "trace"]
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level`, must be one of {0}"
                .format(allowed_values)
            )

        self._level = level

    @property
    def ops(self):
        """
        Gets the ops of this SmbLogLevelFilter.
        Array of SMB operations to filter against.

        :return: The ops of this SmbLogLevelFilter.
        :rtype: list[str]
        """
        return self._ops

    @ops.setter
    def ops(self, ops):
        """
        Sets the ops of this SmbLogLevelFilter.
        Array of SMB operations to filter against.

        :param ops: The ops of this SmbLogLevelFilter.
        :type: list[str]
        """
        
        self._ops = ops

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

