# coding: utf-8

"""
Copyright 2015 SmartBear Software

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


class SettingsReportingEulaItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SettingsReportingEulaItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'accepted': 'bool',
            'body': 'str'
        }

        self.attribute_map = {
            'accepted': 'accepted',
            'body': 'body'
        }

        self._accepted = None
        self._body = None

    @property
    def accepted(self):
        """
        Gets the accepted of this SettingsReportingEulaItem.
        Indicates whether the telemetry collection warning has been acknowledged

        :return: The accepted of this SettingsReportingEulaItem.
        :rtype: bool
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """
        Sets the accepted of this SettingsReportingEulaItem.
        Indicates whether the telemetry collection warning has been acknowledged

        :param accepted: The accepted of this SettingsReportingEulaItem.
        :type: bool
        """
        self._accepted = accepted

    @property
    def body(self):
        """
        Gets the body of this SettingsReportingEulaItem.
        The body of the telemetry collection warning

        :return: The body of this SettingsReportingEulaItem.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this SettingsReportingEulaItem.
        The body of the telemetry collection warning

        :param body: The body of this SettingsReportingEulaItem.
        :type: str
        """
        self._body = body

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

