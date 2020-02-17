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


class SnapshotSchedulesExtended(object):
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
        'resume': 'str',
        'schedules': 'list[SnapshotScheduleExtendedExtended]',
        'total': 'int'
    }

    attribute_map = {
        'resume': 'resume',
        'schedules': 'schedules',
        'total': 'total'
    }

    def __init__(self, resume=None, schedules=None, total=None):  # noqa: E501
        """SnapshotSchedulesExtended - a model defined in Swagger"""  # noqa: E501

        self._resume = None
        self._schedules = None
        self._total = None
        self.discriminator = None

        if resume is not None:
            self.resume = resume
        if schedules is not None:
            self.schedules = schedules
        if total is not None:
            self.total = total

    @property
    def resume(self):
        """Gets the resume of this SnapshotSchedulesExtended.  # noqa: E501

        Resume token value to use in subsequent calls for continuation.  # noqa: E501

        :return: The resume of this SnapshotSchedulesExtended.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this SnapshotSchedulesExtended.

        Resume token value to use in subsequent calls for continuation.  # noqa: E501

        :param resume: The resume of this SnapshotSchedulesExtended.  # noqa: E501
        :type: str
        """

        self._resume = resume

    @property
    def schedules(self):
        """Gets the schedules of this SnapshotSchedulesExtended.  # noqa: E501


        :return: The schedules of this SnapshotSchedulesExtended.  # noqa: E501
        :rtype: list[SnapshotScheduleExtendedExtended]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this SnapshotSchedulesExtended.


        :param schedules: The schedules of this SnapshotSchedulesExtended.  # noqa: E501
        :type: list[SnapshotScheduleExtendedExtended]
        """

        self._schedules = schedules

    @property
    def total(self):
        """Gets the total of this SnapshotSchedulesExtended.  # noqa: E501

        Total number of items available.  # noqa: E501

        :return: The total of this SnapshotSchedulesExtended.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SnapshotSchedulesExtended.

        Total number of items available.  # noqa: E501

        :param total: The total of this SnapshotSchedulesExtended.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(SnapshotSchedulesExtended, dict):
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
        if not isinstance(other, SnapshotSchedulesExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
