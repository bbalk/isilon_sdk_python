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


class CloudSettingsSettingsSleepTimeoutCloudGarbageCollection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CloudSettingsSettingsSleepTimeoutCloudGarbageCollection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'recovery_with_tasks': 'int',
            'recovery_without_tasks': 'int',
            'with_tasks': 'int',
            'without_tasks': 'int'
        }

        self.attribute_map = {
            'recovery_with_tasks': 'recovery_with_tasks',
            'recovery_without_tasks': 'recovery_without_tasks',
            'with_tasks': 'with_tasks',
            'without_tasks': 'without_tasks'
        }

        self._recovery_with_tasks = None
        self._recovery_without_tasks = None
        self._with_tasks = None
        self._without_tasks = None

    @property
    def recovery_with_tasks(self):
        """
        Gets the recovery_with_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        Sleep timeout for a recovery thread with pending tasks

        :return: The recovery_with_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        :rtype: int
        """
        return self._recovery_with_tasks

    @recovery_with_tasks.setter
    def recovery_with_tasks(self, recovery_with_tasks):
        """
        Sets the recovery_with_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        Sleep timeout for a recovery thread with pending tasks

        :param recovery_with_tasks: The recovery_with_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        :type: int
        """
        self._recovery_with_tasks = recovery_with_tasks

    @property
    def recovery_without_tasks(self):
        """
        Gets the recovery_without_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        Sleep timeout for a recovery thread without pending tasks

        :return: The recovery_without_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        :rtype: int
        """
        return self._recovery_without_tasks

    @recovery_without_tasks.setter
    def recovery_without_tasks(self, recovery_without_tasks):
        """
        Sets the recovery_without_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        Sleep timeout for a recovery thread without pending tasks

        :param recovery_without_tasks: The recovery_without_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        :type: int
        """
        self._recovery_without_tasks = recovery_without_tasks

    @property
    def with_tasks(self):
        """
        Gets the with_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        Sleep timeout for a non-recovery thread with pending tasks

        :return: The with_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        :rtype: int
        """
        return self._with_tasks

    @with_tasks.setter
    def with_tasks(self, with_tasks):
        """
        Sets the with_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        Sleep timeout for a non-recovery thread with pending tasks

        :param with_tasks: The with_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        :type: int
        """
        self._with_tasks = with_tasks

    @property
    def without_tasks(self):
        """
        Gets the without_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        Sleep timeout for a non-recovery thread without pending tasks

        :return: The without_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        :rtype: int
        """
        return self._without_tasks

    @without_tasks.setter
    def without_tasks(self, without_tasks):
        """
        Sets the without_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        Sleep timeout for a non-recovery thread without pending tasks

        :param without_tasks: The without_tasks of this CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.
        :type: int
        """
        self._without_tasks = without_tasks

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

