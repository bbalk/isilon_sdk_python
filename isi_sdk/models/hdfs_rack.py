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


class HdfsRack(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HdfsRack - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client_ip_ranges': 'list[str]',
            'ip_pools': 'list[str]',
            'name': 'str'
        }

        self.attribute_map = {
            'client_ip_ranges': 'client_ip_ranges',
            'ip_pools': 'ip_pools',
            'name': 'name'
        }

        self._client_ip_ranges = None
        self._ip_pools = None
        self._name = None

    @property
    def client_ip_ranges(self):
        """
        Gets the client_ip_ranges of this HdfsRack.
        Array of IP ranges. Clients from one of these IP ranges are served by corresponding nodes from ip_pools array.

        :return: The client_ip_ranges of this HdfsRack.
        :rtype: list[str]
        """
        return self._client_ip_ranges

    @client_ip_ranges.setter
    def client_ip_ranges(self, client_ip_ranges):
        """
        Sets the client_ip_ranges of this HdfsRack.
        Array of IP ranges. Clients from one of these IP ranges are served by corresponding nodes from ip_pools array.

        :param client_ip_ranges: The client_ip_ranges of this HdfsRack.
        :type: list[str]
        """
        
        self._client_ip_ranges = client_ip_ranges

    @property
    def ip_pools(self):
        """
        Gets the ip_pools of this HdfsRack.
        Array of IP pool names to use for serving clients from client_ip_ranges.

        :return: The ip_pools of this HdfsRack.
        :rtype: list[str]
        """
        return self._ip_pools

    @ip_pools.setter
    def ip_pools(self, ip_pools):
        """
        Sets the ip_pools of this HdfsRack.
        Array of IP pool names to use for serving clients from client_ip_ranges.

        :param ip_pools: The ip_pools of this HdfsRack.
        :type: list[str]
        """
        
        self._ip_pools = ip_pools

    @property
    def name(self):
        """
        Gets the name of this HdfsRack.
        Name of the rack

        :return: The name of this HdfsRack.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HdfsRack.
        Name of the rack

        :param name: The name of this HdfsRack.
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

