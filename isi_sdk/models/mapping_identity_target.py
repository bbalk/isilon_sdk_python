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


class MappingIdentityTarget(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MappingIdentityTarget - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'on_disk': 'bool',
            'target': 'GroupsGroupMember',
            'type': 'str'
        }

        self.attribute_map = {
            'on_disk': 'on_disk',
            'target': 'target',
            'type': 'type'
        }

        self._on_disk = None
        self._target = None
        self._type = None

    @property
    def on_disk(self):
        """
        Gets the on_disk of this MappingIdentityTarget.
        If true, the identity is preferred on-disk.

        :return: The on_disk of this MappingIdentityTarget.
        :rtype: bool
        """
        return self._on_disk

    @on_disk.setter
    def on_disk(self, on_disk):
        """
        Sets the on_disk of this MappingIdentityTarget.
        If true, the identity is preferred on-disk.

        :param on_disk: The on_disk of this MappingIdentityTarget.
        :type: bool
        """
        self._on_disk = on_disk

    @property
    def target(self):
        """
        Gets the target of this MappingIdentityTarget.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :return: The target of this MappingIdentityTarget.
        :rtype: GroupsGroupMember
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this MappingIdentityTarget.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :param target: The target of this MappingIdentityTarget.
        :type: GroupsGroupMember
        """
        self._target = target

    @property
    def type(self):
        """
        Gets the type of this MappingIdentityTarget.
        Specifies the origin of the identity mapping.

        :return: The type of this MappingIdentityTarget.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MappingIdentityTarget.
        Specifies the origin of the identity mapping.

        :param type: The type of this MappingIdentityTarget.
        :type: str
        """
        allowed_values = ["auto", "external", "manual"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )
        self._type = type

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

