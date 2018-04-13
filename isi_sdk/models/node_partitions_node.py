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

from isi_sdk_8_0_1.models.node_partitions_node_partition import NodePartitionsNodePartition  # noqa: F401,E501


class NodePartitionsNode(object):
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
        'count': 'int',
        'id': 'int',
        'lnn': 'int',
        'partitions': 'list[NodePartitionsNodePartition]'
    }

    attribute_map = {
        'count': 'count',
        'id': 'id',
        'lnn': 'lnn',
        'partitions': 'partitions'
    }

    def __init__(self, count=None, id=None, lnn=None, partitions=None):  # noqa: E501
        """NodePartitionsNode - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._id = None
        self._lnn = None
        self._partitions = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if partitions is not None:
            self.partitions = partitions

    @property
    def count(self):
        """Gets the count of this NodePartitionsNode.  # noqa: E501

        Count of how many partitions are included.  # noqa: E501

        :return: The count of this NodePartitionsNode.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this NodePartitionsNode.

        Count of how many partitions are included.  # noqa: E501

        :param count: The count of this NodePartitionsNode.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def id(self):
        """Gets the id of this NodePartitionsNode.  # noqa: E501

        Node ID (Device Number) of this node.  # noqa: E501

        :return: The id of this NodePartitionsNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodePartitionsNode.

        Node ID (Device Number) of this node.  # noqa: E501

        :param id: The id of this NodePartitionsNode.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this NodePartitionsNode.  # noqa: E501

        Logical Node Number (LNN) of this node.  # noqa: E501

        :return: The lnn of this NodePartitionsNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodePartitionsNode.

        Logical Node Number (LNN) of this node.  # noqa: E501

        :param lnn: The lnn of this NodePartitionsNode.  # noqa: E501
        :type: int
        """

        self._lnn = lnn

    @property
    def partitions(self):
        """Gets the partitions of this NodePartitionsNode.  # noqa: E501

        Partition information.  # noqa: E501

        :return: The partitions of this NodePartitionsNode.  # noqa: E501
        :rtype: list[NodePartitionsNodePartition]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this NodePartitionsNode.

        Partition information.  # noqa: E501

        :param partitions: The partitions of this NodePartitionsNode.  # noqa: E501
        :type: list[NodePartitionsNodePartition]
        """

        self._partitions = partitions

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
        if not isinstance(other, NodePartitionsNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
