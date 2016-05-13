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


class NdmpContextsBreContext(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NdmpContextsBreContext - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bre_context_id': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'bre_context_id': 'bre_context_id',
            'id': 'id'
        }

        self._bre_context_id = None
        self._id = None

    @property
    def bre_context_id(self):
        """
        Gets the bre_context_id of this NdmpContextsBreContext.
        Unique ID of NDMP BRE context

        :return: The bre_context_id of this NdmpContextsBreContext.
        :rtype: str
        """
        return self._bre_context_id

    @bre_context_id.setter
    def bre_context_id(self, bre_context_id):
        """
        Sets the bre_context_id of this NdmpContextsBreContext.
        Unique ID of NDMP BRE context

        :param bre_context_id: The bre_context_id of this NdmpContextsBreContext.
        :type: str
        """
        
        self._bre_context_id = bre_context_id

    @property
    def id(self):
        """
        Gets the id of this NdmpContextsBreContext.
        Unique display id.

        :return: The id of this NdmpContextsBreContext.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NdmpContextsBreContext.
        Unique display id.

        :param id: The id of this NdmpContextsBreContext.
        :type: str
        """
        
        self._id = id

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

