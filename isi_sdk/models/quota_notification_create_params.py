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


class QuotaNotificationCreateParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QuotaNotificationCreateParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action_alert': 'bool',
            'action_email_address': 'str',
            'action_email_owner': 'bool',
            'email_template': 'str',
            'holdoff': 'int',
            'schedule': 'str',
            'condition': 'str',
            'threshold': 'str'
        }

        self.attribute_map = {
            'action_alert': 'action_alert',
            'action_email_address': 'action_email_address',
            'action_email_owner': 'action_email_owner',
            'email_template': 'email_template',
            'holdoff': 'holdoff',
            'schedule': 'schedule',
            'condition': 'condition',
            'threshold': 'threshold'
        }

        self._action_alert = None
        self._action_email_address = None
        self._action_email_owner = None
        self._email_template = None
        self._holdoff = None
        self._schedule = None
        self._condition = None
        self._threshold = None

    @property
    def action_alert(self):
        """
        Gets the action_alert of this QuotaNotificationCreateParams.
        Send alert when rule matches.

        :return: The action_alert of this QuotaNotificationCreateParams.
        :rtype: bool
        """
        return self._action_alert

    @action_alert.setter
    def action_alert(self, action_alert):
        """
        Sets the action_alert of this QuotaNotificationCreateParams.
        Send alert when rule matches.

        :param action_alert: The action_alert of this QuotaNotificationCreateParams.
        :type: bool
        """
        
        self._action_alert = action_alert

    @property
    def action_email_address(self):
        """
        Gets the action_email_address of this QuotaNotificationCreateParams.
        Email a specific email address when rule matches.

        :return: The action_email_address of this QuotaNotificationCreateParams.
        :rtype: str
        """
        return self._action_email_address

    @action_email_address.setter
    def action_email_address(self, action_email_address):
        """
        Sets the action_email_address of this QuotaNotificationCreateParams.
        Email a specific email address when rule matches.

        :param action_email_address: The action_email_address of this QuotaNotificationCreateParams.
        :type: str
        """
        
        self._action_email_address = action_email_address

    @property
    def action_email_owner(self):
        """
        Gets the action_email_owner of this QuotaNotificationCreateParams.
        Email quota domain owner when rule matches.

        :return: The action_email_owner of this QuotaNotificationCreateParams.
        :rtype: bool
        """
        return self._action_email_owner

    @action_email_owner.setter
    def action_email_owner(self, action_email_owner):
        """
        Sets the action_email_owner of this QuotaNotificationCreateParams.
        Email quota domain owner when rule matches.

        :param action_email_owner: The action_email_owner of this QuotaNotificationCreateParams.
        :type: bool
        """
        
        self._action_email_owner = action_email_owner

    @property
    def email_template(self):
        """
        Gets the email_template of this QuotaNotificationCreateParams.
        Path of optional /ifs template file used for email actions.

        :return: The email_template of this QuotaNotificationCreateParams.
        :rtype: str
        """
        return self._email_template

    @email_template.setter
    def email_template(self, email_template):
        """
        Sets the email_template of this QuotaNotificationCreateParams.
        Path of optional /ifs template file used for email actions.

        :param email_template: The email_template of this QuotaNotificationCreateParams.
        :type: str
        """
        
        self._email_template = email_template

    @property
    def holdoff(self):
        """
        Gets the holdoff of this QuotaNotificationCreateParams.
        Time to wait between detections for rules triggered by user actions.

        :return: The holdoff of this QuotaNotificationCreateParams.
        :rtype: int
        """
        return self._holdoff

    @holdoff.setter
    def holdoff(self, holdoff):
        """
        Sets the holdoff of this QuotaNotificationCreateParams.
        Time to wait between detections for rules triggered by user actions.

        :param holdoff: The holdoff of this QuotaNotificationCreateParams.
        :type: int
        """
        
        self._holdoff = holdoff

    @property
    def schedule(self):
        """
        Gets the schedule of this QuotaNotificationCreateParams.
        Schedule for rules that repeatedly notify.

        :return: The schedule of this QuotaNotificationCreateParams.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this QuotaNotificationCreateParams.
        Schedule for rules that repeatedly notify.

        :param schedule: The schedule of this QuotaNotificationCreateParams.
        :type: str
        """
        
        self._schedule = schedule

    @property
    def condition(self):
        """
        Gets the condition of this QuotaNotificationCreateParams.
        The condition detected.

        :return: The condition of this QuotaNotificationCreateParams.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this QuotaNotificationCreateParams.
        The condition detected.

        :param condition: The condition of this QuotaNotificationCreateParams.
        :type: str
        """
        allowed_values = ["exceeded", "denied", "violated", "expired"]
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition`, must be one of {0}"
                .format(allowed_values)
            )

        self._condition = condition

    @property
    def threshold(self):
        """
        Gets the threshold of this QuotaNotificationCreateParams.
        The quota threshold detected.

        :return: The threshold of this QuotaNotificationCreateParams.
        :rtype: str
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """
        Sets the threshold of this QuotaNotificationCreateParams.
        The quota threshold detected.

        :param threshold: The threshold of this QuotaNotificationCreateParams.
        :type: str
        """
        allowed_values = ["hard", "soft", "advisory"]
        if threshold not in allowed_values:
            raise ValueError(
                "Invalid value for `threshold`, must be one of {0}"
                .format(allowed_values)
            )

        self._threshold = threshold

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

