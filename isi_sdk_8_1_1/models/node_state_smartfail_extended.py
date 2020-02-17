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


class NodeStateSmartfailExtended(object):
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
        'dead': 'bool',
        'down': 'bool',
        'in_cluster': 'bool',
        'readonly': 'bool',
        'shutdown_readonly': 'bool',
        'smartfailed': 'bool'
    }

    attribute_map = {
        'dead': 'dead',
        'down': 'down',
        'in_cluster': 'in_cluster',
        'readonly': 'readonly',
        'shutdown_readonly': 'shutdown_readonly',
        'smartfailed': 'smartfailed'
    }

    def __init__(self, dead=None, down=None, in_cluster=None, readonly=None, shutdown_readonly=None, smartfailed=None):  # noqa: E501
        """NodeStateSmartfailExtended - a model defined in Swagger"""  # noqa: E501

        self._dead = None
        self._down = None
        self._in_cluster = None
        self._readonly = None
        self._shutdown_readonly = None
        self._smartfailed = None
        self.discriminator = None

        if dead is not None:
            self.dead = dead
        if down is not None:
            self.down = down
        if in_cluster is not None:
            self.in_cluster = in_cluster
        if readonly is not None:
            self.readonly = readonly
        if shutdown_readonly is not None:
            self.shutdown_readonly = shutdown_readonly
        if smartfailed is not None:
            self.smartfailed = smartfailed

    @property
    def dead(self):
        """Gets the dead of this NodeStateSmartfailExtended.  # noqa: E501

        This node is dead (dead_devs).  # noqa: E501

        :return: The dead of this NodeStateSmartfailExtended.  # noqa: E501
        :rtype: bool
        """
        return self._dead

    @dead.setter
    def dead(self, dead):
        """Sets the dead of this NodeStateSmartfailExtended.

        This node is dead (dead_devs).  # noqa: E501

        :param dead: The dead of this NodeStateSmartfailExtended.  # noqa: E501
        :type: bool
        """

        self._dead = dead

    @property
    def down(self):
        """Gets the down of this NodeStateSmartfailExtended.  # noqa: E501

        This node is down (down_devs).  # noqa: E501

        :return: The down of this NodeStateSmartfailExtended.  # noqa: E501
        :rtype: bool
        """
        return self._down

    @down.setter
    def down(self, down):
        """Sets the down of this NodeStateSmartfailExtended.

        This node is down (down_devs).  # noqa: E501

        :param down: The down of this NodeStateSmartfailExtended.  # noqa: E501
        :type: bool
        """

        self._down = down

    @property
    def in_cluster(self):
        """Gets the in_cluster of this NodeStateSmartfailExtended.  # noqa: E501

        This node is in the cluster (all_devs).  # noqa: E501

        :return: The in_cluster of this NodeStateSmartfailExtended.  # noqa: E501
        :rtype: bool
        """
        return self._in_cluster

    @in_cluster.setter
    def in_cluster(self, in_cluster):
        """Sets the in_cluster of this NodeStateSmartfailExtended.

        This node is in the cluster (all_devs).  # noqa: E501

        :param in_cluster: The in_cluster of this NodeStateSmartfailExtended.  # noqa: E501
        :type: bool
        """

        self._in_cluster = in_cluster

    @property
    def readonly(self):
        """Gets the readonly of this NodeStateSmartfailExtended.  # noqa: E501

        This node is readonly (ro_devs).  # noqa: E501

        :return: The readonly of this NodeStateSmartfailExtended.  # noqa: E501
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this NodeStateSmartfailExtended.

        This node is readonly (ro_devs).  # noqa: E501

        :param readonly: The readonly of this NodeStateSmartfailExtended.  # noqa: E501
        :type: bool
        """

        self._readonly = readonly

    @property
    def shutdown_readonly(self):
        """Gets the shutdown_readonly of this NodeStateSmartfailExtended.  # noqa: E501

        This node is shutdown readonly (down_devs).  # noqa: E501

        :return: The shutdown_readonly of this NodeStateSmartfailExtended.  # noqa: E501
        :rtype: bool
        """
        return self._shutdown_readonly

    @shutdown_readonly.setter
    def shutdown_readonly(self, shutdown_readonly):
        """Sets the shutdown_readonly of this NodeStateSmartfailExtended.

        This node is shutdown readonly (down_devs).  # noqa: E501

        :param shutdown_readonly: The shutdown_readonly of this NodeStateSmartfailExtended.  # noqa: E501
        :type: bool
        """

        self._shutdown_readonly = shutdown_readonly

    @property
    def smartfailed(self):
        """Gets the smartfailed of this NodeStateSmartfailExtended.  # noqa: E501

        This node is smartfailed (soft_devs).  # noqa: E501

        :return: The smartfailed of this NodeStateSmartfailExtended.  # noqa: E501
        :rtype: bool
        """
        return self._smartfailed

    @smartfailed.setter
    def smartfailed(self, smartfailed):
        """Sets the smartfailed of this NodeStateSmartfailExtended.

        This node is smartfailed (soft_devs).  # noqa: E501

        :param smartfailed: The smartfailed of this NodeStateSmartfailExtended.  # noqa: E501
        :type: bool
        """

        self._smartfailed = smartfailed

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
        if issubclass(NodeStateSmartfailExtended, dict):
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
        if not isinstance(other, NodeStateSmartfailExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
