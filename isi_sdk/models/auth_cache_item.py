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


class AuthCacheItem(object):
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
        'all': 'str',
        'gid': 'int',
        'group_name': 'str',
        'provider': 'str',
        'sid': 'str',
        'uid': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'all': 'all',
        'gid': 'gid',
        'group_name': 'group_name',
        'provider': 'provider',
        'sid': 'sid',
        'uid': 'uid',
        'user_name': 'user_name'
    }

    def __init__(self, all=None, gid=None, group_name=None, provider=None, sid=None, uid=None, user_name=None):  # noqa: E501
        """AuthCacheItem - a model defined in Swagger"""  # noqa: E501

        self._all = None
        self._gid = None
        self._group_name = None
        self._provider = None
        self._sid = None
        self._uid = None
        self._user_name = None
        self.discriminator = None

        if all is not None:
            self.all = all
        if gid is not None:
            self.gid = gid
        if group_name is not None:
            self.group_name = group_name
        if provider is not None:
            self.provider = provider
        if sid is not None:
            self.sid = sid
        if uid is not None:
            self.uid = uid
        if user_name is not None:
            self.user_name = user_name

    @property
    def all(self):
        """Gets the all of this AuthCacheItem.  # noqa: E501

        Flush all objects in cache for access zone.  # noqa: E501

        :return: The all of this AuthCacheItem.  # noqa: E501
        :rtype: str
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this AuthCacheItem.

        Flush all objects in cache for access zone.  # noqa: E501

        :param all: The all of this AuthCacheItem.  # noqa: E501
        :type: str
        """

        self._all = all

    @property
    def gid(self):
        """Gets the gid of this AuthCacheItem.  # noqa: E501

        Flush objects in cache for access zone specified by GID.  # noqa: E501

        :return: The gid of this AuthCacheItem.  # noqa: E501
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this AuthCacheItem.

        Flush objects in cache for access zone specified by GID.  # noqa: E501

        :param gid: The gid of this AuthCacheItem.  # noqa: E501
        :type: int
        """

        self._gid = gid

    @property
    def group_name(self):
        """Gets the group_name of this AuthCacheItem.  # noqa: E501

        Flush objects in cache for access zone specified by group name.  # noqa: E501

        :return: The group_name of this AuthCacheItem.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this AuthCacheItem.

        Flush objects in cache for access zone specified by group name.  # noqa: E501

        :param group_name: The group_name of this AuthCacheItem.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def provider(self):
        """Gets the provider of this AuthCacheItem.  # noqa: E501

        Flush objects in cache for access zone specified by authentication provider.  # noqa: E501

        :return: The provider of this AuthCacheItem.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AuthCacheItem.

        Flush objects in cache for access zone specified by authentication provider.  # noqa: E501

        :param provider: The provider of this AuthCacheItem.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def sid(self):
        """Gets the sid of this AuthCacheItem.  # noqa: E501

        Flush objects in cache for access zone specified by SID.  # noqa: E501

        :return: The sid of this AuthCacheItem.  # noqa: E501
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this AuthCacheItem.

        Flush objects in cache for access zone specified by SID.  # noqa: E501

        :param sid: The sid of this AuthCacheItem.  # noqa: E501
        :type: str
        """

        self._sid = sid

    @property
    def uid(self):
        """Gets the uid of this AuthCacheItem.  # noqa: E501

        Flush objects in cache for access zone specified by UID.  # noqa: E501

        :return: The uid of this AuthCacheItem.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AuthCacheItem.

        Flush objects in cache for access zone specified by UID.  # noqa: E501

        :param uid: The uid of this AuthCacheItem.  # noqa: E501
        :type: int
        """

        self._uid = uid

    @property
    def user_name(self):
        """Gets the user_name of this AuthCacheItem.  # noqa: E501

        Flush objects in cache for access zone specified by user name.  # noqa: E501

        :return: The user_name of this AuthCacheItem.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AuthCacheItem.

        Flush objects in cache for access zone specified by user name.  # noqa: E501

        :param user_name: The user_name of this AuthCacheItem.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if not isinstance(other, AuthCacheItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
