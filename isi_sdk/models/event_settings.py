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


class EventSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EventSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'heartbeat_interval': 'str',
            'maintenance': 'EventSettingsMaintenance',
            'retention_days': 'int',
            'storage_limit': 'int'
        }

        self.attribute_map = {
            'heartbeat_interval': 'heartbeat_interval',
            'maintenance': 'maintenance',
            'retention_days': 'retention_days',
            'storage_limit': 'storage_limit'
        }

        self._heartbeat_interval = None
        self._maintenance = None
        self._retention_days = None
        self._storage_limit = None

    @property
    def heartbeat_interval(self):
        """
        Gets the heartbeat_interval of this EventSettings.
        Interval between heartbeat events. \"daily\", \"weekly\", or \"monthly\".

        :return: The heartbeat_interval of this EventSettings.
        :rtype: str
        """
        return self._heartbeat_interval

    @heartbeat_interval.setter
    def heartbeat_interval(self, heartbeat_interval):
        """
        Sets the heartbeat_interval of this EventSettings.
        Interval between heartbeat events. \"daily\", \"weekly\", or \"monthly\".

        :param heartbeat_interval: The heartbeat_interval of this EventSettings.
        :type: str
        """
        self._heartbeat_interval = heartbeat_interval

    @property
    def maintenance(self):
        """
        Gets the maintenance of this EventSettings.
        Specifies start and duration of maintenance period during which no alerts will be sent for new eventgroups.

        :return: The maintenance of this EventSettings.
        :rtype: EventSettingsMaintenance
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """
        Sets the maintenance of this EventSettings.
        Specifies start and duration of maintenance period during which no alerts will be sent for new eventgroups.

        :param maintenance: The maintenance of this EventSettings.
        :type: EventSettingsMaintenance
        """
        self._maintenance = maintenance

    @property
    def retention_days(self):
        """
        Gets the retention_days of this EventSettings.
        Retention period in days

        :return: The retention_days of this EventSettings.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        """
        Sets the retention_days of this EventSettings.
        Retention period in days

        :param retention_days: The retention_days of this EventSettings.
        :type: int
        """
        self._retention_days = retention_days

    @property
    def storage_limit(self):
        """
        Gets the storage_limit of this EventSettings.
        Storage limit in megabytes per terabyte of available storage

        :return: The storage_limit of this EventSettings.
        :rtype: int
        """
        return self._storage_limit

    @storage_limit.setter
    def storage_limit(self, storage_limit):
        """
        Sets the storage_limit of this EventSettings.
        Storage limit in megabytes per terabyte of available storage

        :param storage_limit: The storage_limit of this EventSettings.
        :type: int
        """
        self._storage_limit = storage_limit

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

