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


class LicenseLicense(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LicenseLicense - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'duration': 'int',
            'expiration': 'int',
            'id': 'str',
            'name': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'duration': 'duration',
            'expiration': 'expiration',
            'id': 'id',
            'name': 'name',
            'status': 'status'
        }

        self._duration = None
        self._expiration = None
        self._id = None
        self._name = None
        self._status = None

    @property
    def duration(self):
        """
        Gets the duration of this LicenseLicense.
        Total duration in seconds for temporary licenses.

        :return: The duration of this LicenseLicense.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this LicenseLicense.
        Total duration in seconds for temporary licenses.

        :param duration: The duration of this LicenseLicense.
        :type: int
        """
        self._duration = duration

    @property
    def expiration(self):
        """
        Gets the expiration of this LicenseLicense.
        Unix epoch time the license will expire.

        :return: The expiration of this LicenseLicense.
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """
        Sets the expiration of this LicenseLicense.
        Unix epoch time the license will expire.

        :param expiration: The expiration of this LicenseLicense.
        :type: int
        """
        self._expiration = expiration

    @property
    def id(self):
        """
        Gets the id of this LicenseLicense.
        Unique identifier for the license.

        :return: The id of this LicenseLicense.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LicenseLicense.
        Unique identifier for the license.

        :param id: The id of this LicenseLicense.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this LicenseLicense.
        Name of the licensed feature.

        :return: The name of this LicenseLicense.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LicenseLicense.
        Name of the licensed feature.

        :param name: The name of this LicenseLicense.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """
        Gets the status of this LicenseLicense.
        Current status of the license.

        :return: The status of this LicenseLicense.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LicenseLicense.
        Current status of the license.

        :param status: The status of this LicenseLicense.
        :type: str
        """
        allowed_values = ["Activated", "Evaluation", "Expired", "Inactive", "Unknown"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
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

