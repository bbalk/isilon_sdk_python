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


class AuditSettingsSettings(object):
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
        'audit_failure': 'list[str]',
        'audit_success': 'list[str]',
        'syslog_audit_events': 'list[str]',
        'syslog_forwarding_enabled': 'bool'
    }

    attribute_map = {
        'audit_failure': 'audit_failure',
        'audit_success': 'audit_success',
        'syslog_audit_events': 'syslog_audit_events',
        'syslog_forwarding_enabled': 'syslog_forwarding_enabled'
    }

    def __init__(self, audit_failure=None, audit_success=None, syslog_audit_events=None, syslog_forwarding_enabled=None):  # noqa: E501
        """AuditSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._audit_failure = None
        self._audit_success = None
        self._syslog_audit_events = None
        self._syslog_forwarding_enabled = None
        self.discriminator = None

        if audit_failure is not None:
            self.audit_failure = audit_failure
        if audit_success is not None:
            self.audit_success = audit_success
        if syslog_audit_events is not None:
            self.syslog_audit_events = syslog_audit_events
        if syslog_forwarding_enabled is not None:
            self.syslog_forwarding_enabled = syslog_forwarding_enabled

    @property
    def audit_failure(self):
        """Gets the audit_failure of this AuditSettingsSettings.  # noqa: E501

        Filter of protocol operations to Audit when they fail.  # noqa: E501

        :return: The audit_failure of this AuditSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._audit_failure

    @audit_failure.setter
    def audit_failure(self, audit_failure):
        """Sets the audit_failure of this AuditSettingsSettings.

        Filter of protocol operations to Audit when they fail.  # noqa: E501

        :param audit_failure: The audit_failure of this AuditSettingsSettings.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["close", "create", "delete", "get_security", "logoff", "logon", "read", "rename", "set_security", "tree_connect", "write"]  # noqa: E501
        if not set(audit_failure).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `audit_failure` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(audit_failure) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._audit_failure = audit_failure

    @property
    def audit_success(self):
        """Gets the audit_success of this AuditSettingsSettings.  # noqa: E501

        Filter of protocol operations to Audit when they succeed.  # noqa: E501

        :return: The audit_success of this AuditSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._audit_success

    @audit_success.setter
    def audit_success(self, audit_success):
        """Sets the audit_success of this AuditSettingsSettings.

        Filter of protocol operations to Audit when they succeed.  # noqa: E501

        :param audit_success: The audit_success of this AuditSettingsSettings.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["close", "create", "delete", "get_security", "logoff", "logon", "read", "rename", "set_security", "tree_connect", "write"]  # noqa: E501
        if not set(audit_success).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `audit_success` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(audit_success) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._audit_success = audit_success

    @property
    def syslog_audit_events(self):
        """Gets the syslog_audit_events of this AuditSettingsSettings.  # noqa: E501

        Filter of Audit operations to forward to syslog.  # noqa: E501

        :return: The syslog_audit_events of this AuditSettingsSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._syslog_audit_events

    @syslog_audit_events.setter
    def syslog_audit_events(self, syslog_audit_events):
        """Sets the syslog_audit_events of this AuditSettingsSettings.

        Filter of Audit operations to forward to syslog.  # noqa: E501

        :param syslog_audit_events: The syslog_audit_events of this AuditSettingsSettings.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["close", "create", "delete", "get_security", "logoff", "logon", "read", "rename", "set_security", "tree_connect", "write"]  # noqa: E501
        if not set(syslog_audit_events).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `syslog_audit_events` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(syslog_audit_events) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._syslog_audit_events = syslog_audit_events

    @property
    def syslog_forwarding_enabled(self):
        """Gets the syslog_forwarding_enabled of this AuditSettingsSettings.  # noqa: E501

        Enables forwarding of events to syslog.  # noqa: E501

        :return: The syslog_forwarding_enabled of this AuditSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._syslog_forwarding_enabled

    @syslog_forwarding_enabled.setter
    def syslog_forwarding_enabled(self, syslog_forwarding_enabled):
        """Sets the syslog_forwarding_enabled of this AuditSettingsSettings.

        Enables forwarding of events to syslog.  # noqa: E501

        :param syslog_forwarding_enabled: The syslog_forwarding_enabled of this AuditSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._syslog_forwarding_enabled = syslog_forwarding_enabled

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
        if issubclass(AuditSettingsSettings, dict):
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
        if not isinstance(other, AuditSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
