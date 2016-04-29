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


class QuotaQuotaUsage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QuotaQuotaUsage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'inodes': 'int',
            'logical': 'int',
            'physical': 'int'
        }

        self.attribute_map = {
            'inodes': 'inodes',
            'logical': 'logical',
            'physical': 'physical'
        }

        self._inodes = None
        self._logical = None
        self._physical = None

    @property
    def inodes(self):
        """
        Gets the inodes of this QuotaQuotaUsage.
        Number of inodes (filesystem entities) used by governed data.

        :return: The inodes of this QuotaQuotaUsage.
        :rtype: int
        """
        return self._inodes

    @inodes.setter
    def inodes(self, inodes):
        """
        Sets the inodes of this QuotaQuotaUsage.
        Number of inodes (filesystem entities) used by governed data.

        :param inodes: The inodes of this QuotaQuotaUsage.
        :type: int
        """
        self._inodes = inodes

    @property
    def logical(self):
        """
        Gets the logical of this QuotaQuotaUsage.
        Apparent bytes used by governed data.

        :return: The logical of this QuotaQuotaUsage.
        :rtype: int
        """
        return self._logical

    @logical.setter
    def logical(self, logical):
        """
        Sets the logical of this QuotaQuotaUsage.
        Apparent bytes used by governed data.

        :param logical: The logical of this QuotaQuotaUsage.
        :type: int
        """
        self._logical = logical

    @property
    def physical(self):
        """
        Gets the physical of this QuotaQuotaUsage.
        Bytes used for governed data and filesystem overhead.

        :return: The physical of this QuotaQuotaUsage.
        :rtype: int
        """
        return self._physical

    @physical.setter
    def physical(self, physical):
        """
        Sets the physical of this QuotaQuotaUsage.
        Bytes used for governed data and filesystem overhead.

        :param physical: The physical of this QuotaQuotaUsage.
        :type: int
        """
        self._physical = physical

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

