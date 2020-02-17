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


class ClusterNodeStatus(object):
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
        'batterystatus': 'NodeStatusNodeBatterystatus',
        'capacity': 'list[NodeStatusNodeCapacityItem]',
        'cpu': 'NodeStatusNodeCpu',
        'nvram': 'NodeStatusNodeNvram',
        'powersupplies': 'NodeStatusNodePowersupplies',
        'release': 'str',
        'uptime': 'int',
        'version': 'str'
    }

    attribute_map = {
        'batterystatus': 'batterystatus',
        'capacity': 'capacity',
        'cpu': 'cpu',
        'nvram': 'nvram',
        'powersupplies': 'powersupplies',
        'release': 'release',
        'uptime': 'uptime',
        'version': 'version'
    }

    def __init__(self, batterystatus=None, capacity=None, cpu=None, nvram=None, powersupplies=None, release=None, uptime=None, version=None):  # noqa: E501
        """ClusterNodeStatus - a model defined in Swagger"""  # noqa: E501

        self._batterystatus = None
        self._capacity = None
        self._cpu = None
        self._nvram = None
        self._powersupplies = None
        self._release = None
        self._uptime = None
        self._version = None
        self.discriminator = None

        if batterystatus is not None:
            self.batterystatus = batterystatus
        if capacity is not None:
            self.capacity = capacity
        if cpu is not None:
            self.cpu = cpu
        if nvram is not None:
            self.nvram = nvram
        if powersupplies is not None:
            self.powersupplies = powersupplies
        if release is not None:
            self.release = release
        if uptime is not None:
            self.uptime = uptime
        if version is not None:
            self.version = version

    @property
    def batterystatus(self):
        """Gets the batterystatus of this ClusterNodeStatus.  # noqa: E501

        Battery status information.  # noqa: E501

        :return: The batterystatus of this ClusterNodeStatus.  # noqa: E501
        :rtype: NodeStatusNodeBatterystatus
        """
        return self._batterystatus

    @batterystatus.setter
    def batterystatus(self, batterystatus):
        """Sets the batterystatus of this ClusterNodeStatus.

        Battery status information.  # noqa: E501

        :param batterystatus: The batterystatus of this ClusterNodeStatus.  # noqa: E501
        :type: NodeStatusNodeBatterystatus
        """

        self._batterystatus = batterystatus

    @property
    def capacity(self):
        """Gets the capacity of this ClusterNodeStatus.  # noqa: E501

        Storage capacity of this node.  # noqa: E501

        :return: The capacity of this ClusterNodeStatus.  # noqa: E501
        :rtype: list[NodeStatusNodeCapacityItem]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ClusterNodeStatus.

        Storage capacity of this node.  # noqa: E501

        :param capacity: The capacity of this ClusterNodeStatus.  # noqa: E501
        :type: list[NodeStatusNodeCapacityItem]
        """

        self._capacity = capacity

    @property
    def cpu(self):
        """Gets the cpu of this ClusterNodeStatus.  # noqa: E501

        CPU status information for this node.  # noqa: E501

        :return: The cpu of this ClusterNodeStatus.  # noqa: E501
        :rtype: NodeStatusNodeCpu
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ClusterNodeStatus.

        CPU status information for this node.  # noqa: E501

        :param cpu: The cpu of this ClusterNodeStatus.  # noqa: E501
        :type: NodeStatusNodeCpu
        """

        self._cpu = cpu

    @property
    def nvram(self):
        """Gets the nvram of this ClusterNodeStatus.  # noqa: E501

        Node NVRAM information.  # noqa: E501

        :return: The nvram of this ClusterNodeStatus.  # noqa: E501
        :rtype: NodeStatusNodeNvram
        """
        return self._nvram

    @nvram.setter
    def nvram(self, nvram):
        """Sets the nvram of this ClusterNodeStatus.

        Node NVRAM information.  # noqa: E501

        :param nvram: The nvram of this ClusterNodeStatus.  # noqa: E501
        :type: NodeStatusNodeNvram
        """

        self._nvram = nvram

    @property
    def powersupplies(self):
        """Gets the powersupplies of this ClusterNodeStatus.  # noqa: E501

        Information about this node's power supplies.  # noqa: E501

        :return: The powersupplies of this ClusterNodeStatus.  # noqa: E501
        :rtype: NodeStatusNodePowersupplies
        """
        return self._powersupplies

    @powersupplies.setter
    def powersupplies(self, powersupplies):
        """Sets the powersupplies of this ClusterNodeStatus.

        Information about this node's power supplies.  # noqa: E501

        :param powersupplies: The powersupplies of this ClusterNodeStatus.  # noqa: E501
        :type: NodeStatusNodePowersupplies
        """

        self._powersupplies = powersupplies

    @property
    def release(self):
        """Gets the release of this ClusterNodeStatus.  # noqa: E501

        OneFS release.  # noqa: E501

        :return: The release of this ClusterNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        """Sets the release of this ClusterNodeStatus.

        OneFS release.  # noqa: E501

        :param release: The release of this ClusterNodeStatus.  # noqa: E501
        :type: str
        """

        self._release = release

    @property
    def uptime(self):
        """Gets the uptime of this ClusterNodeStatus.  # noqa: E501

        Seconds this node has been online.  # noqa: E501

        :return: The uptime of this ClusterNodeStatus.  # noqa: E501
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this ClusterNodeStatus.

        Seconds this node has been online.  # noqa: E501

        :param uptime: The uptime of this ClusterNodeStatus.  # noqa: E501
        :type: int
        """

        self._uptime = uptime

    @property
    def version(self):
        """Gets the version of this ClusterNodeStatus.  # noqa: E501

        OneFS version.  # noqa: E501

        :return: The version of this ClusterNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterNodeStatus.

        OneFS version.  # noqa: E501

        :param version: The version of this ClusterNodeStatus.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(ClusterNodeStatus, dict):
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
        if not isinstance(other, ClusterNodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
