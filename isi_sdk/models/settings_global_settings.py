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


class SettingsGlobalSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SettingsGlobalSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'audited_zones': 'list[str]',
            'cee_log_time': 'str',
            'cee_server_uris': 'list[str]',
            'config_auditing_enabled': 'bool',
            'config_syslog_enabled': 'bool',
            'hostname': 'str',
            'protocol_auditing_enabled': 'bool',
            'syslog_log_time': 'str'
        }

        self.attribute_map = {
            'audited_zones': 'audited_zones',
            'cee_log_time': 'cee_log_time',
            'cee_server_uris': 'cee_server_uris',
            'config_auditing_enabled': 'config_auditing_enabled',
            'config_syslog_enabled': 'config_syslog_enabled',
            'hostname': 'hostname',
            'protocol_auditing_enabled': 'protocol_auditing_enabled',
            'syslog_log_time': 'syslog_log_time'
        }

        self._audited_zones = None
        self._cee_log_time = None
        self._cee_server_uris = None
        self._config_auditing_enabled = None
        self._config_syslog_enabled = None
        self._hostname = None
        self._protocol_auditing_enabled = None
        self._syslog_log_time = None

    @property
    def audited_zones(self):
        """
        Gets the audited_zones of this SettingsGlobalSettings.
        Specifies zones that are audited when the protocol_auditing_enabled property is enabled.

        :return: The audited_zones of this SettingsGlobalSettings.
        :rtype: list[str]
        """
        return self._audited_zones

    @audited_zones.setter
    def audited_zones(self, audited_zones):
        """
        Sets the audited_zones of this SettingsGlobalSettings.
        Specifies zones that are audited when the protocol_auditing_enabled property is enabled.

        :param audited_zones: The audited_zones of this SettingsGlobalSettings.
        :type: list[str]
        """
        
        self._audited_zones = audited_zones

    @property
    def cee_log_time(self):
        """
        Gets the cee_log_time of this SettingsGlobalSettings.
        Specifies that events past a certain date are forwarded by the audit CEE forwarder. Format these events as follows: 'Topic@YYYY-MM-DD HH:MM:SS'.

        :return: The cee_log_time of this SettingsGlobalSettings.
        :rtype: str
        """
        return self._cee_log_time

    @cee_log_time.setter
    def cee_log_time(self, cee_log_time):
        """
        Sets the cee_log_time of this SettingsGlobalSettings.
        Specifies that events past a certain date are forwarded by the audit CEE forwarder. Format these events as follows: 'Topic@YYYY-MM-DD HH:MM:SS'.

        :param cee_log_time: The cee_log_time of this SettingsGlobalSettings.
        :type: str
        """
        
        self._cee_log_time = cee_log_time

    @property
    def cee_server_uris(self):
        """
        Gets the cee_server_uris of this SettingsGlobalSettings.
        Specifies a list of Common Event Enabler (CEE) server URIs. Protocol audit logs are sent to these URIs for external processing.

        :return: The cee_server_uris of this SettingsGlobalSettings.
        :rtype: list[str]
        """
        return self._cee_server_uris

    @cee_server_uris.setter
    def cee_server_uris(self, cee_server_uris):
        """
        Sets the cee_server_uris of this SettingsGlobalSettings.
        Specifies a list of Common Event Enabler (CEE) server URIs. Protocol audit logs are sent to these URIs for external processing.

        :param cee_server_uris: The cee_server_uris of this SettingsGlobalSettings.
        :type: list[str]
        """
        
        self._cee_server_uris = cee_server_uris

    @property
    def config_auditing_enabled(self):
        """
        Gets the config_auditing_enabled of this SettingsGlobalSettings.
        Specifies whether logging for API configuration changes are enabled.

        :return: The config_auditing_enabled of this SettingsGlobalSettings.
        :rtype: bool
        """
        return self._config_auditing_enabled

    @config_auditing_enabled.setter
    def config_auditing_enabled(self, config_auditing_enabled):
        """
        Sets the config_auditing_enabled of this SettingsGlobalSettings.
        Specifies whether logging for API configuration changes are enabled.

        :param config_auditing_enabled: The config_auditing_enabled of this SettingsGlobalSettings.
        :type: bool
        """
        
        self._config_auditing_enabled = config_auditing_enabled

    @property
    def config_syslog_enabled(self):
        """
        Gets the config_syslog_enabled of this SettingsGlobalSettings.
        Specifies whether configuration audit syslog messages are forwarded.

        :return: The config_syslog_enabled of this SettingsGlobalSettings.
        :rtype: bool
        """
        return self._config_syslog_enabled

    @config_syslog_enabled.setter
    def config_syslog_enabled(self, config_syslog_enabled):
        """
        Sets the config_syslog_enabled of this SettingsGlobalSettings.
        Specifies whether configuration audit syslog messages are forwarded.

        :param config_syslog_enabled: The config_syslog_enabled of this SettingsGlobalSettings.
        :type: bool
        """
        
        self._config_syslog_enabled = config_syslog_enabled

    @property
    def hostname(self):
        """
        Gets the hostname of this SettingsGlobalSettings.
        Specifies the hostname that is reported in protocol events from this cluster.

        :return: The hostname of this SettingsGlobalSettings.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this SettingsGlobalSettings.
        Specifies the hostname that is reported in protocol events from this cluster.

        :param hostname: The hostname of this SettingsGlobalSettings.
        :type: str
        """
        
        self._hostname = hostname

    @property
    def protocol_auditing_enabled(self):
        """
        Gets the protocol_auditing_enabled of this SettingsGlobalSettings.
        Specifies if logging for the I/O stream is enabled.

        :return: The protocol_auditing_enabled of this SettingsGlobalSettings.
        :rtype: bool
        """
        return self._protocol_auditing_enabled

    @protocol_auditing_enabled.setter
    def protocol_auditing_enabled(self, protocol_auditing_enabled):
        """
        Sets the protocol_auditing_enabled of this SettingsGlobalSettings.
        Specifies if logging for the I/O stream is enabled.

        :param protocol_auditing_enabled: The protocol_auditing_enabled of this SettingsGlobalSettings.
        :type: bool
        """
        
        self._protocol_auditing_enabled = protocol_auditing_enabled

    @property
    def syslog_log_time(self):
        """
        Gets the syslog_log_time of this SettingsGlobalSettings.
        Specifies that events past a specified date are forwarded by the audit syslog forwarder. Format these events as follows: 'Topic@YYYY-MM-DD HH:MM:SS' format

        :return: The syslog_log_time of this SettingsGlobalSettings.
        :rtype: str
        """
        return self._syslog_log_time

    @syslog_log_time.setter
    def syslog_log_time(self, syslog_log_time):
        """
        Sets the syslog_log_time of this SettingsGlobalSettings.
        Specifies that events past a specified date are forwarded by the audit syslog forwarder. Format these events as follows: 'Topic@YYYY-MM-DD HH:MM:SS' format

        :param syslog_log_time: The syslog_log_time of this SettingsGlobalSettings.
        :type: str
        """
        
        self._syslog_log_time = syslog_log_time

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

