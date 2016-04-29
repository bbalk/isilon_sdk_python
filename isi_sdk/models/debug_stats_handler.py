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


class DebugStatsHandler(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DebugStatsHandler - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'delete': 'DebugStatsUnknown',
            'get': 'DebugStatsUnknown',
            'head': 'DebugStatsUnknown',
            'post': 'DebugStatsUnknown',
            'put': 'DebugStatsUnknown',
            'unsupported': 'DebugStatsUnknown',
            'name': 'str'
        }

        self.attribute_map = {
            'delete': 'DELETE',
            'get': 'GET',
            'head': 'HEAD',
            'post': 'POST',
            'put': 'PUT',
            'unsupported': 'UNSUPPORTED',
            'name': 'name'
        }

        self._delete = None
        self._get = None
        self._head = None
        self._post = None
        self._put = None
        self._unsupported = None
        self._name = None

    @property
    def delete(self):
        """
        Gets the delete of this DebugStatsHandler.
        Per-method statistics.

        :return: The delete of this DebugStatsHandler.
        :rtype: DebugStatsUnknown
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """
        Sets the delete of this DebugStatsHandler.
        Per-method statistics.

        :param delete: The delete of this DebugStatsHandler.
        :type: DebugStatsUnknown
        """
        self._delete = delete

    @property
    def get(self):
        """
        Gets the get of this DebugStatsHandler.
        Per-method statistics.

        :return: The get of this DebugStatsHandler.
        :rtype: DebugStatsUnknown
        """
        return self._get

    @get.setter
    def get(self, get):
        """
        Sets the get of this DebugStatsHandler.
        Per-method statistics.

        :param get: The get of this DebugStatsHandler.
        :type: DebugStatsUnknown
        """
        self._get = get

    @property
    def head(self):
        """
        Gets the head of this DebugStatsHandler.
        Per-method statistics.

        :return: The head of this DebugStatsHandler.
        :rtype: DebugStatsUnknown
        """
        return self._head

    @head.setter
    def head(self, head):
        """
        Sets the head of this DebugStatsHandler.
        Per-method statistics.

        :param head: The head of this DebugStatsHandler.
        :type: DebugStatsUnknown
        """
        self._head = head

    @property
    def post(self):
        """
        Gets the post of this DebugStatsHandler.
        Per-method statistics.

        :return: The post of this DebugStatsHandler.
        :rtype: DebugStatsUnknown
        """
        return self._post

    @post.setter
    def post(self, post):
        """
        Sets the post of this DebugStatsHandler.
        Per-method statistics.

        :param post: The post of this DebugStatsHandler.
        :type: DebugStatsUnknown
        """
        self._post = post

    @property
    def put(self):
        """
        Gets the put of this DebugStatsHandler.
        Per-method statistics.

        :return: The put of this DebugStatsHandler.
        :rtype: DebugStatsUnknown
        """
        return self._put

    @put.setter
    def put(self, put):
        """
        Sets the put of this DebugStatsHandler.
        Per-method statistics.

        :param put: The put of this DebugStatsHandler.
        :type: DebugStatsUnknown
        """
        self._put = put

    @property
    def unsupported(self):
        """
        Gets the unsupported of this DebugStatsHandler.
        Per-method statistics.

        :return: The unsupported of this DebugStatsHandler.
        :rtype: DebugStatsUnknown
        """
        return self._unsupported

    @unsupported.setter
    def unsupported(self, unsupported):
        """
        Sets the unsupported of this DebugStatsHandler.
        Per-method statistics.

        :param unsupported: The unsupported of this DebugStatsHandler.
        :type: DebugStatsUnknown
        """
        self._unsupported = unsupported

    @property
    def name(self):
        """
        Gets the name of this DebugStatsHandler.
        The URI.

        :return: The name of this DebugStatsHandler.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DebugStatsHandler.
        The URI.

        :param name: The name of this DebugStatsHandler.
        :type: str
        """
        self._name = name

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

