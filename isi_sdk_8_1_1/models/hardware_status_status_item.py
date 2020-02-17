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


class HardwareStatusStatusItem(object):
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
        'id': 'str',
        'nodepool_name': 'str',
        'unupgraded_lnns': 'list[int]',
        'upgrade_type': 'str',
        'upgraded_lnns': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'nodepool_name': 'nodepool_name',
        'unupgraded_lnns': 'unupgraded_lnns',
        'upgrade_type': 'upgrade_type',
        'upgraded_lnns': 'upgraded_lnns'
    }

    def __init__(self, id=None, nodepool_name=None, unupgraded_lnns=None, upgrade_type=None, upgraded_lnns=None):  # noqa: E501
        """HardwareStatusStatusItem - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._nodepool_name = None
        self._unupgraded_lnns = None
        self._upgrade_type = None
        self._upgraded_lnns = None
        self.discriminator = None

        self.id = id
        if nodepool_name is not None:
            self.nodepool_name = nodepool_name
        self.unupgraded_lnns = unupgraded_lnns
        self.upgrade_type = upgrade_type
        self.upgraded_lnns = upgraded_lnns

    @property
    def id(self):
        """Gets the id of this HardwareStatusStatusItem.  # noqa: E501

        The ID of this upgrade.  # noqa: E501

        :return: The id of this HardwareStatusStatusItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HardwareStatusStatusItem.

        The ID of this upgrade.  # noqa: E501

        :param id: The id of this HardwareStatusStatusItem.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def nodepool_name(self):
        """Gets the nodepool_name of this HardwareStatusStatusItem.  # noqa: E501

        Name of the upgrading pool.  # noqa: E501

        :return: The nodepool_name of this HardwareStatusStatusItem.  # noqa: E501
        :rtype: str
        """
        return self._nodepool_name

    @nodepool_name.setter
    def nodepool_name(self, nodepool_name):
        """Sets the nodepool_name of this HardwareStatusStatusItem.

        Name of the upgrading pool.  # noqa: E501

        :param nodepool_name: The nodepool_name of this HardwareStatusStatusItem.  # noqa: E501
        :type: str
        """

        self._nodepool_name = nodepool_name

    @property
    def unupgraded_lnns(self):
        """Gets the unupgraded_lnns of this HardwareStatusStatusItem.  # noqa: E501

        The lnns of the nodes in the pool that haven't been upgraded yet.  # noqa: E501

        :return: The unupgraded_lnns of this HardwareStatusStatusItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._unupgraded_lnns

    @unupgraded_lnns.setter
    def unupgraded_lnns(self, unupgraded_lnns):
        """Sets the unupgraded_lnns of this HardwareStatusStatusItem.

        The lnns of the nodes in the pool that haven't been upgraded yet.  # noqa: E501

        :param unupgraded_lnns: The unupgraded_lnns of this HardwareStatusStatusItem.  # noqa: E501
        :type: list[int]
        """
        if unupgraded_lnns is None:
            raise ValueError("Invalid value for `unupgraded_lnns`, must not be `None`")  # noqa: E501

        self._unupgraded_lnns = unupgraded_lnns

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this HardwareStatusStatusItem.  # noqa: E501

        The type of upgrade this is.  # noqa: E501

        :return: The upgrade_type of this HardwareStatusStatusItem.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this HardwareStatusStatusItem.

        The type of upgrade this is.  # noqa: E501

        :param upgrade_type: The upgrade_type of this HardwareStatusStatusItem.  # noqa: E501
        :type: str
        """
        if upgrade_type is None:
            raise ValueError("Invalid value for `upgrade_type`, must not be `None`")  # noqa: E501

        self._upgrade_type = upgrade_type

    @property
    def upgraded_lnns(self):
        """Gets the upgraded_lnns of this HardwareStatusStatusItem.  # noqa: E501

        The lnns of the nodes in the pool that have been successsfully upgraded.  # noqa: E501

        :return: The upgraded_lnns of this HardwareStatusStatusItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._upgraded_lnns

    @upgraded_lnns.setter
    def upgraded_lnns(self, upgraded_lnns):
        """Sets the upgraded_lnns of this HardwareStatusStatusItem.

        The lnns of the nodes in the pool that have been successsfully upgraded.  # noqa: E501

        :param upgraded_lnns: The upgraded_lnns of this HardwareStatusStatusItem.  # noqa: E501
        :type: list[int]
        """
        if upgraded_lnns is None:
            raise ValueError("Invalid value for `upgraded_lnns`, must not be `None`")  # noqa: E501

        self._upgraded_lnns = upgraded_lnns

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
        if issubclass(HardwareStatusStatusItem, dict):
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
        if not isinstance(other, HardwareStatusStatusItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
