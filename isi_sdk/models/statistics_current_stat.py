# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 4
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StatisticsCurrentStat(object):
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
        'devid': 'int',
        'error': 'str',
        'error_code': 'int',
        'key': 'str',
        'time': 'int',
        'value': 'str'
    }

    attribute_map = {
        'devid': 'devid',
        'error': 'error',
        'error_code': 'error_code',
        'key': 'key',
        'time': 'time',
        'value': 'value'
    }

    def __init__(self, devid=None, error=None, error_code=None, key=None, time=None, value=None):  # noqa: E501
        """StatisticsCurrentStat - a model defined in Swagger"""  # noqa: E501

        self._devid = None
        self._error = None
        self._error_code = None
        self._key = None
        self._time = None
        self._value = None
        self.discriminator = None

        self.devid = devid
        if error is not None:
            self.error = error
        if error_code is not None:
            self.error_code = error_code
        self.key = key
        self.time = time
        if value is not None:
            self.value = value

    @property
    def devid(self):
        """Gets the devid of this StatisticsCurrentStat.  # noqa: E501

        Devid of node of statistic or 0 for cluster scoped statistics.  # noqa: E501

        :return: The devid of this StatisticsCurrentStat.  # noqa: E501
        :rtype: int
        """
        return self._devid

    @devid.setter
    def devid(self, devid):
        """Sets the devid of this StatisticsCurrentStat.

        Devid of node of statistic or 0 for cluster scoped statistics.  # noqa: E501

        :param devid: The devid of this StatisticsCurrentStat.  # noqa: E501
        :type: int
        """
        if devid is None:
            raise ValueError("Invalid value for `devid`, must not be `None`")  # noqa: E501

        self._devid = devid

    @property
    def error(self):
        """Gets the error of this StatisticsCurrentStat.  # noqa: E501

        Key specific error string, if applicable.  # noqa: E501

        :return: The error of this StatisticsCurrentStat.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this StatisticsCurrentStat.

        Key specific error string, if applicable.  # noqa: E501

        :param error: The error of this StatisticsCurrentStat.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_code(self):
        """Gets the error_code of this StatisticsCurrentStat.  # noqa: E501

        Key specific error number, if applicable.  # noqa: E501

        :return: The error_code of this StatisticsCurrentStat.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this StatisticsCurrentStat.

        Key specific error number, if applicable.  # noqa: E501

        :param error_code: The error_code of this StatisticsCurrentStat.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def key(self):
        """Gets the key of this StatisticsCurrentStat.  # noqa: E501

        Key name of statistic.  # noqa: E501

        :return: The key of this StatisticsCurrentStat.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this StatisticsCurrentStat.

        Key name of statistic.  # noqa: E501

        :param key: The key of this StatisticsCurrentStat.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def time(self):
        """Gets the time of this StatisticsCurrentStat.  # noqa: E501

        Unix Epoch time in seconds that statistic was collected.  # noqa: E501

        :return: The time of this StatisticsCurrentStat.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StatisticsCurrentStat.

        Unix Epoch time in seconds that statistic was collected.  # noqa: E501

        :param time: The time of this StatisticsCurrentStat.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def value(self):
        """Gets the value of this StatisticsCurrentStat.  # noqa: E501

        Key dependent value.  # noqa: E501

        :return: The value of this StatisticsCurrentStat.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StatisticsCurrentStat.

        Key dependent value.  # noqa: E501

        :param value: The value of this StatisticsCurrentStat.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, StatisticsCurrentStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
