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


class NodeDriveconfigNodeAlert(object):
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
        'unknown_firmware': 'bool',
        'unknown_model': 'bool'
    }

    attribute_map = {
        'unknown_firmware': 'unknown_firmware',
        'unknown_model': 'unknown_model'
    }

    def __init__(self, unknown_firmware=True, unknown_model=True):  # noqa: E501
        """NodeDriveconfigNodeAlert - a model defined in Swagger"""  # noqa: E501

        self._unknown_firmware = None
        self._unknown_model = None
        self.discriminator = None

        if unknown_firmware is not None:
            self.unknown_firmware = unknown_firmware
        if unknown_model is not None:
            self.unknown_model = unknown_model

    @property
    def unknown_firmware(self):
        """Gets the unknown_firmware of this NodeDriveconfigNodeAlert.  # noqa: E501

        Send alerts for unknown drive firmware.  # noqa: E501

        :return: The unknown_firmware of this NodeDriveconfigNodeAlert.  # noqa: E501
        :rtype: bool
        """
        return self._unknown_firmware

    @unknown_firmware.setter
    def unknown_firmware(self, unknown_firmware):
        """Sets the unknown_firmware of this NodeDriveconfigNodeAlert.

        Send alerts for unknown drive firmware.  # noqa: E501

        :param unknown_firmware: The unknown_firmware of this NodeDriveconfigNodeAlert.  # noqa: E501
        :type: bool
        """

        self._unknown_firmware = unknown_firmware

    @property
    def unknown_model(self):
        """Gets the unknown_model of this NodeDriveconfigNodeAlert.  # noqa: E501

        Send alerts for unknown drive model.  # noqa: E501

        :return: The unknown_model of this NodeDriveconfigNodeAlert.  # noqa: E501
        :rtype: bool
        """
        return self._unknown_model

    @unknown_model.setter
    def unknown_model(self, unknown_model):
        """Sets the unknown_model of this NodeDriveconfigNodeAlert.

        Send alerts for unknown drive model.  # noqa: E501

        :param unknown_model: The unknown_model of this NodeDriveconfigNodeAlert.  # noqa: E501
        :type: bool
        """

        self._unknown_model = unknown_model

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
        if issubclass(NodeDriveconfigNodeAlert, dict):
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
        if not isinstance(other, NodeDriveconfigNodeAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
