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


class StatisticsHistoryStat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StatisticsHistoryStat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'devid': 'int',
            'error': 'str',
            'error_code': 'int',
            'key': 'str',
            'values': 'list[StatisticsHistoryStatValue]'
        }

        self.attribute_map = {
            'devid': 'devid',
            'error': 'error',
            'error_code': 'error_code',
            'key': 'key',
            'values': 'values'
        }

        self._devid = None
        self._error = None
        self._error_code = None
        self._key = None
        self._values = None

    @property
    def devid(self):
        """
        Gets the devid of this StatisticsHistoryStat.
        Devid of node of statistic or 0 for cluster scoped statistics.

        :return: The devid of this StatisticsHistoryStat.
        :rtype: int
        """
        return self._devid

    @devid.setter
    def devid(self, devid):
        """
        Sets the devid of this StatisticsHistoryStat.
        Devid of node of statistic or 0 for cluster scoped statistics.

        :param devid: The devid of this StatisticsHistoryStat.
        :type: int
        """
        
        self._devid = devid

    @property
    def error(self):
        """
        Gets the error of this StatisticsHistoryStat.
        Key specific error string, if applicable.

        :return: The error of this StatisticsHistoryStat.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this StatisticsHistoryStat.
        Key specific error string, if applicable.

        :param error: The error of this StatisticsHistoryStat.
        :type: str
        """
        
        self._error = error

    @property
    def error_code(self):
        """
        Gets the error_code of this StatisticsHistoryStat.
        Key specific error number, if applicable.

        :return: The error_code of this StatisticsHistoryStat.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this StatisticsHistoryStat.
        Key specific error number, if applicable.

        :param error_code: The error_code of this StatisticsHistoryStat.
        :type: int
        """
        
        self._error_code = error_code

    @property
    def key(self):
        """
        Gets the key of this StatisticsHistoryStat.
        Key name of statistic.

        :return: The key of this StatisticsHistoryStat.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this StatisticsHistoryStat.
        Key name of statistic.

        :param key: The key of this StatisticsHistoryStat.
        :type: str
        """
        
        self._key = key

    @property
    def values(self):
        """
        Gets the values of this StatisticsHistoryStat.
        Time-series values.

        :return: The values of this StatisticsHistoryStat.
        :rtype: list[StatisticsHistoryStatValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this StatisticsHistoryStat.
        Time-series values.

        :param values: The values of this StatisticsHistoryStat.
        :type: list[StatisticsHistoryStatValue]
        """
        
        self._values = values

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

