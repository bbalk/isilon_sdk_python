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


class SnapshotSettingsSettings(object):
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
        'autocreate': 'bool',
        'autodelete': 'bool',
        'global_visible_accessible': 'bool',
        'local_root_accessible': 'bool',
        'local_root_visible': 'bool',
        'local_subdir_accessible': 'bool',
        'nfs_root_accessible': 'bool',
        'nfs_root_visible': 'bool',
        'nfs_subdir_accessible': 'bool',
        'reserve': 'float',
        'service': 'bool',
        'smb_root_accessible': 'bool',
        'smb_root_visible': 'bool',
        'smb_subdir_accessible': 'bool'
    }

    attribute_map = {
        'autocreate': 'autocreate',
        'autodelete': 'autodelete',
        'global_visible_accessible': 'global_visible_accessible',
        'local_root_accessible': 'local_root_accessible',
        'local_root_visible': 'local_root_visible',
        'local_subdir_accessible': 'local_subdir_accessible',
        'nfs_root_accessible': 'nfs_root_accessible',
        'nfs_root_visible': 'nfs_root_visible',
        'nfs_subdir_accessible': 'nfs_subdir_accessible',
        'reserve': 'reserve',
        'service': 'service',
        'smb_root_accessible': 'smb_root_accessible',
        'smb_root_visible': 'smb_root_visible',
        'smb_subdir_accessible': 'smb_subdir_accessible'
    }

    def __init__(self, autocreate=None, autodelete=None, global_visible_accessible=None, local_root_accessible=None, local_root_visible=None, local_subdir_accessible=None, nfs_root_accessible=None, nfs_root_visible=None, nfs_subdir_accessible=None, reserve=None, service=None, smb_root_accessible=None, smb_root_visible=None, smb_subdir_accessible=None):  # noqa: E501
        """SnapshotSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._autocreate = None
        self._autodelete = None
        self._global_visible_accessible = None
        self._local_root_accessible = None
        self._local_root_visible = None
        self._local_subdir_accessible = None
        self._nfs_root_accessible = None
        self._nfs_root_visible = None
        self._nfs_subdir_accessible = None
        self._reserve = None
        self._service = None
        self._smb_root_accessible = None
        self._smb_root_visible = None
        self._smb_subdir_accessible = None
        self.discriminator = None

        self.autocreate = autocreate
        self.autodelete = autodelete
        self.global_visible_accessible = global_visible_accessible
        self.local_root_accessible = local_root_accessible
        self.local_root_visible = local_root_visible
        self.local_subdir_accessible = local_subdir_accessible
        self.nfs_root_accessible = nfs_root_accessible
        self.nfs_root_visible = nfs_root_visible
        self.nfs_subdir_accessible = nfs_subdir_accessible
        self.reserve = reserve
        self.service = service
        self.smb_root_accessible = smb_root_accessible
        self.smb_root_visible = smb_root_visible
        self.smb_subdir_accessible = smb_subdir_accessible

    @property
    def autocreate(self):
        """Gets the autocreate of this SnapshotSettingsSettings.  # noqa: E501

        True if the scheduled snapshot creation services is on.  # noqa: E501

        :return: The autocreate of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._autocreate

    @autocreate.setter
    def autocreate(self, autocreate):
        """Sets the autocreate of this SnapshotSettingsSettings.

        True if the scheduled snapshot creation services is on.  # noqa: E501

        :param autocreate: The autocreate of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if autocreate is None:
            raise ValueError("Invalid value for `autocreate`, must not be `None`")  # noqa: E501

        self._autocreate = autocreate

    @property
    def autodelete(self):
        """Gets the autodelete of this SnapshotSettingsSettings.  # noqa: E501

        True if the scheduled snapshot deletion services is on.  # noqa: E501

        :return: The autodelete of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._autodelete

    @autodelete.setter
    def autodelete(self, autodelete):
        """Sets the autodelete of this SnapshotSettingsSettings.

        True if the scheduled snapshot deletion services is on.  # noqa: E501

        :param autodelete: The autodelete of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if autodelete is None:
            raise ValueError("Invalid value for `autodelete`, must not be `None`")  # noqa: E501

        self._autodelete = autodelete

    @property
    def global_visible_accessible(self):
        """Gets the global_visible_accessible of this SnapshotSettingsSettings.  # noqa: E501

        Global switch for other accessible and visible settings.  # noqa: E501

        :return: The global_visible_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._global_visible_accessible

    @global_visible_accessible.setter
    def global_visible_accessible(self, global_visible_accessible):
        """Sets the global_visible_accessible of this SnapshotSettingsSettings.

        Global switch for other accessible and visible settings.  # noqa: E501

        :param global_visible_accessible: The global_visible_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if global_visible_accessible is None:
            raise ValueError("Invalid value for `global_visible_accessible`, must not be `None`")  # noqa: E501

        self._global_visible_accessible = global_visible_accessible

    @property
    def local_root_accessible(self):
        """Gets the local_root_accessible of this SnapshotSettingsSettings.  # noqa: E501

        True if root .snapshot directory is accessible locally.  # noqa: E501

        :return: The local_root_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._local_root_accessible

    @local_root_accessible.setter
    def local_root_accessible(self, local_root_accessible):
        """Sets the local_root_accessible of this SnapshotSettingsSettings.

        True if root .snapshot directory is accessible locally.  # noqa: E501

        :param local_root_accessible: The local_root_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if local_root_accessible is None:
            raise ValueError("Invalid value for `local_root_accessible`, must not be `None`")  # noqa: E501

        self._local_root_accessible = local_root_accessible

    @property
    def local_root_visible(self):
        """Gets the local_root_visible of this SnapshotSettingsSettings.  # noqa: E501

        True if root .snapshot directory is visible locally.  # noqa: E501

        :return: The local_root_visible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._local_root_visible

    @local_root_visible.setter
    def local_root_visible(self, local_root_visible):
        """Sets the local_root_visible of this SnapshotSettingsSettings.

        True if root .snapshot directory is visible locally.  # noqa: E501

        :param local_root_visible: The local_root_visible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if local_root_visible is None:
            raise ValueError("Invalid value for `local_root_visible`, must not be `None`")  # noqa: E501

        self._local_root_visible = local_root_visible

    @property
    def local_subdir_accessible(self):
        """Gets the local_subdir_accessible of this SnapshotSettingsSettings.  # noqa: E501

        True if sub-directory .snapshot directory is accessible locally.  # noqa: E501

        :return: The local_subdir_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._local_subdir_accessible

    @local_subdir_accessible.setter
    def local_subdir_accessible(self, local_subdir_accessible):
        """Sets the local_subdir_accessible of this SnapshotSettingsSettings.

        True if sub-directory .snapshot directory is accessible locally.  # noqa: E501

        :param local_subdir_accessible: The local_subdir_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if local_subdir_accessible is None:
            raise ValueError("Invalid value for `local_subdir_accessible`, must not be `None`")  # noqa: E501

        self._local_subdir_accessible = local_subdir_accessible

    @property
    def nfs_root_accessible(self):
        """Gets the nfs_root_accessible of this SnapshotSettingsSettings.  # noqa: E501

        True if root .snapshot directory is accessible over NFS.  # noqa: E501

        :return: The nfs_root_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfs_root_accessible

    @nfs_root_accessible.setter
    def nfs_root_accessible(self, nfs_root_accessible):
        """Sets the nfs_root_accessible of this SnapshotSettingsSettings.

        True if root .snapshot directory is accessible over NFS.  # noqa: E501

        :param nfs_root_accessible: The nfs_root_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if nfs_root_accessible is None:
            raise ValueError("Invalid value for `nfs_root_accessible`, must not be `None`")  # noqa: E501

        self._nfs_root_accessible = nfs_root_accessible

    @property
    def nfs_root_visible(self):
        """Gets the nfs_root_visible of this SnapshotSettingsSettings.  # noqa: E501

        True if root .snapshot directory is visible over NFS.  # noqa: E501

        :return: The nfs_root_visible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfs_root_visible

    @nfs_root_visible.setter
    def nfs_root_visible(self, nfs_root_visible):
        """Sets the nfs_root_visible of this SnapshotSettingsSettings.

        True if root .snapshot directory is visible over NFS.  # noqa: E501

        :param nfs_root_visible: The nfs_root_visible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if nfs_root_visible is None:
            raise ValueError("Invalid value for `nfs_root_visible`, must not be `None`")  # noqa: E501

        self._nfs_root_visible = nfs_root_visible

    @property
    def nfs_subdir_accessible(self):
        """Gets the nfs_subdir_accessible of this SnapshotSettingsSettings.  # noqa: E501

        True if sub-directory .snapshot directory is accessible over NFS.  # noqa: E501

        :return: The nfs_subdir_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._nfs_subdir_accessible

    @nfs_subdir_accessible.setter
    def nfs_subdir_accessible(self, nfs_subdir_accessible):
        """Sets the nfs_subdir_accessible of this SnapshotSettingsSettings.

        True if sub-directory .snapshot directory is accessible over NFS.  # noqa: E501

        :param nfs_subdir_accessible: The nfs_subdir_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if nfs_subdir_accessible is None:
            raise ValueError("Invalid value for `nfs_subdir_accessible`, must not be `None`")  # noqa: E501

        self._nfs_subdir_accessible = nfs_subdir_accessible

    @property
    def reserve(self):
        """Gets the reserve of this SnapshotSettingsSettings.  # noqa: E501

        Percentage of space to reserve for snapshots.  # noqa: E501

        :return: The reserve of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: float
        """
        return self._reserve

    @reserve.setter
    def reserve(self, reserve):
        """Sets the reserve of this SnapshotSettingsSettings.

        Percentage of space to reserve for snapshots.  # noqa: E501

        :param reserve: The reserve of this SnapshotSettingsSettings.  # noqa: E501
        :type: float
        """
        if reserve is None:
            raise ValueError("Invalid value for `reserve`, must not be `None`")  # noqa: E501

        self._reserve = reserve

    @property
    def service(self):
        """Gets the service of this SnapshotSettingsSettings.  # noqa: E501

        True if the system allows snapshot creation.  # noqa: E501

        :return: The service of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this SnapshotSettingsSettings.

        True if the system allows snapshot creation.  # noqa: E501

        :param service: The service of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def smb_root_accessible(self):
        """Gets the smb_root_accessible of this SnapshotSettingsSettings.  # noqa: E501

        True if root .snapshot directory is accessible over SMB.  # noqa: E501

        :return: The smb_root_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._smb_root_accessible

    @smb_root_accessible.setter
    def smb_root_accessible(self, smb_root_accessible):
        """Sets the smb_root_accessible of this SnapshotSettingsSettings.

        True if root .snapshot directory is accessible over SMB.  # noqa: E501

        :param smb_root_accessible: The smb_root_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if smb_root_accessible is None:
            raise ValueError("Invalid value for `smb_root_accessible`, must not be `None`")  # noqa: E501

        self._smb_root_accessible = smb_root_accessible

    @property
    def smb_root_visible(self):
        """Gets the smb_root_visible of this SnapshotSettingsSettings.  # noqa: E501

        True if root .snapshot directory is visible over SMB.  # noqa: E501

        :return: The smb_root_visible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._smb_root_visible

    @smb_root_visible.setter
    def smb_root_visible(self, smb_root_visible):
        """Sets the smb_root_visible of this SnapshotSettingsSettings.

        True if root .snapshot directory is visible over SMB.  # noqa: E501

        :param smb_root_visible: The smb_root_visible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if smb_root_visible is None:
            raise ValueError("Invalid value for `smb_root_visible`, must not be `None`")  # noqa: E501

        self._smb_root_visible = smb_root_visible

    @property
    def smb_subdir_accessible(self):
        """Gets the smb_subdir_accessible of this SnapshotSettingsSettings.  # noqa: E501

        True if sub-directory .snapshot directory is accessible over SMB.  # noqa: E501

        :return: The smb_subdir_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._smb_subdir_accessible

    @smb_subdir_accessible.setter
    def smb_subdir_accessible(self, smb_subdir_accessible):
        """Sets the smb_subdir_accessible of this SnapshotSettingsSettings.

        True if sub-directory .snapshot directory is accessible over SMB.  # noqa: E501

        :param smb_subdir_accessible: The smb_subdir_accessible of this SnapshotSettingsSettings.  # noqa: E501
        :type: bool
        """
        if smb_subdir_accessible is None:
            raise ValueError("Invalid value for `smb_subdir_accessible`, must not be `None`")  # noqa: E501

        self._smb_subdir_accessible = smb_subdir_accessible

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
        if not isinstance(other, SnapshotSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
