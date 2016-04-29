# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class SmbSettingsShareSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SmbSettingsShareSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_based_enumeration': 'bool',
            'access_based_enumeration_root_only': 'bool',
            'allow_delete_readonly': 'bool',
            'allow_execute_always': 'bool',
            'ca_timeout': 'int',
            'ca_write_integrity': 'str',
            'change_notify': 'str',
            'create_permissions': 'str',
            'csc_policy': 'str',
            'directory_create_mask': 'int',
            'directory_create_mode': 'int',
            'file_create_mask': 'int',
            'file_create_mode': 'int',
            'file_filter_extensions': 'list[str]',
            'file_filter_type': 'str',
            'file_filtering_enabled': 'bool',
            'hide_dot_files': 'bool',
            'host_acl': 'list[str]',
            'impersonate_guest': 'str',
            'impersonate_user': 'str',
            'mangle_byte_start': 'int',
            'mangle_map': 'list[str]',
            'ntfs_acl_support': 'bool',
            'oplocks': 'bool',
            'strict_ca_lockout': 'bool',
            'strict_flush': 'bool',
            'strict_locking': 'bool',
            'zone': 'str'
        }

        self.attribute_map = {
            'access_based_enumeration': 'access_based_enumeration',
            'access_based_enumeration_root_only': 'access_based_enumeration_root_only',
            'allow_delete_readonly': 'allow_delete_readonly',
            'allow_execute_always': 'allow_execute_always',
            'ca_timeout': 'ca_timeout',
            'ca_write_integrity': 'ca_write_integrity',
            'change_notify': 'change_notify',
            'create_permissions': 'create_permissions',
            'csc_policy': 'csc_policy',
            'directory_create_mask': 'directory_create_mask',
            'directory_create_mode': 'directory_create_mode',
            'file_create_mask': 'file_create_mask',
            'file_create_mode': 'file_create_mode',
            'file_filter_extensions': 'file_filter_extensions',
            'file_filter_type': 'file_filter_type',
            'file_filtering_enabled': 'file_filtering_enabled',
            'hide_dot_files': 'hide_dot_files',
            'host_acl': 'host_acl',
            'impersonate_guest': 'impersonate_guest',
            'impersonate_user': 'impersonate_user',
            'mangle_byte_start': 'mangle_byte_start',
            'mangle_map': 'mangle_map',
            'ntfs_acl_support': 'ntfs_acl_support',
            'oplocks': 'oplocks',
            'strict_ca_lockout': 'strict_ca_lockout',
            'strict_flush': 'strict_flush',
            'strict_locking': 'strict_locking',
            'zone': 'zone'
        }

        self._access_based_enumeration = None
        self._access_based_enumeration_root_only = None
        self._allow_delete_readonly = None
        self._allow_execute_always = None
        self._ca_timeout = None
        self._ca_write_integrity = None
        self._change_notify = None
        self._create_permissions = None
        self._csc_policy = None
        self._directory_create_mask = None
        self._directory_create_mode = None
        self._file_create_mask = None
        self._file_create_mode = None
        self._file_filter_extensions = None
        self._file_filter_type = None
        self._file_filtering_enabled = None
        self._hide_dot_files = None
        self._host_acl = None
        self._impersonate_guest = None
        self._impersonate_user = None
        self._mangle_byte_start = None
        self._mangle_map = None
        self._ntfs_acl_support = None
        self._oplocks = None
        self._strict_ca_lockout = None
        self._strict_flush = None
        self._strict_locking = None
        self._zone = None

    @property
    def access_based_enumeration(self):
        """
        Gets the access_based_enumeration of this SmbSettingsShareSettings.
        Only enumerate files and folders the requesting user has access to.

        :return: The access_based_enumeration of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._access_based_enumeration

    @access_based_enumeration.setter
    def access_based_enumeration(self, access_based_enumeration):
        """
        Sets the access_based_enumeration of this SmbSettingsShareSettings.
        Only enumerate files and folders the requesting user has access to.

        :param access_based_enumeration: The access_based_enumeration of this SmbSettingsShareSettings.
        :type: bool
        """
        self._access_based_enumeration = access_based_enumeration

    @property
    def access_based_enumeration_root_only(self):
        """
        Gets the access_based_enumeration_root_only of this SmbSettingsShareSettings.
        Access-based enumeration on only the root directory of the share.

        :return: The access_based_enumeration_root_only of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._access_based_enumeration_root_only

    @access_based_enumeration_root_only.setter
    def access_based_enumeration_root_only(self, access_based_enumeration_root_only):
        """
        Sets the access_based_enumeration_root_only of this SmbSettingsShareSettings.
        Access-based enumeration on only the root directory of the share.

        :param access_based_enumeration_root_only: The access_based_enumeration_root_only of this SmbSettingsShareSettings.
        :type: bool
        """
        self._access_based_enumeration_root_only = access_based_enumeration_root_only

    @property
    def allow_delete_readonly(self):
        """
        Gets the allow_delete_readonly of this SmbSettingsShareSettings.
        Allow deletion of read-only files in the share.

        :return: The allow_delete_readonly of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._allow_delete_readonly

    @allow_delete_readonly.setter
    def allow_delete_readonly(self, allow_delete_readonly):
        """
        Sets the allow_delete_readonly of this SmbSettingsShareSettings.
        Allow deletion of read-only files in the share.

        :param allow_delete_readonly: The allow_delete_readonly of this SmbSettingsShareSettings.
        :type: bool
        """
        self._allow_delete_readonly = allow_delete_readonly

    @property
    def allow_execute_always(self):
        """
        Gets the allow_execute_always of this SmbSettingsShareSettings.
        Allows users to execute files they have read rights for.

        :return: The allow_execute_always of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._allow_execute_always

    @allow_execute_always.setter
    def allow_execute_always(self, allow_execute_always):
        """
        Sets the allow_execute_always of this SmbSettingsShareSettings.
        Allows users to execute files they have read rights for.

        :param allow_execute_always: The allow_execute_always of this SmbSettingsShareSettings.
        :type: bool
        """
        self._allow_execute_always = allow_execute_always

    @property
    def ca_timeout(self):
        """
        Gets the ca_timeout of this SmbSettingsShareSettings.
        Persistent open timeout for the share.

        :return: The ca_timeout of this SmbSettingsShareSettings.
        :rtype: int
        """
        return self._ca_timeout

    @ca_timeout.setter
    def ca_timeout(self, ca_timeout):
        """
        Sets the ca_timeout of this SmbSettingsShareSettings.
        Persistent open timeout for the share.

        :param ca_timeout: The ca_timeout of this SmbSettingsShareSettings.
        :type: int
        """
        self._ca_timeout = ca_timeout

    @property
    def ca_write_integrity(self):
        """
        Gets the ca_write_integrity of this SmbSettingsShareSettings.
        Specify the level of write-integrity on continuously available shares.

        :return: The ca_write_integrity of this SmbSettingsShareSettings.
        :rtype: str
        """
        return self._ca_write_integrity

    @ca_write_integrity.setter
    def ca_write_integrity(self, ca_write_integrity):
        """
        Sets the ca_write_integrity of this SmbSettingsShareSettings.
        Specify the level of write-integrity on continuously available shares.

        :param ca_write_integrity: The ca_write_integrity of this SmbSettingsShareSettings.
        :type: str
        """
        allowed_values = ["none", "write-read-coherent", "full"]
        if ca_write_integrity not in allowed_values:
            raise ValueError(
                "Invalid value for `ca_write_integrity`, must be one of {0}"
                .format(allowed_values)
            )
        self._ca_write_integrity = ca_write_integrity

    @property
    def change_notify(self):
        """
        Gets the change_notify of this SmbSettingsShareSettings.
        Specify level of change notification alerts on the share.

        :return: The change_notify of this SmbSettingsShareSettings.
        :rtype: str
        """
        return self._change_notify

    @change_notify.setter
    def change_notify(self, change_notify):
        """
        Sets the change_notify of this SmbSettingsShareSettings.
        Specify level of change notification alerts on the share.

        :param change_notify: The change_notify of this SmbSettingsShareSettings.
        :type: str
        """
        allowed_values = ["all", "norecurse", "none"]
        if change_notify not in allowed_values:
            raise ValueError(
                "Invalid value for `change_notify`, must be one of {0}"
                .format(allowed_values)
            )
        self._change_notify = change_notify

    @property
    def create_permissions(self):
        """
        Gets the create_permissions of this SmbSettingsShareSettings.
        Set the create permissions for new files and directories in share.

        :return: The create_permissions of this SmbSettingsShareSettings.
        :rtype: str
        """
        return self._create_permissions

    @create_permissions.setter
    def create_permissions(self, create_permissions):
        """
        Sets the create_permissions of this SmbSettingsShareSettings.
        Set the create permissions for new files and directories in share.

        :param create_permissions: The create_permissions of this SmbSettingsShareSettings.
        :type: str
        """
        allowed_values = ["default acl", "inherit mode bits", "use create mask and mode"]
        if create_permissions not in allowed_values:
            raise ValueError(
                "Invalid value for `create_permissions`, must be one of {0}"
                .format(allowed_values)
            )
        self._create_permissions = create_permissions

    @property
    def csc_policy(self):
        """
        Gets the csc_policy of this SmbSettingsShareSettings.
        Client-side caching policy for the shares.

        :return: The csc_policy of this SmbSettingsShareSettings.
        :rtype: str
        """
        return self._csc_policy

    @csc_policy.setter
    def csc_policy(self, csc_policy):
        """
        Sets the csc_policy of this SmbSettingsShareSettings.
        Client-side caching policy for the shares.

        :param csc_policy: The csc_policy of this SmbSettingsShareSettings.
        :type: str
        """
        allowed_values = ["manual", "documents", "programs", "none"]
        if csc_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `csc_policy`, must be one of {0}"
                .format(allowed_values)
            )
        self._csc_policy = csc_policy

    @property
    def directory_create_mask(self):
        """
        Gets the directory_create_mask of this SmbSettingsShareSettings.
        Unix umask or mode bits.

        :return: The directory_create_mask of this SmbSettingsShareSettings.
        :rtype: int
        """
        return self._directory_create_mask

    @directory_create_mask.setter
    def directory_create_mask(self, directory_create_mask):
        """
        Sets the directory_create_mask of this SmbSettingsShareSettings.
        Unix umask or mode bits.

        :param directory_create_mask: The directory_create_mask of this SmbSettingsShareSettings.
        :type: int
        """
        self._directory_create_mask = directory_create_mask

    @property
    def directory_create_mode(self):
        """
        Gets the directory_create_mode of this SmbSettingsShareSettings.
        Unix umask or mode bits.

        :return: The directory_create_mode of this SmbSettingsShareSettings.
        :rtype: int
        """
        return self._directory_create_mode

    @directory_create_mode.setter
    def directory_create_mode(self, directory_create_mode):
        """
        Sets the directory_create_mode of this SmbSettingsShareSettings.
        Unix umask or mode bits.

        :param directory_create_mode: The directory_create_mode of this SmbSettingsShareSettings.
        :type: int
        """
        self._directory_create_mode = directory_create_mode

    @property
    def file_create_mask(self):
        """
        Gets the file_create_mask of this SmbSettingsShareSettings.
        Unix umask or mode bits.

        :return: The file_create_mask of this SmbSettingsShareSettings.
        :rtype: int
        """
        return self._file_create_mask

    @file_create_mask.setter
    def file_create_mask(self, file_create_mask):
        """
        Sets the file_create_mask of this SmbSettingsShareSettings.
        Unix umask or mode bits.

        :param file_create_mask: The file_create_mask of this SmbSettingsShareSettings.
        :type: int
        """
        self._file_create_mask = file_create_mask

    @property
    def file_create_mode(self):
        """
        Gets the file_create_mode of this SmbSettingsShareSettings.
        Unix umask or mode bits.

        :return: The file_create_mode of this SmbSettingsShareSettings.
        :rtype: int
        """
        return self._file_create_mode

    @file_create_mode.setter
    def file_create_mode(self, file_create_mode):
        """
        Sets the file_create_mode of this SmbSettingsShareSettings.
        Unix umask or mode bits.

        :param file_create_mode: The file_create_mode of this SmbSettingsShareSettings.
        :type: int
        """
        self._file_create_mode = file_create_mode

    @property
    def file_filter_extensions(self):
        """
        Gets the file_filter_extensions of this SmbSettingsShareSettings.
        Specifies the list of file extensions.

        :return: The file_filter_extensions of this SmbSettingsShareSettings.
        :rtype: list[str]
        """
        return self._file_filter_extensions

    @file_filter_extensions.setter
    def file_filter_extensions(self, file_filter_extensions):
        """
        Sets the file_filter_extensions of this SmbSettingsShareSettings.
        Specifies the list of file extensions.

        :param file_filter_extensions: The file_filter_extensions of this SmbSettingsShareSettings.
        :type: list[str]
        """
        self._file_filter_extensions = file_filter_extensions

    @property
    def file_filter_type(self):
        """
        Gets the file_filter_type of this SmbSettingsShareSettings.
        Specifies if filter list is for deny or allow. Default is deny.

        :return: The file_filter_type of this SmbSettingsShareSettings.
        :rtype: str
        """
        return self._file_filter_type

    @file_filter_type.setter
    def file_filter_type(self, file_filter_type):
        """
        Sets the file_filter_type of this SmbSettingsShareSettings.
        Specifies if filter list is for deny or allow. Default is deny.

        :param file_filter_type: The file_filter_type of this SmbSettingsShareSettings.
        :type: str
        """
        allowed_values = ["deny", "allow"]
        if file_filter_type not in allowed_values:
            raise ValueError(
                "Invalid value for `file_filter_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._file_filter_type = file_filter_type

    @property
    def file_filtering_enabled(self):
        """
        Gets the file_filtering_enabled of this SmbSettingsShareSettings.
        Enables file filtering on the share.

        :return: The file_filtering_enabled of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._file_filtering_enabled

    @file_filtering_enabled.setter
    def file_filtering_enabled(self, file_filtering_enabled):
        """
        Sets the file_filtering_enabled of this SmbSettingsShareSettings.
        Enables file filtering on the share.

        :param file_filtering_enabled: The file_filtering_enabled of this SmbSettingsShareSettings.
        :type: bool
        """
        self._file_filtering_enabled = file_filtering_enabled

    @property
    def hide_dot_files(self):
        """
        Gets the hide_dot_files of this SmbSettingsShareSettings.
        Hide files and directories that begin with a period '.'.

        :return: The hide_dot_files of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._hide_dot_files

    @hide_dot_files.setter
    def hide_dot_files(self, hide_dot_files):
        """
        Sets the hide_dot_files of this SmbSettingsShareSettings.
        Hide files and directories that begin with a period '.'.

        :param hide_dot_files: The hide_dot_files of this SmbSettingsShareSettings.
        :type: bool
        """
        self._hide_dot_files = hide_dot_files

    @property
    def host_acl(self):
        """
        Gets the host_acl of this SmbSettingsShareSettings.
        An ACL expressing which hosts are allowed access. A deny clause must be the final entry.

        :return: The host_acl of this SmbSettingsShareSettings.
        :rtype: list[str]
        """
        return self._host_acl

    @host_acl.setter
    def host_acl(self, host_acl):
        """
        Sets the host_acl of this SmbSettingsShareSettings.
        An ACL expressing which hosts are allowed access. A deny clause must be the final entry.

        :param host_acl: The host_acl of this SmbSettingsShareSettings.
        :type: list[str]
        """
        self._host_acl = host_acl

    @property
    def impersonate_guest(self):
        """
        Gets the impersonate_guest of this SmbSettingsShareSettings.
        Specify the condition in which user access is done as the guest account.

        :return: The impersonate_guest of this SmbSettingsShareSettings.
        :rtype: str
        """
        return self._impersonate_guest

    @impersonate_guest.setter
    def impersonate_guest(self, impersonate_guest):
        """
        Sets the impersonate_guest of this SmbSettingsShareSettings.
        Specify the condition in which user access is done as the guest account.

        :param impersonate_guest: The impersonate_guest of this SmbSettingsShareSettings.
        :type: str
        """
        allowed_values = ["always", "bad user", "never"]
        if impersonate_guest not in allowed_values:
            raise ValueError(
                "Invalid value for `impersonate_guest`, must be one of {0}"
                .format(allowed_values)
            )
        self._impersonate_guest = impersonate_guest

    @property
    def impersonate_user(self):
        """
        Gets the impersonate_user of this SmbSettingsShareSettings.
        User account to be used as guest account.

        :return: The impersonate_user of this SmbSettingsShareSettings.
        :rtype: str
        """
        return self._impersonate_user

    @impersonate_user.setter
    def impersonate_user(self, impersonate_user):
        """
        Sets the impersonate_user of this SmbSettingsShareSettings.
        User account to be used as guest account.

        :param impersonate_user: The impersonate_user of this SmbSettingsShareSettings.
        :type: str
        """
        self._impersonate_user = impersonate_user

    @property
    def mangle_byte_start(self):
        """
        Gets the mangle_byte_start of this SmbSettingsShareSettings.
        Specifies the wchar_t starting point for automatic byte mangling.

        :return: The mangle_byte_start of this SmbSettingsShareSettings.
        :rtype: int
        """
        return self._mangle_byte_start

    @mangle_byte_start.setter
    def mangle_byte_start(self, mangle_byte_start):
        """
        Sets the mangle_byte_start of this SmbSettingsShareSettings.
        Specifies the wchar_t starting point for automatic byte mangling.

        :param mangle_byte_start: The mangle_byte_start of this SmbSettingsShareSettings.
        :type: int
        """
        self._mangle_byte_start = mangle_byte_start

    @property
    def mangle_map(self):
        """
        Gets the mangle_map of this SmbSettingsShareSettings.
        Character mangle map.

        :return: The mangle_map of this SmbSettingsShareSettings.
        :rtype: list[str]
        """
        return self._mangle_map

    @mangle_map.setter
    def mangle_map(self, mangle_map):
        """
        Sets the mangle_map of this SmbSettingsShareSettings.
        Character mangle map.

        :param mangle_map: The mangle_map of this SmbSettingsShareSettings.
        :type: list[str]
        """
        self._mangle_map = mangle_map

    @property
    def ntfs_acl_support(self):
        """
        Gets the ntfs_acl_support of this SmbSettingsShareSettings.
        Support NTFS ACLs on files and directories.

        :return: The ntfs_acl_support of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._ntfs_acl_support

    @ntfs_acl_support.setter
    def ntfs_acl_support(self, ntfs_acl_support):
        """
        Sets the ntfs_acl_support of this SmbSettingsShareSettings.
        Support NTFS ACLs on files and directories.

        :param ntfs_acl_support: The ntfs_acl_support of this SmbSettingsShareSettings.
        :type: bool
        """
        self._ntfs_acl_support = ntfs_acl_support

    @property
    def oplocks(self):
        """
        Gets the oplocks of this SmbSettingsShareSettings.
        Allow oplock requests.

        :return: The oplocks of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._oplocks

    @oplocks.setter
    def oplocks(self, oplocks):
        """
        Sets the oplocks of this SmbSettingsShareSettings.
        Allow oplock requests.

        :param oplocks: The oplocks of this SmbSettingsShareSettings.
        :type: bool
        """
        self._oplocks = oplocks

    @property
    def strict_ca_lockout(self):
        """
        Gets the strict_ca_lockout of this SmbSettingsShareSettings.
        Specifies if persistent opens would do strict lockout on the share.

        :return: The strict_ca_lockout of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._strict_ca_lockout

    @strict_ca_lockout.setter
    def strict_ca_lockout(self, strict_ca_lockout):
        """
        Sets the strict_ca_lockout of this SmbSettingsShareSettings.
        Specifies if persistent opens would do strict lockout on the share.

        :param strict_ca_lockout: The strict_ca_lockout of this SmbSettingsShareSettings.
        :type: bool
        """
        self._strict_ca_lockout = strict_ca_lockout

    @property
    def strict_flush(self):
        """
        Gets the strict_flush of this SmbSettingsShareSettings.
        Handle SMB flush operations.

        :return: The strict_flush of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._strict_flush

    @strict_flush.setter
    def strict_flush(self, strict_flush):
        """
        Sets the strict_flush of this SmbSettingsShareSettings.
        Handle SMB flush operations.

        :param strict_flush: The strict_flush of this SmbSettingsShareSettings.
        :type: bool
        """
        self._strict_flush = strict_flush

    @property
    def strict_locking(self):
        """
        Gets the strict_locking of this SmbSettingsShareSettings.
        Specifies whether byte range locks contend against SMB I/O.

        :return: The strict_locking of this SmbSettingsShareSettings.
        :rtype: bool
        """
        return self._strict_locking

    @strict_locking.setter
    def strict_locking(self, strict_locking):
        """
        Sets the strict_locking of this SmbSettingsShareSettings.
        Specifies whether byte range locks contend against SMB I/O.

        :param strict_locking: The strict_locking of this SmbSettingsShareSettings.
        :type: bool
        """
        self._strict_locking = strict_locking

    @property
    def zone(self):
        """
        Gets the zone of this SmbSettingsShareSettings.
        Name of the access zone in which to update settings

        :return: The zone of this SmbSettingsShareSettings.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """
        Sets the zone of this SmbSettingsShareSettings.
        Name of the access zone in which to update settings

        :param zone: The zone of this SmbSettingsShareSettings.
        :type: str
        """
        self._zone = zone

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

