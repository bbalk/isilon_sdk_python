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


class CreateSnapshotChangelistResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateSnapshotChangelistResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'job_id': 'int',
            'num_entries': 'int',
            'root_path': 'str',
            'snap1': 'int',
            'snap2': 'int',
            'status': 'str'
        }

        self.attribute_map = {
            'job_id': 'job_id',
            'num_entries': 'num_entries',
            'root_path': 'root_path',
            'snap1': 'snap1',
            'snap2': 'snap2',
            'status': 'status'
        }

        self._job_id = None
        self._num_entries = None
        self._root_path = None
        self._snap1 = None
        self._snap2 = None
        self._status = None

    @property
    def job_id(self):
        """
        Gets the job_id of this CreateSnapshotChangelistResponse.
        The ID of the job which created the changelist.

        :return: The job_id of this CreateSnapshotChangelistResponse.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this CreateSnapshotChangelistResponse.
        The ID of the job which created the changelist.

        :param job_id: The job_id of this CreateSnapshotChangelistResponse.
        :type: int
        """
        self._job_id = job_id

    @property
    def num_entries(self):
        """
        Gets the num_entries of this CreateSnapshotChangelistResponse.
        Number of LIN entries in changelist.

        :return: The num_entries of this CreateSnapshotChangelistResponse.
        :rtype: int
        """
        return self._num_entries

    @num_entries.setter
    def num_entries(self, num_entries):
        """
        Sets the num_entries of this CreateSnapshotChangelistResponse.
        Number of LIN entries in changelist.

        :param num_entries: The num_entries of this CreateSnapshotChangelistResponse.
        :type: int
        """
        self._num_entries = num_entries

    @property
    def root_path(self):
        """
        Gets the root_path of this CreateSnapshotChangelistResponse.
        Root path of all LINs in changelist.

        :return: The root_path of this CreateSnapshotChangelistResponse.
        :rtype: str
        """
        return self._root_path

    @root_path.setter
    def root_path(self, root_path):
        """
        Sets the root_path of this CreateSnapshotChangelistResponse.
        Root path of all LINs in changelist.

        :param root_path: The root_path of this CreateSnapshotChangelistResponse.
        :type: str
        """
        self._root_path = root_path

    @property
    def snap1(self):
        """
        Gets the snap1 of this CreateSnapshotChangelistResponse.
        The lower snapid used to compute the changelist.

        :return: The snap1 of this CreateSnapshotChangelistResponse.
        :rtype: int
        """
        return self._snap1

    @snap1.setter
    def snap1(self, snap1):
        """
        Sets the snap1 of this CreateSnapshotChangelistResponse.
        The lower snapid used to compute the changelist.

        :param snap1: The snap1 of this CreateSnapshotChangelistResponse.
        :type: int
        """
        self._snap1 = snap1

    @property
    def snap2(self):
        """
        Gets the snap2 of this CreateSnapshotChangelistResponse.
        The higher snapid used to compute the changelist.

        :return: The snap2 of this CreateSnapshotChangelistResponse.
        :rtype: int
        """
        return self._snap2

    @snap2.setter
    def snap2(self, snap2):
        """
        Sets the snap2 of this CreateSnapshotChangelistResponse.
        The higher snapid used to compute the changelist.

        :param snap2: The snap2 of this CreateSnapshotChangelistResponse.
        :type: int
        """
        self._snap2 = snap2

    @property
    def status(self):
        """
        Gets the status of this CreateSnapshotChangelistResponse.
        Status of changelist.

        :return: The status of this CreateSnapshotChangelistResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CreateSnapshotChangelistResponse.
        Status of changelist.

        :param status: The status of this CreateSnapshotChangelistResponse.
        :type: str
        """
        self._status = status

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

