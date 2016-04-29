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


class SnapshotRepstatesExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SnapshotRepstatesExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'snap2': 'int',
            'repstates': 'list[SnapshotRepstates]',
            'resume': 'str',
            'total': 'int',
            'id': 'str',
            'snap1': 'int'
        }

        self.attribute_map = {
            'snap2': 'snap2',
            'repstates': 'repstates',
            'resume': 'resume',
            'total': 'total',
            'id': 'id',
            'snap1': 'snap1'
        }

        self._snap2 = None
        self._repstates = None
        self._resume = None
        self._total = None
        self._id = None
        self._snap1 = None

    @property
    def snap2(self):
        """
        Gets the snap2 of this SnapshotRepstatesExtended.
        The higher snapid used to compute the repstate.

        :return: The snap2 of this SnapshotRepstatesExtended.
        :rtype: int
        """
        return self._snap2

    @snap2.setter
    def snap2(self, snap2):
        """
        Sets the snap2 of this SnapshotRepstatesExtended.
        The higher snapid used to compute the repstate.

        :param snap2: The snap2 of this SnapshotRepstatesExtended.
        :type: int
        """
        self._snap2 = snap2

    @property
    def repstates(self):
        """
        Gets the repstates of this SnapshotRepstatesExtended.


        :return: The repstates of this SnapshotRepstatesExtended.
        :rtype: list[SnapshotRepstates]
        """
        return self._repstates

    @repstates.setter
    def repstates(self, repstates):
        """
        Sets the repstates of this SnapshotRepstatesExtended.


        :param repstates: The repstates of this SnapshotRepstatesExtended.
        :type: list[SnapshotRepstates]
        """
        self._repstates = repstates

    @property
    def resume(self):
        """
        Gets the resume of this SnapshotRepstatesExtended.
        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).

        :return: The resume of this SnapshotRepstatesExtended.
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """
        Sets the resume of this SnapshotRepstatesExtended.
        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).

        :param resume: The resume of this SnapshotRepstatesExtended.
        :type: str
        """
        self._resume = resume

    @property
    def total(self):
        """
        Gets the total of this SnapshotRepstatesExtended.
        Total number of items available.

        :return: The total of this SnapshotRepstatesExtended.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this SnapshotRepstatesExtended.
        Total number of items available.

        :param total: The total of this SnapshotRepstatesExtended.
        :type: int
        """
        self._total = total

    @property
    def id(self):
        """
        Gets the id of this SnapshotRepstatesExtended.
        The system ID given to the repstate.

        :return: The id of this SnapshotRepstatesExtended.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SnapshotRepstatesExtended.
        The system ID given to the repstate.

        :param id: The id of this SnapshotRepstatesExtended.
        :type: str
        """
        self._id = id

    @property
    def snap1(self):
        """
        Gets the snap1 of this SnapshotRepstatesExtended.
        The lower snapid used to compute the repstate.

        :return: The snap1 of this SnapshotRepstatesExtended.
        :rtype: int
        """
        return self._snap1

    @snap1.setter
    def snap1(self, snap1):
        """
        Sets the snap1 of this SnapshotRepstatesExtended.
        The lower snapid used to compute the repstate.

        :param snap1: The snap1 of this SnapshotRepstatesExtended.
        :type: int
        """
        self._snap1 = snap1

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

