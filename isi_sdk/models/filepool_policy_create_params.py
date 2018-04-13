# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 4
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_0_1.models.filepool_policy_action_create_params import FilepoolPolicyActionCreateParams  # noqa: F401,E501
from isi_sdk_8_0_1.models.filepool_policy_file_matching_pattern import FilepoolPolicyFileMatchingPattern  # noqa: F401,E501


class FilepoolPolicyCreateParams(object):
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
        'actions': 'list[FilepoolPolicyActionCreateParams]',
        'apply_order': 'int',
        'description': 'str',
        'file_matching_pattern': 'FilepoolPolicyFileMatchingPattern',
        'name': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'apply_order': 'apply_order',
        'description': 'description',
        'file_matching_pattern': 'file_matching_pattern',
        'name': 'name'
    }

    def __init__(self, actions=None, apply_order=None, description=None, file_matching_pattern=None, name=None):  # noqa: E501
        """FilepoolPolicyCreateParams - a model defined in Swagger"""  # noqa: E501

        self._actions = None
        self._apply_order = None
        self._description = None
        self._file_matching_pattern = None
        self._name = None
        self.discriminator = None

        if actions is not None:
            self.actions = actions
        if apply_order is not None:
            self.apply_order = apply_order
        if description is not None:
            self.description = description
        self.file_matching_pattern = file_matching_pattern
        self.name = name

    @property
    def actions(self):
        """Gets the actions of this FilepoolPolicyCreateParams.  # noqa: E501

        A list of actions to be taken for matching files  # noqa: E501

        :return: The actions of this FilepoolPolicyCreateParams.  # noqa: E501
        :rtype: list[FilepoolPolicyActionCreateParams]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this FilepoolPolicyCreateParams.

        A list of actions to be taken for matching files  # noqa: E501

        :param actions: The actions of this FilepoolPolicyCreateParams.  # noqa: E501
        :type: list[FilepoolPolicyActionCreateParams]
        """

        self._actions = actions

    @property
    def apply_order(self):
        """Gets the apply_order of this FilepoolPolicyCreateParams.  # noqa: E501

        The order in which this policy should be applied (relative to other policies)  # noqa: E501

        :return: The apply_order of this FilepoolPolicyCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._apply_order

    @apply_order.setter
    def apply_order(self, apply_order):
        """Sets the apply_order of this FilepoolPolicyCreateParams.

        The order in which this policy should be applied (relative to other policies)  # noqa: E501

        :param apply_order: The apply_order of this FilepoolPolicyCreateParams.  # noqa: E501
        :type: int
        """

        self._apply_order = apply_order

    @property
    def description(self):
        """Gets the description of this FilepoolPolicyCreateParams.  # noqa: E501

        A description for this policy  # noqa: E501

        :return: The description of this FilepoolPolicyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FilepoolPolicyCreateParams.

        A description for this policy  # noqa: E501

        :param description: The description of this FilepoolPolicyCreateParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file_matching_pattern(self):
        """Gets the file_matching_pattern of this FilepoolPolicyCreateParams.  # noqa: E501

        The file matching rules for this policy  # noqa: E501

        :return: The file_matching_pattern of this FilepoolPolicyCreateParams.  # noqa: E501
        :rtype: FilepoolPolicyFileMatchingPattern
        """
        return self._file_matching_pattern

    @file_matching_pattern.setter
    def file_matching_pattern(self, file_matching_pattern):
        """Sets the file_matching_pattern of this FilepoolPolicyCreateParams.

        The file matching rules for this policy  # noqa: E501

        :param file_matching_pattern: The file_matching_pattern of this FilepoolPolicyCreateParams.  # noqa: E501
        :type: FilepoolPolicyFileMatchingPattern
        """
        if file_matching_pattern is None:
            raise ValueError("Invalid value for `file_matching_pattern`, must not be `None`")  # noqa: E501

        self._file_matching_pattern = file_matching_pattern

    @property
    def name(self):
        """Gets the name of this FilepoolPolicyCreateParams.  # noqa: E501

        A unique name for this policy  # noqa: E501

        :return: The name of this FilepoolPolicyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilepoolPolicyCreateParams.

        A unique name for this policy  # noqa: E501

        :param name: The name of this FilepoolPolicyCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FilepoolPolicyCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
