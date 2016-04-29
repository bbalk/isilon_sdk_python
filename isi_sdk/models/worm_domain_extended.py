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


class WormDomainExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WormDomainExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'override_date': 'int',
            'max_retention': 'int',
            'type': 'str',
            'lin': 'int',
            'path': 'str',
            'incomplete': 'bool',
            'default_retention': 'int',
            'total_modifies': 'int',
            'privileged_delete': 'str',
            'autocommit_offset': 'int',
            'id': 'int',
            'min_retention': 'int',
            'max_modifies': 'int'
        }

        self.attribute_map = {
            'override_date': 'override_date',
            'max_retention': 'max_retention',
            'type': 'type',
            'lin': 'lin',
            'path': 'path',
            'incomplete': 'incomplete',
            'default_retention': 'default_retention',
            'total_modifies': 'total_modifies',
            'privileged_delete': 'privileged_delete',
            'autocommit_offset': 'autocommit_offset',
            'id': 'id',
            'min_retention': 'min_retention',
            'max_modifies': 'max_modifies'
        }

        self._override_date = None
        self._max_retention = None
        self._type = None
        self._lin = None
        self._path = None
        self._incomplete = None
        self._default_retention = None
        self._total_modifies = None
        self._privileged_delete = None
        self._autocommit_offset = None
        self._id = None
        self._min_retention = None
        self._max_modifies = None

    @property
    def override_date(self):
        """
        Gets the override_date of this WormDomainExtended.
        Specifies the override retention date for the domain. If this date is later than the retention date for any committed file, the file will remain protected until the override retention date.

        :return: The override_date of this WormDomainExtended.
        :rtype: int
        """
        return self._override_date

    @override_date.setter
    def override_date(self, override_date):
        """
        Sets the override_date of this WormDomainExtended.
        Specifies the override retention date for the domain. If this date is later than the retention date for any committed file, the file will remain protected until the override retention date.

        :param override_date: The override_date of this WormDomainExtended.
        :type: int
        """
        self._override_date = override_date

    @property
    def max_retention(self):
        """
        Gets the max_retention of this WormDomainExtended.
        Specifies the maximum amount of time, in seconds, that a file in this domain will be protected. This setting will override the retention period of any file committed with a longer retention period. If this parameter is set to null, an infinite length retention period is set.

        :return: The max_retention of this WormDomainExtended.
        :rtype: int
        """
        return self._max_retention

    @max_retention.setter
    def max_retention(self, max_retention):
        """
        Sets the max_retention of this WormDomainExtended.
        Specifies the maximum amount of time, in seconds, that a file in this domain will be protected. This setting will override the retention period of any file committed with a longer retention period. If this parameter is set to null, an infinite length retention period is set.

        :param max_retention: The max_retention of this WormDomainExtended.
        :type: int
        """
        self._max_retention = max_retention

    @property
    def type(self):
        """
        Gets the type of this WormDomainExtended.
        Specifies whether the domain is an enterprise domain or a compliance domain. Compliance domains can not be created on enterprise clusters. Enterprise and compliance domains can be created on compliance clusters.

        :return: The type of this WormDomainExtended.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WormDomainExtended.
        Specifies whether the domain is an enterprise domain or a compliance domain. Compliance domains can not be created on enterprise clusters. Enterprise and compliance domains can be created on compliance clusters.

        :param type: The type of this WormDomainExtended.
        :type: str
        """
        allowed_values = ["enterprise", "compliance"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def lin(self):
        """
        Gets the lin of this WormDomainExtended.
        Specifies the logical inode number (LIN) for the root of this domain.

        :return: The lin of this WormDomainExtended.
        :rtype: int
        """
        return self._lin

    @lin.setter
    def lin(self, lin):
        """
        Sets the lin of this WormDomainExtended.
        Specifies the logical inode number (LIN) for the root of this domain.

        :param lin: The lin of this WormDomainExtended.
        :type: int
        """
        self._lin = lin

    @property
    def path(self):
        """
        Gets the path of this WormDomainExtended.
        Specifies the root path of this domain. Files in this directory and all sub-directories will be protected.

        :return: The path of this WormDomainExtended.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this WormDomainExtended.
        Specifies the root path of this domain. Files in this directory and all sub-directories will be protected.

        :param path: The path of this WormDomainExtended.
        :type: str
        """
        self._path = path

    @property
    def incomplete(self):
        """
        Gets the incomplete of this WormDomainExtended.
        True if OneFS is still in the process of creating this domain and is unable to prevent files from being modified or deleted. If false, indicates that the domain is fully created and is able to prevent files from being modified or deleted.

        :return: The incomplete of this WormDomainExtended.
        :rtype: bool
        """
        return self._incomplete

    @incomplete.setter
    def incomplete(self, incomplete):
        """
        Sets the incomplete of this WormDomainExtended.
        True if OneFS is still in the process of creating this domain and is unable to prevent files from being modified or deleted. If false, indicates that the domain is fully created and is able to prevent files from being modified or deleted.

        :param incomplete: The incomplete of this WormDomainExtended.
        :type: bool
        """
        self._incomplete = incomplete

    @property
    def default_retention(self):
        """
        Gets the default_retention of this WormDomainExtended.
        Specifies the default amount of time, in seconds, that a file in this domain will be protected for. The default retention period is applied if no retention date is manually set on the file. This parameter can also be set to 'forever', 'use_min' (which applies the 'min_retention' option), or 'use_max' (which applies the 'max_retention' option).

        :return: The default_retention of this WormDomainExtended.
        :rtype: int
        """
        return self._default_retention

    @default_retention.setter
    def default_retention(self, default_retention):
        """
        Sets the default_retention of this WormDomainExtended.
        Specifies the default amount of time, in seconds, that a file in this domain will be protected for. The default retention period is applied if no retention date is manually set on the file. This parameter can also be set to 'forever', 'use_min' (which applies the 'min_retention' option), or 'use_max' (which applies the 'max_retention' option).

        :param default_retention: The default_retention of this WormDomainExtended.
        :type: int
        """
        self._default_retention = default_retention

    @property
    def total_modifies(self):
        """
        Gets the total_modifies of this WormDomainExtended.
        Specifies the number of times this domain has been modified and the number of times the attributes for the domain have changed. A SmartLock domain can be modified a fixed number of times as defined by the 'max_modifies' parameter.

        :return: The total_modifies of this WormDomainExtended.
        :rtype: int
        """
        return self._total_modifies

    @total_modifies.setter
    def total_modifies(self, total_modifies):
        """
        Sets the total_modifies of this WormDomainExtended.
        Specifies the number of times this domain has been modified and the number of times the attributes for the domain have changed. A SmartLock domain can be modified a fixed number of times as defined by the 'max_modifies' parameter.

        :param total_modifies: The total_modifies of this WormDomainExtended.
        :type: int
        """
        self._total_modifies = total_modifies

    @property
    def privileged_delete(self):
        """
        Gets the privileged_delete of this WormDomainExtended.
        When this value is set to 'on', files in this domain can be deleted through the privileged delete feature. If this value is set to 'disabled', privileged file deletes are permanently disabled and cannot be turned on again.

        :return: The privileged_delete of this WormDomainExtended.
        :rtype: str
        """
        return self._privileged_delete

    @privileged_delete.setter
    def privileged_delete(self, privileged_delete):
        """
        Sets the privileged_delete of this WormDomainExtended.
        When this value is set to 'on', files in this domain can be deleted through the privileged delete feature. If this value is set to 'disabled', privileged file deletes are permanently disabled and cannot be turned on again.

        :param privileged_delete: The privileged_delete of this WormDomainExtended.
        :type: str
        """
        allowed_values = ["on", "off", "disabled"]
        if privileged_delete not in allowed_values:
            raise ValueError(
                "Invalid value for `privileged_delete`, must be one of {0}"
                .format(allowed_values)
            )
        self._privileged_delete = privileged_delete

    @property
    def autocommit_offset(self):
        """
        Gets the autocommit_offset of this WormDomainExtended.
        Specifies the autocommit time period for the domain in seconds.  After a file is in the domain without being modified for the specified time period, the file is automatically committed. If this parameter is set to null, there is no autocommit time, and files must be committed manually.

        :return: The autocommit_offset of this WormDomainExtended.
        :rtype: int
        """
        return self._autocommit_offset

    @autocommit_offset.setter
    def autocommit_offset(self, autocommit_offset):
        """
        Sets the autocommit_offset of this WormDomainExtended.
        Specifies the autocommit time period for the domain in seconds.  After a file is in the domain without being modified for the specified time period, the file is automatically committed. If this parameter is set to null, there is no autocommit time, and files must be committed manually.

        :param autocommit_offset: The autocommit_offset of this WormDomainExtended.
        :type: int
        """
        self._autocommit_offset = autocommit_offset

    @property
    def id(self):
        """
        Gets the id of this WormDomainExtended.
        Specifies the system-assigned ID for the protection domain.

        :return: The id of this WormDomainExtended.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WormDomainExtended.
        Specifies the system-assigned ID for the protection domain.

        :param id: The id of this WormDomainExtended.
        :type: int
        """
        self._id = id

    @property
    def min_retention(self):
        """
        Gets the min_retention of this WormDomainExtended.
        Specifies the minimum amount of time, in seconds, that a file in this domain will be protected. This setting will override the retention period of any file committed with a shorter retention period. If this parameter is set to null, this minimum value is not enforced. This parameter can also be set to 'forever'.

        :return: The min_retention of this WormDomainExtended.
        :rtype: int
        """
        return self._min_retention

    @min_retention.setter
    def min_retention(self, min_retention):
        """
        Sets the min_retention of this WormDomainExtended.
        Specifies the minimum amount of time, in seconds, that a file in this domain will be protected. This setting will override the retention period of any file committed with a shorter retention period. If this parameter is set to null, this minimum value is not enforced. This parameter can also be set to 'forever'.

        :param min_retention: The min_retention of this WormDomainExtended.
        :type: int
        """
        self._min_retention = min_retention

    @property
    def max_modifies(self):
        """
        Gets the max_modifies of this WormDomainExtended.
        Specifies the maximum amount of time, in seconds, that a file in this domain will be protected. This setting will override the retention period of any file committed with a longer retention period. If this parameter is set to null, an infinite length retention period is set.

        :return: The max_modifies of this WormDomainExtended.
        :rtype: int
        """
        return self._max_modifies

    @max_modifies.setter
    def max_modifies(self, max_modifies):
        """
        Sets the max_modifies of this WormDomainExtended.
        Specifies the maximum amount of time, in seconds, that a file in this domain will be protected. This setting will override the retention period of any file committed with a longer retention period. If this parameter is set to null, an infinite length retention period is set.

        :param max_modifies: The max_modifies of this WormDomainExtended.
        :type: int
        """
        self._max_modifies = max_modifies

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

