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


class HardwareStopItem(object):
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
        'node_pool': 'str',
        'split': 'bool'
    }

    attribute_map = {
        'node_pool': 'node_pool',
        'split': 'split'
    }

    def __init__(self, node_pool=None, split=None):  # noqa: E501
        """HardwareStopItem - a model defined in Swagger"""  # noqa: E501

        self._node_pool = None
        self._split = None
        self.discriminator = None

        self.node_pool = node_pool
        if split is not None:
            self.split = split

    @property
    def node_pool(self):
        """Gets the node_pool of this HardwareStopItem.  # noqa: E501

        The nodepool ID or name on which to stop the upgrade.  # noqa: E501

        :return: The node_pool of this HardwareStopItem.  # noqa: E501
        :rtype: str
        """
        return self._node_pool

    @node_pool.setter
    def node_pool(self, node_pool):
        """Sets the node_pool of this HardwareStopItem.

        The nodepool ID or name on which to stop the upgrade.  # noqa: E501

        :param node_pool: The node_pool of this HardwareStopItem.  # noqa: E501
        :type: str
        """
        if node_pool is None:
            raise ValueError("Invalid value for `node_pool`, must not be `None`")  # noqa: E501

        self._node_pool = node_pool

    @property
    def split(self):
        """Gets the split of this HardwareStopItem.  # noqa: E501

        Argument to indicate whether the nodepool should split into upgraded and non-upgraded pools or not. Default is false.  # noqa: E501

        :return: The split of this HardwareStopItem.  # noqa: E501
        :rtype: bool
        """
        return self._split

    @split.setter
    def split(self, split):
        """Sets the split of this HardwareStopItem.

        Argument to indicate whether the nodepool should split into upgraded and non-upgraded pools or not. Default is false.  # noqa: E501

        :param split: The split of this HardwareStopItem.  # noqa: E501
        :type: bool
        """

        self._split = split

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
        if issubclass(HardwareStopItem, dict):
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
        if not isinstance(other, HardwareStopItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
