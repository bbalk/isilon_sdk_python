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

from isi_sdk_8_0_1.models.cluster_firmware_status_node_device import ClusterFirmwareStatusNodeDevice  # noqa: F401,E501
from isi_sdk_8_0_1.models.cluster_firmware_status_node_package_item import ClusterFirmwareStatusNodePackageItem  # noqa: F401,E501


class NodesNodeFirmwareStatus(object):
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
        'devices': 'list[ClusterFirmwareStatusNodeDevice]',
        'node_unavailable': 'bool',
        'package': 'list[ClusterFirmwareStatusNodePackageItem]'
    }

    attribute_map = {
        'devices': 'devices',
        'node_unavailable': 'node_unavailable',
        'package': 'package'
    }

    def __init__(self, devices=None, node_unavailable=None, package=None):  # noqa: E501
        """NodesNodeFirmwareStatus - a model defined in Swagger"""  # noqa: E501

        self._devices = None
        self._node_unavailable = None
        self._package = None
        self.discriminator = None

        if devices is not None:
            self.devices = devices
        if node_unavailable is not None:
            self.node_unavailable = node_unavailable
        if package is not None:
            self.package = package

    @property
    def devices(self):
        """Gets the devices of this NodesNodeFirmwareStatus.  # noqa: E501

        List of the firmware status for hardware components on the node.  # noqa: E501

        :return: The devices of this NodesNodeFirmwareStatus.  # noqa: E501
        :rtype: list[ClusterFirmwareStatusNodeDevice]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this NodesNodeFirmwareStatus.

        List of the firmware status for hardware components on the node.  # noqa: E501

        :param devices: The devices of this NodesNodeFirmwareStatus.  # noqa: E501
        :type: list[ClusterFirmwareStatusNodeDevice]
        """

        self._devices = devices

    @property
    def node_unavailable(self):
        """Gets the node_unavailable of this NodesNodeFirmwareStatus.  # noqa: E501

        Node is unavailable.  # noqa: E501

        :return: The node_unavailable of this NodesNodeFirmwareStatus.  # noqa: E501
        :rtype: bool
        """
        return self._node_unavailable

    @node_unavailable.setter
    def node_unavailable(self, node_unavailable):
        """Sets the node_unavailable of this NodesNodeFirmwareStatus.

        Node is unavailable.  # noqa: E501

        :param node_unavailable: The node_unavailable of this NodesNodeFirmwareStatus.  # noqa: E501
        :type: bool
        """

        self._node_unavailable = node_unavailable

    @property
    def package(self):
        """Gets the package of this NodesNodeFirmwareStatus.  # noqa: E501

        List of the firmware binary information for the installed firmware package.  # noqa: E501

        :return: The package of this NodesNodeFirmwareStatus.  # noqa: E501
        :rtype: list[ClusterFirmwareStatusNodePackageItem]
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this NodesNodeFirmwareStatus.

        List of the firmware binary information for the installed firmware package.  # noqa: E501

        :param package: The package of this NodesNodeFirmwareStatus.  # noqa: E501
        :type: list[ClusterFirmwareStatusNodePackageItem]
        """

        self._package = package

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
        if not isinstance(other, NodesNodeFirmwareStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
