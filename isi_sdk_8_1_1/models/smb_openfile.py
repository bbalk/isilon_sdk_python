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


class SmbOpenfile(object):
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
        'file': 'str',
        'id': 'int',
        'locks': 'int',
        'permissions': 'list[str]',
        'user': 'str'
    }

    attribute_map = {
        'file': 'file',
        'id': 'id',
        'locks': 'locks',
        'permissions': 'permissions',
        'user': 'user'
    }

    def __init__(self, file=None, id=None, locks=None, permissions=None, user=None):  # noqa: E501
        """SmbOpenfile - a model defined in Swagger"""  # noqa: E501

        self._file = None
        self._id = None
        self._locks = None
        self._permissions = None
        self._user = None
        self.discriminator = None

        self.file = file
        self.id = id
        self.locks = locks
        self.permissions = permissions
        self.user = user

    @property
    def file(self):
        """Gets the file of this SmbOpenfile.  # noqa: E501

        Path of file within /ifs.  # noqa: E501

        :return: The file of this SmbOpenfile.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this SmbOpenfile.

        Path of file within /ifs.  # noqa: E501

        :param file: The file of this SmbOpenfile.  # noqa: E501
        :type: str
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def id(self):
        """Gets the id of this SmbOpenfile.  # noqa: E501

        The file ID.  # noqa: E501

        :return: The id of this SmbOpenfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmbOpenfile.

        The file ID.  # noqa: E501

        :param id: The id of this SmbOpenfile.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def locks(self):
        """Gets the locks of this SmbOpenfile.  # noqa: E501

        Number of locks user holds on file.  # noqa: E501

        :return: The locks of this SmbOpenfile.  # noqa: E501
        :rtype: int
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """Sets the locks of this SmbOpenfile.

        Number of locks user holds on file.  # noqa: E501

        :param locks: The locks of this SmbOpenfile.  # noqa: E501
        :type: int
        """
        if locks is None:
            raise ValueError("Invalid value for `locks`, must not be `None`")  # noqa: E501

        self._locks = locks

    @property
    def permissions(self):
        """Gets the permissions of this SmbOpenfile.  # noqa: E501

        The user's permissions on file.  # noqa: E501

        :return: The permissions of this SmbOpenfile.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this SmbOpenfile.

        The user's permissions on file.  # noqa: E501

        :param permissions: The permissions of this SmbOpenfile.  # noqa: E501
        :type: list[str]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501
        allowed_values = ["read", "write", "create"]  # noqa: E501
        if not set(permissions).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._permissions = permissions

    @property
    def user(self):
        """Gets the user of this SmbOpenfile.  # noqa: E501

        User holding file open.  # noqa: E501

        :return: The user of this SmbOpenfile.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SmbOpenfile.

        User holding file open.  # noqa: E501

        :param user: The user of this SmbOpenfile.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if issubclass(SmbOpenfile, dict):
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
        if not isinstance(other, SmbOpenfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
