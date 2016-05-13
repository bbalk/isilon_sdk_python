# coding: utf-8

"""
Copyright 2016 SmartBear Software

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
import re


class SnapshotSnapshot(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SnapshotSnapshot - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alias': 'str',
            'expires': 'int',
            'name': 'str'
        }

        self.attribute_map = {
            'alias': 'alias',
            'expires': 'expires',
            'name': 'name'
        }

        self._alias = None
        self._expires = None
        self._name = None

    @property
    def alias(self):
        """
        Gets the alias of this SnapshotSnapshot.
        Alias name to create for this snapshot. If null, remove any alias.

        :return: The alias of this SnapshotSnapshot.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this SnapshotSnapshot.
        Alias name to create for this snapshot. If null, remove any alias.

        :param alias: The alias of this SnapshotSnapshot.
        :type: str
        """
        
        self._alias = alias

    @property
    def expires(self):
        """
        Gets the expires of this SnapshotSnapshot.
        The Unix Epoch time the snapshot will expire and be eligible for automatic deletion.

        :return: The expires of this SnapshotSnapshot.
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this SnapshotSnapshot.
        The Unix Epoch time the snapshot will expire and be eligible for automatic deletion.

        :param expires: The expires of this SnapshotSnapshot.
        :type: int
        """
        
        self._expires = expires

    @property
    def name(self):
        """
        Gets the name of this SnapshotSnapshot.
        The user or system supplied snapshot name. This will be null for snapshots pending delete.

        :return: The name of this SnapshotSnapshot.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SnapshotSnapshot.
        The user or system supplied snapshot name. This will be null for snapshots pending delete.

        :param name: The name of this SnapshotSnapshot.
        :type: str
        """
        
        self._name = name

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

