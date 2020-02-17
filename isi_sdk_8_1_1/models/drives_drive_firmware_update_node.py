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


class DrivesDriveFirmwareUpdateNode(object):
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
        'error': 'str',
        'id': 'int',
        'lnn': 'int',
        'status': 'DrivesDriveFirmwareUpdateNodeStatus'
    }

    attribute_map = {
        'error': 'error',
        'id': 'id',
        'lnn': 'lnn',
        'status': 'status'
    }

    def __init__(self, error=None, id=None, lnn=None, status=None):  # noqa: E501
        """DrivesDriveFirmwareUpdateNode - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._id = None
        self._lnn = None
        self._status = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if status is not None:
            self.status = status

    @property
    def error(self):
        """Gets the error of this DrivesDriveFirmwareUpdateNode.  # noqa: E501

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :return: The error of this DrivesDriveFirmwareUpdateNode.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DrivesDriveFirmwareUpdateNode.

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :param error: The error of this DrivesDriveFirmwareUpdateNode.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """Gets the id of this DrivesDriveFirmwareUpdateNode.  # noqa: E501

        Node ID of the node reporting this information.  # noqa: E501

        :return: The id of this DrivesDriveFirmwareUpdateNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DrivesDriveFirmwareUpdateNode.

        Node ID of the node reporting this information.  # noqa: E501

        :param id: The id of this DrivesDriveFirmwareUpdateNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this DrivesDriveFirmwareUpdateNode.  # noqa: E501

        Logical node number of the node reporting this information.  # noqa: E501

        :return: The lnn of this DrivesDriveFirmwareUpdateNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this DrivesDriveFirmwareUpdateNode.

        Logical node number of the node reporting this information.  # noqa: E501

        :param lnn: The lnn of this DrivesDriveFirmwareUpdateNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if lnn is not None and lnn < 0:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `0`")  # noqa: E501

        self._lnn = lnn

    @property
    def status(self):
        """Gets the status of this DrivesDriveFirmwareUpdateNode.  # noqa: E501

        Drive firmware update status information.  # noqa: E501

        :return: The status of this DrivesDriveFirmwareUpdateNode.  # noqa: E501
        :rtype: DrivesDriveFirmwareUpdateNodeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DrivesDriveFirmwareUpdateNode.

        Drive firmware update status information.  # noqa: E501

        :param status: The status of this DrivesDriveFirmwareUpdateNode.  # noqa: E501
        :type: DrivesDriveFirmwareUpdateNodeStatus
        """

        self._status = status

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
        if issubclass(DrivesDriveFirmwareUpdateNode, dict):
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
        if not isinstance(other, DrivesDriveFirmwareUpdateNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other