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


class QuotaQuota(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QuotaQuota - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'container': 'bool',
            'enforced': 'bool',
            'linked': 'bool',
            'thresholds': 'QuotaQuotaThresholds',
            'thresholds_include_overhead': 'bool'
        }

        self.attribute_map = {
            'container': 'container',
            'enforced': 'enforced',
            'linked': 'linked',
            'thresholds': 'thresholds',
            'thresholds_include_overhead': 'thresholds_include_overhead'
        }

        self._container = None
        self._enforced = None
        self._linked = None
        self._thresholds = None
        self._thresholds_include_overhead = None

    @property
    def container(self):
        """
        Gets the container of this QuotaQuota.
        If true, SMB shares using the quota directory see the quota thresholds as share size.

        :return: The container of this QuotaQuota.
        :rtype: bool
        """
        return self._container

    @container.setter
    def container(self, container):
        """
        Sets the container of this QuotaQuota.
        If true, SMB shares using the quota directory see the quota thresholds as share size.

        :param container: The container of this QuotaQuota.
        :type: bool
        """
        
        self._container = container

    @property
    def enforced(self):
        """
        Gets the enforced of this QuotaQuota.
        True if the quota provides enforcement, otherwise a accounting quota.

        :return: The enforced of this QuotaQuota.
        :rtype: bool
        """
        return self._enforced

    @enforced.setter
    def enforced(self, enforced):
        """
        Sets the enforced of this QuotaQuota.
        True if the quota provides enforcement, otherwise a accounting quota.

        :param enforced: The enforced of this QuotaQuota.
        :type: bool
        """
        
        self._enforced = enforced

    @property
    def linked(self):
        """
        Gets the linked of this QuotaQuota.
        If false and the quota is linked, attempt to unlink.

        :return: The linked of this QuotaQuota.
        :rtype: bool
        """
        return self._linked

    @linked.setter
    def linked(self, linked):
        """
        Sets the linked of this QuotaQuota.
        If false and the quota is linked, attempt to unlink.

        :param linked: The linked of this QuotaQuota.
        :type: bool
        """
        
        self._linked = linked

    @property
    def thresholds(self):
        """
        Gets the thresholds of this QuotaQuota.
        

        :return: The thresholds of this QuotaQuota.
        :rtype: QuotaQuotaThresholds
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """
        Sets the thresholds of this QuotaQuota.
        

        :param thresholds: The thresholds of this QuotaQuota.
        :type: QuotaQuotaThresholds
        """
        
        self._thresholds = thresholds

    @property
    def thresholds_include_overhead(self):
        """
        Gets the thresholds_include_overhead of this QuotaQuota.
        If true, thresholds apply to data plus filesystem overhead required to store the data (i.e. 'physical' usage).

        :return: The thresholds_include_overhead of this QuotaQuota.
        :rtype: bool
        """
        return self._thresholds_include_overhead

    @thresholds_include_overhead.setter
    def thresholds_include_overhead(self, thresholds_include_overhead):
        """
        Sets the thresholds_include_overhead of this QuotaQuota.
        If true, thresholds apply to data plus filesystem overhead required to store the data (i.e. 'physical' usage).

        :param thresholds_include_overhead: The thresholds_include_overhead of this QuotaQuota.
        :type: bool
        """
        
        self._thresholds_include_overhead = thresholds_include_overhead

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

