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


class ClusterFirmwareStatusNodePackageItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterFirmwareStatusNodePackageItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'checksum': 'str',
            'firmware': 'str',
            'version': 'str'
        }

        self.attribute_map = {
            'checksum': 'checksum',
            'firmware': 'firmware',
            'version': 'version'
        }

        self._checksum = None
        self._firmware = None
        self._version = None

    @property
    def checksum(self):
        """
        Gets the checksum of this ClusterFirmwareStatusNodePackageItem.
        Valid checksum string for binary. One of the following: 'ok', 'bad', 'file_missing', or 'na'

        :return: The checksum of this ClusterFirmwareStatusNodePackageItem.
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """
        Sets the checksum of this ClusterFirmwareStatusNodePackageItem.
        Valid checksum string for binary. One of the following: 'ok', 'bad', 'file_missing', or 'na'

        :param checksum: The checksum of this ClusterFirmwareStatusNodePackageItem.
        :type: str
        """
        self._checksum = checksum

    @property
    def firmware(self):
        """
        Gets the firmware of this ClusterFirmwareStatusNodePackageItem.
        The name of the firmware binary.

        :return: The firmware of this ClusterFirmwareStatusNodePackageItem.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this ClusterFirmwareStatusNodePackageItem.
        The name of the firmware binary.

        :param firmware: The firmware of this ClusterFirmwareStatusNodePackageItem.
        :type: str
        """
        self._firmware = firmware

    @property
    def version(self):
        """
        Gets the version of this ClusterFirmwareStatusNodePackageItem.
        The version string for the binary.

        :return: The version of this ClusterFirmwareStatusNodePackageItem.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ClusterFirmwareStatusNodePackageItem.
        The version string for the binary.

        :param version: The version of this ClusterFirmwareStatusNodePackageItem.
        :type: str
        """
        self._version = version

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

