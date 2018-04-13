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


class AuthLdapTemplatesLdapFieldTemplateItem(object):
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
        'cn_attribute': 'str',
        'crypt_password_attribute': 'str',
        'email_attribute': 'str',
        'gecos_attribute': 'str',
        'gid_attribute': 'str',
        'group_filter': 'str',
        'group_members_attribute': 'str',
        'homedir_attribute': 'str',
        'id': 'str',
        'name_attribute': 'str',
        'netgroup_filter': 'str',
        'netgroup_members_attribute': 'str',
        'netgroup_triple_attribute': 'str',
        'nt_password_attribute': 'str',
        'shadow_expire_attribute': 'str',
        'shadow_flag_attribute': 'str',
        'shadow_inactive_attribute': 'str',
        'shadow_last_change_attribute': 'str',
        'shadow_max_attribute': 'str',
        'shadow_min_attribute': 'str',
        'shadow_user_filter': 'str',
        'shadow_warning_attribute': 'str',
        'shell_attribute': 'str',
        'uid_attribute': 'str',
        'unique_group_members_attribute': 'str',
        'user_filter': 'str'
    }

    attribute_map = {
        'cn_attribute': 'cn_attribute',
        'crypt_password_attribute': 'crypt_password_attribute',
        'email_attribute': 'email_attribute',
        'gecos_attribute': 'gecos_attribute',
        'gid_attribute': 'gid_attribute',
        'group_filter': 'group_filter',
        'group_members_attribute': 'group_members_attribute',
        'homedir_attribute': 'homedir_attribute',
        'id': 'id',
        'name_attribute': 'name_attribute',
        'netgroup_filter': 'netgroup_filter',
        'netgroup_members_attribute': 'netgroup_members_attribute',
        'netgroup_triple_attribute': 'netgroup_triple_attribute',
        'nt_password_attribute': 'nt_password_attribute',
        'shadow_expire_attribute': 'shadow_expire_attribute',
        'shadow_flag_attribute': 'shadow_flag_attribute',
        'shadow_inactive_attribute': 'shadow_inactive_attribute',
        'shadow_last_change_attribute': 'shadow_last_change_attribute',
        'shadow_max_attribute': 'shadow_max_attribute',
        'shadow_min_attribute': 'shadow_min_attribute',
        'shadow_user_filter': 'shadow_user_filter',
        'shadow_warning_attribute': 'shadow_warning_attribute',
        'shell_attribute': 'shell_attribute',
        'uid_attribute': 'uid_attribute',
        'unique_group_members_attribute': 'unique_group_members_attribute',
        'user_filter': 'user_filter'
    }

    def __init__(self, cn_attribute=None, crypt_password_attribute=None, email_attribute=None, gecos_attribute=None, gid_attribute=None, group_filter=None, group_members_attribute=None, homedir_attribute=None, id=None, name_attribute=None, netgroup_filter=None, netgroup_members_attribute=None, netgroup_triple_attribute=None, nt_password_attribute=None, shadow_expire_attribute=None, shadow_flag_attribute=None, shadow_inactive_attribute=None, shadow_last_change_attribute=None, shadow_max_attribute=None, shadow_min_attribute=None, shadow_user_filter=None, shadow_warning_attribute=None, shell_attribute=None, uid_attribute=None, unique_group_members_attribute=None, user_filter=None):  # noqa: E501
        """AuthLdapTemplatesLdapFieldTemplateItem - a model defined in Swagger"""  # noqa: E501

        self._cn_attribute = None
        self._crypt_password_attribute = None
        self._email_attribute = None
        self._gecos_attribute = None
        self._gid_attribute = None
        self._group_filter = None
        self._group_members_attribute = None
        self._homedir_attribute = None
        self._id = None
        self._name_attribute = None
        self._netgroup_filter = None
        self._netgroup_members_attribute = None
        self._netgroup_triple_attribute = None
        self._nt_password_attribute = None
        self._shadow_expire_attribute = None
        self._shadow_flag_attribute = None
        self._shadow_inactive_attribute = None
        self._shadow_last_change_attribute = None
        self._shadow_max_attribute = None
        self._shadow_min_attribute = None
        self._shadow_user_filter = None
        self._shadow_warning_attribute = None
        self._shell_attribute = None
        self._uid_attribute = None
        self._unique_group_members_attribute = None
        self._user_filter = None
        self.discriminator = None

        if cn_attribute is not None:
            self.cn_attribute = cn_attribute
        if crypt_password_attribute is not None:
            self.crypt_password_attribute = crypt_password_attribute
        if email_attribute is not None:
            self.email_attribute = email_attribute
        if gecos_attribute is not None:
            self.gecos_attribute = gecos_attribute
        if gid_attribute is not None:
            self.gid_attribute = gid_attribute
        if group_filter is not None:
            self.group_filter = group_filter
        if group_members_attribute is not None:
            self.group_members_attribute = group_members_attribute
        if homedir_attribute is not None:
            self.homedir_attribute = homedir_attribute
        if id is not None:
            self.id = id
        if name_attribute is not None:
            self.name_attribute = name_attribute
        if netgroup_filter is not None:
            self.netgroup_filter = netgroup_filter
        if netgroup_members_attribute is not None:
            self.netgroup_members_attribute = netgroup_members_attribute
        if netgroup_triple_attribute is not None:
            self.netgroup_triple_attribute = netgroup_triple_attribute
        if nt_password_attribute is not None:
            self.nt_password_attribute = nt_password_attribute
        if shadow_expire_attribute is not None:
            self.shadow_expire_attribute = shadow_expire_attribute
        if shadow_flag_attribute is not None:
            self.shadow_flag_attribute = shadow_flag_attribute
        if shadow_inactive_attribute is not None:
            self.shadow_inactive_attribute = shadow_inactive_attribute
        if shadow_last_change_attribute is not None:
            self.shadow_last_change_attribute = shadow_last_change_attribute
        if shadow_max_attribute is not None:
            self.shadow_max_attribute = shadow_max_attribute
        if shadow_min_attribute is not None:
            self.shadow_min_attribute = shadow_min_attribute
        if shadow_user_filter is not None:
            self.shadow_user_filter = shadow_user_filter
        if shadow_warning_attribute is not None:
            self.shadow_warning_attribute = shadow_warning_attribute
        if shell_attribute is not None:
            self.shell_attribute = shell_attribute
        if uid_attribute is not None:
            self.uid_attribute = uid_attribute
        if unique_group_members_attribute is not None:
            self.unique_group_members_attribute = unique_group_members_attribute
        if user_filter is not None:
            self.user_filter = user_filter

    @property
    def cn_attribute(self):
        """Gets the cn_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Specifies canonical name.  # noqa: E501

        :return: The cn_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._cn_attribute

    @cn_attribute.setter
    def cn_attribute(self, cn_attribute):
        """Sets the cn_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Specifies canonical name.  # noqa: E501

        :param cn_attribute: The cn_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._cn_attribute = cn_attribute

    @property
    def crypt_password_attribute(self):
        """Gets the crypt_password_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets hashed password value.  # noqa: E501

        :return: The crypt_password_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._crypt_password_attribute

    @crypt_password_attribute.setter
    def crypt_password_attribute(self, crypt_password_attribute):
        """Sets the crypt_password_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets hashed password value.  # noqa: E501

        :param crypt_password_attribute: The crypt_password_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._crypt_password_attribute = crypt_password_attribute

    @property
    def email_attribute(self):
        """Gets the email_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP Email attribute.  # noqa: E501

        :return: The email_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._email_attribute

    @email_attribute.setter
    def email_attribute(self, email_attribute):
        """Sets the email_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP Email attribute.  # noqa: E501

        :param email_attribute: The email_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._email_attribute = email_attribute

    @property
    def gecos_attribute(self):
        """Gets the gecos_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP GECOS attribute.  # noqa: E501

        :return: The gecos_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._gecos_attribute

    @gecos_attribute.setter
    def gecos_attribute(self, gecos_attribute):
        """Sets the gecos_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP GECOS attribute.  # noqa: E501

        :param gecos_attribute: The gecos_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._gecos_attribute = gecos_attribute

    @property
    def gid_attribute(self):
        """Gets the gid_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP GID attribute.  # noqa: E501

        :return: The gid_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._gid_attribute

    @gid_attribute.setter
    def gid_attribute(self, gid_attribute):
        """Sets the gid_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP GID attribute.  # noqa: E501

        :param gid_attribute: The gid_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._gid_attribute = gid_attribute

    @property
    def group_filter(self):
        """Gets the group_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets LDAP filter for group objects.  # noqa: E501

        :return: The group_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._group_filter

    @group_filter.setter
    def group_filter(self, group_filter):
        """Sets the group_filter of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets LDAP filter for group objects.  # noqa: E501

        :param group_filter: The group_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._group_filter = group_filter

    @property
    def group_members_attribute(self):
        """Gets the group_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP Group Members attribute.  # noqa: E501

        :return: The group_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._group_members_attribute

    @group_members_attribute.setter
    def group_members_attribute(self, group_members_attribute):
        """Sets the group_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP Group Members attribute.  # noqa: E501

        :param group_members_attribute: The group_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._group_members_attribute = group_members_attribute

    @property
    def homedir_attribute(self):
        """Gets the homedir_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP Homedir attribute.  # noqa: E501

        :return: The homedir_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._homedir_attribute

    @homedir_attribute.setter
    def homedir_attribute(self, homedir_attribute):
        """Sets the homedir_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP Homedir attribute.  # noqa: E501

        :param homedir_attribute: The homedir_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._homedir_attribute = homedir_attribute

    @property
    def id(self):
        """Gets the id of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Specifies the ID of the LDAP provider field template.  # noqa: E501

        :return: The id of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthLdapTemplatesLdapFieldTemplateItem.

        Specifies the ID of the LDAP provider field template.  # noqa: E501

        :param id: The id of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name_attribute(self):
        """Gets the name_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP UID attribute, which is used as the login name.  # noqa: E501

        :return: The name_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._name_attribute

    @name_attribute.setter
    def name_attribute(self, name_attribute):
        """Sets the name_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP UID attribute, which is used as the login name.  # noqa: E501

        :param name_attribute: The name_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._name_attribute = name_attribute

    @property
    def netgroup_filter(self):
        """Gets the netgroup_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets LDAP filter for netgroup objects.  # noqa: E501

        :return: The netgroup_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._netgroup_filter

    @netgroup_filter.setter
    def netgroup_filter(self, netgroup_filter):
        """Sets the netgroup_filter of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets LDAP filter for netgroup objects.  # noqa: E501

        :param netgroup_filter: The netgroup_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._netgroup_filter = netgroup_filter

    @property
    def netgroup_members_attribute(self):
        """Gets the netgroup_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP Netgroup Members attribute.  # noqa: E501

        :return: The netgroup_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._netgroup_members_attribute

    @netgroup_members_attribute.setter
    def netgroup_members_attribute(self, netgroup_members_attribute):
        """Sets the netgroup_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP Netgroup Members attribute.  # noqa: E501

        :param netgroup_members_attribute: The netgroup_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._netgroup_members_attribute = netgroup_members_attribute

    @property
    def netgroup_triple_attribute(self):
        """Gets the netgroup_triple_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP Netgroup Triple attribute.  # noqa: E501

        :return: The netgroup_triple_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._netgroup_triple_attribute

    @netgroup_triple_attribute.setter
    def netgroup_triple_attribute(self, netgroup_triple_attribute):
        """Sets the netgroup_triple_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP Netgroup Triple attribute.  # noqa: E501

        :param netgroup_triple_attribute: The netgroup_triple_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._netgroup_triple_attribute = netgroup_triple_attribute

    @property
    def nt_password_attribute(self):
        """Gets the nt_password_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP NT Password attribute.  # noqa: E501

        :return: The nt_password_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._nt_password_attribute

    @nt_password_attribute.setter
    def nt_password_attribute(self, nt_password_attribute):
        """Sets the nt_password_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP NT Password attribute.  # noqa: E501

        :param nt_password_attribute: The nt_password_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._nt_password_attribute = nt_password_attribute

    @property
    def shadow_expire_attribute(self):
        """Gets the shadow_expire_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the absolute date to expire the account.  # noqa: E501

        :return: The shadow_expire_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._shadow_expire_attribute

    @shadow_expire_attribute.setter
    def shadow_expire_attribute(self, shadow_expire_attribute):
        """Sets the shadow_expire_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the absolute date to expire the account.  # noqa: E501

        :param shadow_expire_attribute: The shadow_expire_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._shadow_expire_attribute = shadow_expire_attribute

    @property
    def shadow_flag_attribute(self):
        """Gets the shadow_flag_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the section of the shadow map that is used to store the flag value.  # noqa: E501

        :return: The shadow_flag_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._shadow_flag_attribute

    @shadow_flag_attribute.setter
    def shadow_flag_attribute(self, shadow_flag_attribute):
        """Sets the shadow_flag_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the section of the shadow map that is used to store the flag value.  # noqa: E501

        :param shadow_flag_attribute: The shadow_flag_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._shadow_flag_attribute = shadow_flag_attribute

    @property
    def shadow_inactive_attribute(self):
        """Gets the shadow_inactive_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the number of days of inactivity that is allowed for the user.  # noqa: E501

        :return: The shadow_inactive_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._shadow_inactive_attribute

    @shadow_inactive_attribute.setter
    def shadow_inactive_attribute(self, shadow_inactive_attribute):
        """Sets the shadow_inactive_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the number of days of inactivity that is allowed for the user.  # noqa: E501

        :param shadow_inactive_attribute: The shadow_inactive_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._shadow_inactive_attribute = shadow_inactive_attribute

    @property
    def shadow_last_change_attribute(self):
        """Gets the shadow_last_change_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the last change of the shadow information.  # noqa: E501

        :return: The shadow_last_change_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._shadow_last_change_attribute

    @shadow_last_change_attribute.setter
    def shadow_last_change_attribute(self, shadow_last_change_attribute):
        """Sets the shadow_last_change_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the last change of the shadow information.  # noqa: E501

        :param shadow_last_change_attribute: The shadow_last_change_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._shadow_last_change_attribute = shadow_last_change_attribute

    @property
    def shadow_max_attribute(self):
        """Gets the shadow_max_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the maximum number of days a password can be valid.  # noqa: E501

        :return: The shadow_max_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._shadow_max_attribute

    @shadow_max_attribute.setter
    def shadow_max_attribute(self, shadow_max_attribute):
        """Sets the shadow_max_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the maximum number of days a password can be valid.  # noqa: E501

        :param shadow_max_attribute: The shadow_max_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._shadow_max_attribute = shadow_max_attribute

    @property
    def shadow_min_attribute(self):
        """Gets the shadow_min_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the minimum number of days between shadow changes.  # noqa: E501

        :return: The shadow_min_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._shadow_min_attribute

    @shadow_min_attribute.setter
    def shadow_min_attribute(self, shadow_min_attribute):
        """Sets the shadow_min_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the minimum number of days between shadow changes.  # noqa: E501

        :param shadow_min_attribute: The shadow_min_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._shadow_min_attribute = shadow_min_attribute

    @property
    def shadow_user_filter(self):
        """Gets the shadow_user_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets LDAP filter for shadow user objects.  # noqa: E501

        :return: The shadow_user_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._shadow_user_filter

    @shadow_user_filter.setter
    def shadow_user_filter(self, shadow_user_filter):
        """Sets the shadow_user_filter of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets LDAP filter for shadow user objects.  # noqa: E501

        :param shadow_user_filter: The shadow_user_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._shadow_user_filter = shadow_user_filter

    @property
    def shadow_warning_attribute(self):
        """Gets the shadow_warning_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the number of days before the password expires to warn the user.  # noqa: E501

        :return: The shadow_warning_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._shadow_warning_attribute

    @shadow_warning_attribute.setter
    def shadow_warning_attribute(self, shadow_warning_attribute):
        """Sets the shadow_warning_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the number of days before the password expires to warn the user.  # noqa: E501

        :param shadow_warning_attribute: The shadow_warning_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._shadow_warning_attribute = shadow_warning_attribute

    @property
    def shell_attribute(self):
        """Gets the shell_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP Shell attribute.  # noqa: E501

        :return: The shell_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._shell_attribute

    @shell_attribute.setter
    def shell_attribute(self, shell_attribute):
        """Sets the shell_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP Shell attribute.  # noqa: E501

        :param shell_attribute: The shell_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._shell_attribute = shell_attribute

    @property
    def uid_attribute(self):
        """Gets the uid_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP UID Number attribute.  # noqa: E501

        :return: The uid_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._uid_attribute

    @uid_attribute.setter
    def uid_attribute(self, uid_attribute):
        """Sets the uid_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP UID Number attribute.  # noqa: E501

        :param uid_attribute: The uid_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._uid_attribute = uid_attribute

    @property
    def unique_group_members_attribute(self):
        """Gets the unique_group_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets the LDAP Unique Group Members attribute.  # noqa: E501

        :return: The unique_group_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._unique_group_members_attribute

    @unique_group_members_attribute.setter
    def unique_group_members_attribute(self, unique_group_members_attribute):
        """Sets the unique_group_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets the LDAP Unique Group Members attribute.  # noqa: E501

        :param unique_group_members_attribute: The unique_group_members_attribute of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._unique_group_members_attribute = unique_group_members_attribute

    @property
    def user_filter(self):
        """Gets the user_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501

        Sets LDAP filter for user objects.  # noqa: E501

        :return: The user_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :rtype: str
        """
        return self._user_filter

    @user_filter.setter
    def user_filter(self, user_filter):
        """Sets the user_filter of this AuthLdapTemplatesLdapFieldTemplateItem.

        Sets LDAP filter for user objects.  # noqa: E501

        :param user_filter: The user_filter of this AuthLdapTemplatesLdapFieldTemplateItem.  # noqa: E501
        :type: str
        """

        self._user_filter = user_filter

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
        if not isinstance(other, AuthLdapTemplatesLdapFieldTemplateItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
