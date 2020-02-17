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


class StoragepoolTierExtended(object):
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
        'children': 'list[str]',
        'name': 'str',
        'id': 'int',
        'lnns': 'list[int]',
        'usage': 'StoragepoolTierUsage'
    }

    attribute_map = {
        'children': 'children',
        'name': 'name',
        'id': 'id',
        'lnns': 'lnns',
        'usage': 'usage'
    }

    def __init__(self, children=None, name=None, id=None, lnns=None, usage=None):  # noqa: E501
        """StoragepoolTierExtended - a model defined in Swagger"""  # noqa: E501

        self._children = None
        self._name = None
        self._id = None
        self._lnns = None
        self._usage = None
        self.discriminator = None

        if children is not None:
            self.children = children
        self.name = name
        self.id = id
        self.lnns = lnns
        self.usage = usage

    @property
    def children(self):
        """Gets the children of this StoragepoolTierExtended.  # noqa: E501

        The names or IDs of the tier's children.  # noqa: E501

        :return: The children of this StoragepoolTierExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this StoragepoolTierExtended.

        The names or IDs of the tier's children.  # noqa: E501

        :param children: The children of this StoragepoolTierExtended.  # noqa: E501
        :type: list[str]
        """

        self._children = children

    @property
    def name(self):
        """Gets the name of this StoragepoolTierExtended.  # noqa: E501

        The tier name.  # noqa: E501

        :return: The name of this StoragepoolTierExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoragepoolTierExtended.

        The tier name.  # noqa: E501

        :param name: The name of this StoragepoolTierExtended.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this StoragepoolTierExtended.  # noqa: E501

        The system ID given to the tier.  # noqa: E501

        :return: The id of this StoragepoolTierExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoragepoolTierExtended.

        The system ID given to the tier.  # noqa: E501

        :param id: The id of this StoragepoolTierExtended.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def lnns(self):
        """Gets the lnns of this StoragepoolTierExtended.  # noqa: E501

        The nodes that are part of this tier.  # noqa: E501

        :return: The lnns of this StoragepoolTierExtended.  # noqa: E501
        :rtype: list[int]
        """
        return self._lnns

    @lnns.setter
    def lnns(self, lnns):
        """Sets the lnns of this StoragepoolTierExtended.

        The nodes that are part of this tier.  # noqa: E501

        :param lnns: The lnns of this StoragepoolTierExtended.  # noqa: E501
        :type: list[int]
        """
        if lnns is None:
            raise ValueError("Invalid value for `lnns`, must not be `None`")  # noqa: E501

        self._lnns = lnns

    @property
    def usage(self):
        """Gets the usage of this StoragepoolTierExtended.  # noqa: E501

        Total pool usage.  # noqa: E501

        :return: The usage of this StoragepoolTierExtended.  # noqa: E501
        :rtype: StoragepoolTierUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this StoragepoolTierExtended.

        Total pool usage.  # noqa: E501

        :param usage: The usage of this StoragepoolTierExtended.  # noqa: E501
        :type: StoragepoolTierUsage
        """
        if usage is None:
            raise ValueError("Invalid value for `usage`, must not be `None`")  # noqa: E501

        self._usage = usage

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
        if issubclass(StoragepoolTierExtended, dict):
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
        if not isinstance(other, StoragepoolTierExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other