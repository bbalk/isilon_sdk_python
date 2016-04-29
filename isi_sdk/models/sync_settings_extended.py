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


class SyncSettingsExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SyncSettingsExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'settings': 'SyncSettingsSettings',
            'burst_memory_constraint': 'int',
            'restrict_target_network': 'bool',
            'force_interface': 'bool',
            'service': 'str',
            'report_max_count': 'int',
            'report_email': 'list[str]',
            'rpo_alerts': 'bool',
            'burst_socket_buffer_size': 'int',
            'report_max_age': 'int',
            'source_network': 'SyncPolicySourceNetwork'
        }

        self.attribute_map = {
            'settings': 'settings',
            'burst_memory_constraint': 'burst_memory_constraint',
            'restrict_target_network': 'restrict_target_network',
            'force_interface': 'force_interface',
            'service': 'service',
            'report_max_count': 'report_max_count',
            'report_email': 'report_email',
            'rpo_alerts': 'rpo_alerts',
            'burst_socket_buffer_size': 'burst_socket_buffer_size',
            'report_max_age': 'report_max_age',
            'source_network': 'source_network'
        }

        self._settings = None
        self._burst_memory_constraint = None
        self._restrict_target_network = None
        self._force_interface = None
        self._service = None
        self._report_max_count = None
        self._report_email = None
        self._rpo_alerts = None
        self._burst_socket_buffer_size = None
        self._report_max_age = None
        self._source_network = None

    @property
    def settings(self):
        """
        Gets the settings of this SyncSettingsExtended.
        Global SyncIQ settings.

        :return: The settings of this SyncSettingsExtended.
        :rtype: SyncSettingsSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this SyncSettingsExtended.
        Global SyncIQ settings.

        :param settings: The settings of this SyncSettingsExtended.
        :type: SyncSettingsSettings
        """
        self._settings = settings

    @property
    def burst_memory_constraint(self):
        """
        Gets the burst_memory_constraint of this SyncSettingsExtended.
        The per-worker burst socket memory constraint, in bytes.

        :return: The burst_memory_constraint of this SyncSettingsExtended.
        :rtype: int
        """
        return self._burst_memory_constraint

    @burst_memory_constraint.setter
    def burst_memory_constraint(self, burst_memory_constraint):
        """
        Sets the burst_memory_constraint of this SyncSettingsExtended.
        The per-worker burst socket memory constraint, in bytes.

        :param burst_memory_constraint: The burst_memory_constraint of this SyncSettingsExtended.
        :type: int
        """
        self._burst_memory_constraint = burst_memory_constraint

    @property
    def restrict_target_network(self):
        """
        Gets the restrict_target_network of this SyncSettingsExtended.
        Default for the \"restrict_target_network\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \"target_host\" field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster.

        :return: The restrict_target_network of this SyncSettingsExtended.
        :rtype: bool
        """
        return self._restrict_target_network

    @restrict_target_network.setter
    def restrict_target_network(self, restrict_target_network):
        """
        Sets the restrict_target_network of this SyncSettingsExtended.
        Default for the \"restrict_target_network\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \"target_host\" field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster.

        :param restrict_target_network: The restrict_target_network of this SyncSettingsExtended.
        :type: bool
        """
        self._restrict_target_network = restrict_target_network

    @property
    def force_interface(self):
        """
        Gets the force_interface of this SyncSettingsExtended.
        NOTE: This field should not be changed without the help of Isilon support.  Default for the \"force_interface\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \"source_network\" field. This option can be useful if there are multiple interfaces for the given source subnet.

        :return: The force_interface of this SyncSettingsExtended.
        :rtype: bool
        """
        return self._force_interface

    @force_interface.setter
    def force_interface(self, force_interface):
        """
        Sets the force_interface of this SyncSettingsExtended.
        NOTE: This field should not be changed without the help of Isilon support.  Default for the \"force_interface\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \"source_network\" field. This option can be useful if there are multiple interfaces for the given source subnet.

        :param force_interface: The force_interface of this SyncSettingsExtended.
        :type: bool
        """
        self._force_interface = force_interface

    @property
    def service(self):
        """
        Gets the service of this SyncSettingsExtended.
        Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled.

        :return: The service of this SyncSettingsExtended.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this SyncSettingsExtended.
        Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled.

        :param service: The service of this SyncSettingsExtended.
        :type: str
        """
        allowed_values = ["on", "off", "paused"]
        if service not in allowed_values:
            raise ValueError(
                "Invalid value for `service`, must be one of {0}"
                .format(allowed_values)
            )
        self._service = service

    @property
    def report_max_count(self):
        """
        Gets the report_max_count of this SyncSettingsExtended.
        The default maximum number of reports to retain for a policy.

        :return: The report_max_count of this SyncSettingsExtended.
        :rtype: int
        """
        return self._report_max_count

    @report_max_count.setter
    def report_max_count(self, report_max_count):
        """
        Sets the report_max_count of this SyncSettingsExtended.
        The default maximum number of reports to retain for a policy.

        :param report_max_count: The report_max_count of this SyncSettingsExtended.
        :type: int
        """
        self._report_max_count = report_max_count

    @property
    def report_email(self):
        """
        Gets the report_email of this SyncSettingsExtended.
        Email sync reports to these addresses.

        :return: The report_email of this SyncSettingsExtended.
        :rtype: list[str]
        """
        return self._report_email

    @report_email.setter
    def report_email(self, report_email):
        """
        Sets the report_email of this SyncSettingsExtended.
        Email sync reports to these addresses.

        :param report_email: The report_email of this SyncSettingsExtended.
        :type: list[str]
        """
        self._report_email = report_email

    @property
    def rpo_alerts(self):
        """
        Gets the rpo_alerts of this SyncSettingsExtended.
        If disabled, no RPO alerts will be generated.

        :return: The rpo_alerts of this SyncSettingsExtended.
        :rtype: bool
        """
        return self._rpo_alerts

    @rpo_alerts.setter
    def rpo_alerts(self, rpo_alerts):
        """
        Sets the rpo_alerts of this SyncSettingsExtended.
        If disabled, no RPO alerts will be generated.

        :param rpo_alerts: The rpo_alerts of this SyncSettingsExtended.
        :type: bool
        """
        self._rpo_alerts = rpo_alerts

    @property
    def burst_socket_buffer_size(self):
        """
        Gets the burst_socket_buffer_size of this SyncSettingsExtended.
        The per-worker burst socket buffer coalesced data, in bytes.

        :return: The burst_socket_buffer_size of this SyncSettingsExtended.
        :rtype: int
        """
        return self._burst_socket_buffer_size

    @burst_socket_buffer_size.setter
    def burst_socket_buffer_size(self, burst_socket_buffer_size):
        """
        Sets the burst_socket_buffer_size of this SyncSettingsExtended.
        The per-worker burst socket buffer coalesced data, in bytes.

        :param burst_socket_buffer_size: The burst_socket_buffer_size of this SyncSettingsExtended.
        :type: int
        """
        self._burst_socket_buffer_size = burst_socket_buffer_size

    @property
    def report_max_age(self):
        """
        Gets the report_max_age of this SyncSettingsExtended.
        The default length of time (in seconds) a policy report will be stored.

        :return: The report_max_age of this SyncSettingsExtended.
        :rtype: int
        """
        return self._report_max_age

    @report_max_age.setter
    def report_max_age(self, report_max_age):
        """
        Sets the report_max_age of this SyncSettingsExtended.
        The default length of time (in seconds) a policy report will be stored.

        :param report_max_age: The report_max_age of this SyncSettingsExtended.
        :type: int
        """
        self._report_max_age = report_max_age

    @property
    def source_network(self):
        """
        Gets the source_network of this SyncSettingsExtended.
        Restricts replication policies on the local cluster to running on the specified subnet and pool.

        :return: The source_network of this SyncSettingsExtended.
        :rtype: SyncPolicySourceNetwork
        """
        return self._source_network

    @source_network.setter
    def source_network(self, source_network):
        """
        Sets the source_network of this SyncSettingsExtended.
        Restricts replication policies on the local cluster to running on the specified subnet and pool.

        :param source_network: The source_network of this SyncSettingsExtended.
        :type: SyncPolicySourceNetwork
        """
        self._source_network = source_network

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

