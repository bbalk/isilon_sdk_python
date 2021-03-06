# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 6
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateCompatibilitiesClassActiveItemResponseMerge(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ids': 'list[int]',
        'names': 'list[str]',
        'result_name': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'names': 'names',
        'result_name': 'result_name'
    }

    def __init__(self, ids=None, names=None, result_name=None):  # noqa: E501
        """CreateCompatibilitiesClassActiveItemResponseMerge - a model defined in Swagger"""  # noqa: E501

        self._ids = None
        self._names = None
        self._result_name = None
        self.discriminator = None

        self.ids = ids
        self.names = names
        self.result_name = result_name

    @property
    def ids(self):
        """Gets the ids of this CreateCompatibilitiesClassActiveItemResponseMerge.  # noqa: E501

        The nodepool ids that will be merged  # noqa: E501

        :return: The ids of this CreateCompatibilitiesClassActiveItemResponseMerge.  # noqa: E501
        :rtype: list[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this CreateCompatibilitiesClassActiveItemResponseMerge.

        The nodepool ids that will be merged  # noqa: E501

        :param ids: The ids of this CreateCompatibilitiesClassActiveItemResponseMerge.  # noqa: E501
        :type: list[int]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")  # noqa: E501

        self._ids = ids

    @property
    def names(self):
        """Gets the names of this CreateCompatibilitiesClassActiveItemResponseMerge.  # noqa: E501

        The nodepool names that will be merged, in the sameorder as the ids  # noqa: E501

        :return: The names of this CreateCompatibilitiesClassActiveItemResponseMerge.  # noqa: E501
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this CreateCompatibilitiesClassActiveItemResponseMerge.

        The nodepool names that will be merged, in the sameorder as the ids  # noqa: E501

        :param names: The names of this CreateCompatibilitiesClassActiveItemResponseMerge.  # noqa: E501
        :type: list[str]
        """
        if names is None:
            raise ValueError("Invalid value for `names`, must not be `None`")  # noqa: E501

        self._names = names

    @property
    def result_name(self):
        """Gets the result_name of this CreateCompatibilitiesClassActiveItemResponseMerge.  # noqa: E501

        The name of the nodepool all others will merge into  # noqa: E501

        :return: The result_name of this CreateCompatibilitiesClassActiveItemResponseMerge.  # noqa: E501
        :rtype: str
        """
        return self._result_name

    @result_name.setter
    def result_name(self, result_name):
        """Sets the result_name of this CreateCompatibilitiesClassActiveItemResponseMerge.

        The name of the nodepool all others will merge into  # noqa: E501

        :param result_name: The result_name of this CreateCompatibilitiesClassActiveItemResponseMerge.  # noqa: E501
        :type: str
        """
        if result_name is None:
            raise ValueError("Invalid value for `result_name`, must not be `None`")  # noqa: E501

        self._result_name = result_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CreateCompatibilitiesClassActiveItemResponseMerge, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateCompatibilitiesClassActiveItemResponseMerge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
