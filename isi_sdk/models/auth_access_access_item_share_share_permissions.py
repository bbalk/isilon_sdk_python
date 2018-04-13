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

from isi_sdk_8_0_1.models.auth_access_access_item_share_share_permissions_share_relevant_ace import AuthAccessAccessItemShareSharePermissionsShareRelevantAce  # noqa: F401,E501


class AuthAccessAccessItemShareSharePermissions(object):
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
        'expected_permissions': 'str',
        'impersonate_guest': 'bool',
        'impersonate_user': 'bool',
        'run_as_root': 'bool',
        'share_relevant_aces': 'list[AuthAccessAccessItemShareSharePermissionsShareRelevantAce]'
    }

    attribute_map = {
        'expected_permissions': 'expected_permissions',
        'impersonate_guest': 'impersonate_guest',
        'impersonate_user': 'impersonate_user',
        'run_as_root': 'run_as_root',
        'share_relevant_aces': 'share_relevant_aces'
    }

    def __init__(self, expected_permissions=None, impersonate_guest=None, impersonate_user=None, run_as_root=None, share_relevant_aces=None):  # noqa: E501
        """AuthAccessAccessItemShareSharePermissions - a model defined in Swagger"""  # noqa: E501

        self._expected_permissions = None
        self._impersonate_guest = None
        self._impersonate_user = None
        self._run_as_root = None
        self._share_relevant_aces = None
        self.discriminator = None

        if expected_permissions is not None:
            self.expected_permissions = expected_permissions
        if impersonate_guest is not None:
            self.impersonate_guest = impersonate_guest
        if impersonate_user is not None:
            self.impersonate_user = impersonate_user
        if run_as_root is not None:
            self.run_as_root = run_as_root
        if share_relevant_aces is not None:
            self.share_relevant_aces = share_relevant_aces

    @property
    def expected_permissions(self):
        """Gets the expected_permissions of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501

        Returns Share level permissions for the user.{ 'read' , 'write' , 'full' or 'none' will be the values}  # noqa: E501

        :return: The expected_permissions of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :rtype: str
        """
        return self._expected_permissions

    @expected_permissions.setter
    def expected_permissions(self, expected_permissions):
        """Sets the expected_permissions of this AuthAccessAccessItemShareSharePermissions.

        Returns Share level permissions for the user.{ 'read' , 'write' , 'full' or 'none' will be the values}  # noqa: E501

        :param expected_permissions: The expected_permissions of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :type: str
        """

        self._expected_permissions = expected_permissions

    @property
    def impersonate_guest(self):
        """Gets the impersonate_guest of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501

        Returns whether impersonate guest setting is enabled for the user on the share.  # noqa: E501

        :return: The impersonate_guest of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._impersonate_guest

    @impersonate_guest.setter
    def impersonate_guest(self, impersonate_guest):
        """Sets the impersonate_guest of this AuthAccessAccessItemShareSharePermissions.

        Returns whether impersonate guest setting is enabled for the user on the share.  # noqa: E501

        :param impersonate_guest: The impersonate_guest of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :type: bool
        """

        self._impersonate_guest = impersonate_guest

    @property
    def impersonate_user(self):
        """Gets the impersonate_user of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501

        Returns whether impersonate user setting is enabled on the share  # noqa: E501

        :return: The impersonate_user of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._impersonate_user

    @impersonate_user.setter
    def impersonate_user(self, impersonate_user):
        """Sets the impersonate_user of this AuthAccessAccessItemShareSharePermissions.

        Returns whether impersonate user setting is enabled on the share  # noqa: E501

        :param impersonate_user: The impersonate_user of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :type: bool
        """

        self._impersonate_user = impersonate_user

    @property
    def run_as_root(self):
        """Gets the run_as_root of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501

        Returns whether run as root is enabled for the user on the share  # noqa: E501

        :return: The run_as_root of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._run_as_root

    @run_as_root.setter
    def run_as_root(self, run_as_root):
        """Sets the run_as_root of this AuthAccessAccessItemShareSharePermissions.

        Returns whether run as root is enabled for the user on the share  # noqa: E501

        :param run_as_root: The run_as_root of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :type: bool
        """

        self._run_as_root = run_as_root

    @property
    def share_relevant_aces(self):
        """Gets the share_relevant_aces of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501

        Specifies a list of the relevant Access Control Entries withrespect to the user in the share.  # noqa: E501

        :return: The share_relevant_aces of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :rtype: list[AuthAccessAccessItemShareSharePermissionsShareRelevantAce]
        """
        return self._share_relevant_aces

    @share_relevant_aces.setter
    def share_relevant_aces(self, share_relevant_aces):
        """Sets the share_relevant_aces of this AuthAccessAccessItemShareSharePermissions.

        Specifies a list of the relevant Access Control Entries withrespect to the user in the share.  # noqa: E501

        :param share_relevant_aces: The share_relevant_aces of this AuthAccessAccessItemShareSharePermissions.  # noqa: E501
        :type: list[AuthAccessAccessItemShareSharePermissionsShareRelevantAce]
        """

        self._share_relevant_aces = share_relevant_aces

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
        if not isinstance(other, AuthAccessAccessItemShareSharePermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
