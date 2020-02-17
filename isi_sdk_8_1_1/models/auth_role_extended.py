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


class AuthRoleExtended(object):
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
        'description': 'str',
        'members': 'list[AuthAccessAccessItemFileGroup]',
        'name': 'str',
        'privileges': 'list[AuthIdNtokenPrivilegeItem]',
        'id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'members': 'members',
        'name': 'name',
        'privileges': 'privileges',
        'id': 'id'
    }

    def __init__(self, description=None, members=None, name=None, privileges=None, id=None):  # noqa: E501
        """AuthRoleExtended - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._members = None
        self._name = None
        self._privileges = None
        self._id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.members = members
        self.name = name
        self.privileges = privileges
        self.id = id

    @property
    def description(self):
        """Gets the description of this AuthRoleExtended.  # noqa: E501

        Specifies the description of the role.  # noqa: E501

        :return: The description of this AuthRoleExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AuthRoleExtended.

        Specifies the description of the role.  # noqa: E501

        :param description: The description of this AuthRoleExtended.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def members(self):
        """Gets the members of this AuthRoleExtended.  # noqa: E501

        Specifies the users or groups that have this role.  # noqa: E501

        :return: The members of this AuthRoleExtended.  # noqa: E501
        :rtype: list[AuthAccessAccessItemFileGroup]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this AuthRoleExtended.

        Specifies the users or groups that have this role.  # noqa: E501

        :param members: The members of this AuthRoleExtended.  # noqa: E501
        :type: list[AuthAccessAccessItemFileGroup]
        """
        if members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")  # noqa: E501

        self._members = members

    @property
    def name(self):
        """Gets the name of this AuthRoleExtended.  # noqa: E501

        Specifies the name of the role.  # noqa: E501

        :return: The name of this AuthRoleExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthRoleExtended.

        Specifies the name of the role.  # noqa: E501

        :param name: The name of this AuthRoleExtended.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def privileges(self):
        """Gets the privileges of this AuthRoleExtended.  # noqa: E501

        Specifies the privileges granted by this role.  # noqa: E501

        :return: The privileges of this AuthRoleExtended.  # noqa: E501
        :rtype: list[AuthIdNtokenPrivilegeItem]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this AuthRoleExtended.

        Specifies the privileges granted by this role.  # noqa: E501

        :param privileges: The privileges of this AuthRoleExtended.  # noqa: E501
        :type: list[AuthIdNtokenPrivilegeItem]
        """
        if privileges is None:
            raise ValueError("Invalid value for `privileges`, must not be `None`")  # noqa: E501

        self._privileges = privileges

    @property
    def id(self):
        """Gets the id of this AuthRoleExtended.  # noqa: E501

        Specifies the ID of the role.  # noqa: E501

        :return: The id of this AuthRoleExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthRoleExtended.

        Specifies the ID of the role.  # noqa: E501

        :param id: The id of this AuthRoleExtended.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

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
        if issubclass(AuthRoleExtended, dict):
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
        if not isinstance(other, AuthRoleExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
