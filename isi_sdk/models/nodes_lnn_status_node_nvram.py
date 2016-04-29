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


class NodesLnnStatusNodeNvram(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NodesLnnStatusNodeNvram - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'batteries': 'list[NodesLnnStatusNodeNvramBattery]',
            'battery_count': 'int',
            'charge_status': 'str',
            'charge_status_number': 'int',
            'device': 'str',
            'present': 'bool',
            'present_flash': 'bool',
            'present_size': 'int',
            'present_type': 'str',
            'ship_mode': 'int',
            'supported': 'bool',
            'supported_flash': 'bool',
            'supported_size': 'int',
            'supported_type': 'str'
        }

        self.attribute_map = {
            'batteries': 'batteries',
            'battery_count': 'battery_count',
            'charge_status': 'charge_status',
            'charge_status_number': 'charge_status_number',
            'device': 'device',
            'present': 'present',
            'present_flash': 'present_flash',
            'present_size': 'present_size',
            'present_type': 'present_type',
            'ship_mode': 'ship_mode',
            'supported': 'supported',
            'supported_flash': 'supported_flash',
            'supported_size': 'supported_size',
            'supported_type': 'supported_type'
        }

        self._batteries = None
        self._battery_count = None
        self._charge_status = None
        self._charge_status_number = None
        self._device = None
        self._present = None
        self._present_flash = None
        self._present_size = None
        self._present_type = None
        self._ship_mode = None
        self._supported = None
        self._supported_flash = None
        self._supported_size = None
        self._supported_type = None

    @property
    def batteries(self):
        """
        Gets the batteries of this NodesLnnStatusNodeNvram.
        This node's NVRAM battery status information.

        :return: The batteries of this NodesLnnStatusNodeNvram.
        :rtype: list[NodesLnnStatusNodeNvramBattery]
        """
        return self._batteries

    @batteries.setter
    def batteries(self, batteries):
        """
        Sets the batteries of this NodesLnnStatusNodeNvram.
        This node's NVRAM battery status information.

        :param batteries: The batteries of this NodesLnnStatusNodeNvram.
        :type: list[NodesLnnStatusNodeNvramBattery]
        """
        self._batteries = batteries

    @property
    def battery_count(self):
        """
        Gets the battery_count of this NodesLnnStatusNodeNvram.
        This node's NVRAM battery count.

        :return: The battery_count of this NodesLnnStatusNodeNvram.
        :rtype: int
        """
        return self._battery_count

    @battery_count.setter
    def battery_count(self, battery_count):
        """
        Sets the battery_count of this NodesLnnStatusNodeNvram.
        This node's NVRAM battery count.

        :param battery_count: The battery_count of this NodesLnnStatusNodeNvram.
        :type: int
        """
        self._battery_count = battery_count

    @property
    def charge_status(self):
        """
        Gets the charge_status of this NodesLnnStatusNodeNvram.
        This node's NVRAM battery charge status, as a color.

        :return: The charge_status of this NodesLnnStatusNodeNvram.
        :rtype: str
        """
        return self._charge_status

    @charge_status.setter
    def charge_status(self, charge_status):
        """
        Sets the charge_status of this NodesLnnStatusNodeNvram.
        This node's NVRAM battery charge status, as a color.

        :param charge_status: The charge_status of this NodesLnnStatusNodeNvram.
        :type: str
        """
        self._charge_status = charge_status

    @property
    def charge_status_number(self):
        """
        Gets the charge_status_number of this NodesLnnStatusNodeNvram.
        This node's NVRAM battery charge status, as a number.

        :return: The charge_status_number of this NodesLnnStatusNodeNvram.
        :rtype: int
        """
        return self._charge_status_number

    @charge_status_number.setter
    def charge_status_number(self, charge_status_number):
        """
        Sets the charge_status_number of this NodesLnnStatusNodeNvram.
        This node's NVRAM battery charge status, as a number.

        :param charge_status_number: The charge_status_number of this NodesLnnStatusNodeNvram.
        :type: int
        """
        self._charge_status_number = charge_status_number

    @property
    def device(self):
        """
        Gets the device of this NodesLnnStatusNodeNvram.
        This node's NVRAM device name with path.

        :return: The device of this NodesLnnStatusNodeNvram.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this NodesLnnStatusNodeNvram.
        This node's NVRAM device name with path.

        :param device: The device of this NodesLnnStatusNodeNvram.
        :type: str
        """
        self._device = device

    @property
    def present(self):
        """
        Gets the present of this NodesLnnStatusNodeNvram.
        This node has NVRAM.

        :return: The present of this NodesLnnStatusNodeNvram.
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """
        Sets the present of this NodesLnnStatusNodeNvram.
        This node has NVRAM.

        :param present: The present of this NodesLnnStatusNodeNvram.
        :type: bool
        """
        self._present = present

    @property
    def present_flash(self):
        """
        Gets the present_flash of this NodesLnnStatusNodeNvram.
        This node has NVRAM with flash storage.

        :return: The present_flash of this NodesLnnStatusNodeNvram.
        :rtype: bool
        """
        return self._present_flash

    @present_flash.setter
    def present_flash(self, present_flash):
        """
        Sets the present_flash of this NodesLnnStatusNodeNvram.
        This node has NVRAM with flash storage.

        :param present_flash: The present_flash of this NodesLnnStatusNodeNvram.
        :type: bool
        """
        self._present_flash = present_flash

    @property
    def present_size(self):
        """
        Gets the present_size of this NodesLnnStatusNodeNvram.
        The size of the NVRAM, in bytes.

        :return: The present_size of this NodesLnnStatusNodeNvram.
        :rtype: int
        """
        return self._present_size

    @present_size.setter
    def present_size(self, present_size):
        """
        Sets the present_size of this NodesLnnStatusNodeNvram.
        The size of the NVRAM, in bytes.

        :param present_size: The present_size of this NodesLnnStatusNodeNvram.
        :type: int
        """
        self._present_size = present_size

    @property
    def present_type(self):
        """
        Gets the present_type of this NodesLnnStatusNodeNvram.
        This node's NVRAM type.

        :return: The present_type of this NodesLnnStatusNodeNvram.
        :rtype: str
        """
        return self._present_type

    @present_type.setter
    def present_type(self, present_type):
        """
        Sets the present_type of this NodesLnnStatusNodeNvram.
        This node's NVRAM type.

        :param present_type: The present_type of this NodesLnnStatusNodeNvram.
        :type: str
        """
        self._present_type = present_type

    @property
    def ship_mode(self):
        """
        Gets the ship_mode of this NodesLnnStatusNodeNvram.
        This node's current ship mode state for NVRAM batteries.

        :return: The ship_mode of this NodesLnnStatusNodeNvram.
        :rtype: int
        """
        return self._ship_mode

    @ship_mode.setter
    def ship_mode(self, ship_mode):
        """
        Sets the ship_mode of this NodesLnnStatusNodeNvram.
        This node's current ship mode state for NVRAM batteries.

        :param ship_mode: The ship_mode of this NodesLnnStatusNodeNvram.
        :type: int
        """
        self._ship_mode = ship_mode

    @property
    def supported(self):
        """
        Gets the supported of this NodesLnnStatusNodeNvram.
        This node supports NVRAM.

        :return: The supported of this NodesLnnStatusNodeNvram.
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """
        Sets the supported of this NodesLnnStatusNodeNvram.
        This node supports NVRAM.

        :param supported: The supported of this NodesLnnStatusNodeNvram.
        :type: bool
        """
        self._supported = supported

    @property
    def supported_flash(self):
        """
        Gets the supported_flash of this NodesLnnStatusNodeNvram.
        This node supports NVRAM with flash storage.

        :return: The supported_flash of this NodesLnnStatusNodeNvram.
        :rtype: bool
        """
        return self._supported_flash

    @supported_flash.setter
    def supported_flash(self, supported_flash):
        """
        Sets the supported_flash of this NodesLnnStatusNodeNvram.
        This node supports NVRAM with flash storage.

        :param supported_flash: The supported_flash of this NodesLnnStatusNodeNvram.
        :type: bool
        """
        self._supported_flash = supported_flash

    @property
    def supported_size(self):
        """
        Gets the supported_size of this NodesLnnStatusNodeNvram.
        The maximum size of the NVRAM, in bytes.

        :return: The supported_size of this NodesLnnStatusNodeNvram.
        :rtype: int
        """
        return self._supported_size

    @supported_size.setter
    def supported_size(self, supported_size):
        """
        Sets the supported_size of this NodesLnnStatusNodeNvram.
        The maximum size of the NVRAM, in bytes.

        :param supported_size: The supported_size of this NodesLnnStatusNodeNvram.
        :type: int
        """
        self._supported_size = supported_size

    @property
    def supported_type(self):
        """
        Gets the supported_type of this NodesLnnStatusNodeNvram.
        This node's supported NVRAM type.

        :return: The supported_type of this NodesLnnStatusNodeNvram.
        :rtype: str
        """
        return self._supported_type

    @supported_type.setter
    def supported_type(self, supported_type):
        """
        Sets the supported_type of this NodesLnnStatusNodeNvram.
        This node's supported NVRAM type.

        :param supported_type: The supported_type of this NodesLnnStatusNodeNvram.
        :type: str
        """
        self._supported_type = supported_type

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

