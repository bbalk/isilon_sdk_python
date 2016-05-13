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


class JobJobAvscanParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JobJobAvscanParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'force_run': 'bool',
            'policy': 'str',
            'report_id': 'str',
            'update': 'bool'
        }

        self.attribute_map = {
            'force_run': 'force_run',
            'policy': 'policy',
            'report_id': 'report_id',
            'update': 'update'
        }

        self._force_run = None
        self._policy = None
        self._report_id = None
        self._update = None

    @property
    def force_run(self):
        """
        Gets the force_run of this JobJobAvscanParams.
        Force files to be scanned, even if excluded by the policy.

        :return: The force_run of this JobJobAvscanParams.
        :rtype: bool
        """
        return self._force_run

    @force_run.setter
    def force_run(self, force_run):
        """
        Sets the force_run of this JobJobAvscanParams.
        Force files to be scanned, even if excluded by the policy.

        :param force_run: The force_run of this JobJobAvscanParams.
        :type: bool
        """
        
        self._force_run = force_run

    @property
    def policy(self):
        """
        Gets the policy of this JobJobAvscanParams.
        The antivirus scan policy to run.

        :return: The policy of this JobJobAvscanParams.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this JobJobAvscanParams.
        The antivirus scan policy to run.

        :param policy: The policy of this JobJobAvscanParams.
        :type: str
        """
        
        if not policy:
            raise ValueError("Invalid value for `policy`, must not be `None`")
        if len(policy) < 1: 
            raise ValueError("Invalid value for `policy`, length must be greater than or equal to `1`")

        self._policy = policy

    @property
    def report_id(self):
        """
        Gets the report_id of this JobJobAvscanParams.
        An optional report id for the scan.

        :return: The report_id of this JobJobAvscanParams.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """
        Sets the report_id of this JobJobAvscanParams.
        An optional report id for the scan.

        :param report_id: The report_id of this JobJobAvscanParams.
        :type: str
        """
        
        if not report_id:
            raise ValueError("Invalid value for `report_id`, must not be `None`")
        if len(report_id) > 15: 
            raise ValueError("Invalid value for `report_id`, length must be less than `15`")
        if len(report_id) < 1: 
            raise ValueError("Invalid value for `report_id`, length must be greater than or equal to `1`")

        self._report_id = report_id

    @property
    def update(self):
        """
        Gets the update of this JobJobAvscanParams.
        Update the last run time for the policy.

        :return: The update of this JobJobAvscanParams.
        :rtype: bool
        """
        return self._update

    @update.setter
    def update(self, update):
        """
        Sets the update of this JobJobAvscanParams.
        Update the last run time for the policy.

        :param update: The update of this JobJobAvscanParams.
        :type: bool
        """
        
        self._update = update

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

