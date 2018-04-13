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

from isi_sdk_8_0_1.models.settings_mapping_mapping_settings import SettingsMappingMappingSettings  # noqa: F401,E501


class SettingsMapping(object):
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
        'mapping_settings': 'SettingsMappingMappingSettings'
    }

    attribute_map = {
        'mapping_settings': 'mapping_settings'
    }

    def __init__(self, mapping_settings=None):  # noqa: E501
        """SettingsMapping - a model defined in Swagger"""  # noqa: E501

        self._mapping_settings = None
        self.discriminator = None

        if mapping_settings is not None:
            self.mapping_settings = mapping_settings

    @property
    def mapping_settings(self):
        """Gets the mapping_settings of this SettingsMapping.  # noqa: E501

        Specifies the properties for global authentication setting.  # noqa: E501

        :return: The mapping_settings of this SettingsMapping.  # noqa: E501
        :rtype: SettingsMappingMappingSettings
        """
        return self._mapping_settings

    @mapping_settings.setter
    def mapping_settings(self, mapping_settings):
        """Sets the mapping_settings of this SettingsMapping.

        Specifies the properties for global authentication setting.  # noqa: E501

        :param mapping_settings: The mapping_settings of this SettingsMapping.  # noqa: E501
        :type: SettingsMappingMappingSettings
        """

        self._mapping_settings = mapping_settings

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
        if not isinstance(other, SettingsMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
