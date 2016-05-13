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


class DedupeReportExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DedupeReportExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'dedupe_percent': 'str',
            'elapsed_time': 'int',
            'id': 'int',
            'job_id': 'int',
            'job_type': 'str',
            'reports': 'list[DedupeReport]'
        }

        self.attribute_map = {
            'dedupe_percent': 'dedupe_percent',
            'elapsed_time': 'elapsed_time',
            'id': 'id',
            'job_id': 'job_id',
            'job_type': 'job_type',
            'reports': 'reports'
        }

        self._dedupe_percent = None
        self._elapsed_time = None
        self._id = None
        self._job_id = None
        self._job_type = None
        self._reports = None

    @property
    def dedupe_percent(self):
        """
        Gets the dedupe_percent of this DedupeReportExtended.
        The amount of space the directory trees under this job's paths now take up, compared to what they would take up if not deduplicated (0 ~ 100).

        :return: The dedupe_percent of this DedupeReportExtended.
        :rtype: str
        """
        return self._dedupe_percent

    @dedupe_percent.setter
    def dedupe_percent(self, dedupe_percent):
        """
        Sets the dedupe_percent of this DedupeReportExtended.
        The amount of space the directory trees under this job's paths now take up, compared to what they would take up if not deduplicated (0 ~ 100).

        :param dedupe_percent: The dedupe_percent of this DedupeReportExtended.
        :type: str
        """
        
        self._dedupe_percent = dedupe_percent

    @property
    def elapsed_time(self):
        """
        Gets the elapsed_time of this DedupeReportExtended.
        The amount of time in seconds it took to run this job.

        :return: The elapsed_time of this DedupeReportExtended.
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """
        Sets the elapsed_time of this DedupeReportExtended.
        The amount of time in seconds it took to run this job.

        :param elapsed_time: The elapsed_time of this DedupeReportExtended.
        :type: int
        """
        
        self._elapsed_time = elapsed_time

    @property
    def id(self):
        """
        Gets the id of this DedupeReportExtended.
        An unique identifier for this report.

        :return: The id of this DedupeReportExtended.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DedupeReportExtended.
        An unique identifier for this report.

        :param id: The id of this DedupeReportExtended.
        :type: int
        """
        
        self._id = id

    @property
    def job_id(self):
        """
        Gets the job_id of this DedupeReportExtended.
        The job id this report refers to.

        :return: The job_id of this DedupeReportExtended.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this DedupeReportExtended.
        The job id this report refers to.

        :param job_id: The job_id of this DedupeReportExtended.
        :type: int
        """
        
        self._job_id = job_id

    @property
    def job_type(self):
        """
        Gets the job_type of this DedupeReportExtended.
        The type of dedupe job this report refers to.

        :return: The job_type of this DedupeReportExtended.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this DedupeReportExtended.
        The type of dedupe job this report refers to.

        :param job_type: The job_type of this DedupeReportExtended.
        :type: str
        """
        
        self._job_type = job_type

    @property
    def reports(self):
        """
        Gets the reports of this DedupeReportExtended.
        A list of report entries for this dedupe job.

        :return: The reports of this DedupeReportExtended.
        :rtype: list[DedupeReport]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """
        Sets the reports of this DedupeReportExtended.
        A list of report entries for this dedupe job.

        :param reports: The reports of this DedupeReportExtended.
        :type: list[DedupeReport]
        """
        
        self._reports = reports

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

