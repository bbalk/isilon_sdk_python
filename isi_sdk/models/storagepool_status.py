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


class StoragepoolStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StoragepoolStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'unhealthy': 'list[StoragepoolStatusUnhealthyItem]',
            'unprovisioned': 'list[StoragepoolStatusUnprovisionedItem]'
        }

        self.attribute_map = {
            'unhealthy': 'unhealthy',
            'unprovisioned': 'unprovisioned'
        }

        self._unhealthy = None
        self._unprovisioned = None

    @property
    def unhealthy(self):
        """
        Gets the unhealthy of this StoragepoolStatus.
        Disk pools which are currently unhealthy.

        :return: The unhealthy of this StoragepoolStatus.
        :rtype: list[StoragepoolStatusUnhealthyItem]
        """
        return self._unhealthy

    @unhealthy.setter
    def unhealthy(self, unhealthy):
        """
        Sets the unhealthy of this StoragepoolStatus.
        Disk pools which are currently unhealthy.

        :param unhealthy: The unhealthy of this StoragepoolStatus.
        :type: list[StoragepoolStatusUnhealthyItem]
        """
        self._unhealthy = unhealthy

    @property
    def unprovisioned(self):
        """
        Gets the unprovisioned of this StoragepoolStatus.
        Drives which are not currently provisioned into a disk pool.

        :return: The unprovisioned of this StoragepoolStatus.
        :rtype: list[StoragepoolStatusUnprovisionedItem]
        """
        return self._unprovisioned

    @unprovisioned.setter
    def unprovisioned(self, unprovisioned):
        """
        Sets the unprovisioned of this StoragepoolStatus.
        Drives which are not currently provisioned into a disk pool.

        :param unprovisioned: The unprovisioned of this StoragepoolStatus.
        :type: list[StoragepoolStatusUnprovisionedItem]
        """
        self._unprovisioned = unprovisioned

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

