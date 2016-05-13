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


class SyncSettingsSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SyncSettingsSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'burst_memory_constraint': 'int',
            'burst_socket_buffer_size': 'int',
            'force_interface': 'bool',
            'max_concurrent_jobs': 'int',
            'report_email': 'list[str]',
            'report_max_age': 'int',
            'report_max_count': 'int',
            'restrict_target_network': 'bool',
            'rpo_alerts': 'bool',
            'service': 'str',
            'source_network': 'SyncPolicySourceNetwork'
        }

        self.attribute_map = {
            'burst_memory_constraint': 'burst_memory_constraint',
            'burst_socket_buffer_size': 'burst_socket_buffer_size',
            'force_interface': 'force_interface',
            'max_concurrent_jobs': 'max_concurrent_jobs',
            'report_email': 'report_email',
            'report_max_age': 'report_max_age',
            'report_max_count': 'report_max_count',
            'restrict_target_network': 'restrict_target_network',
            'rpo_alerts': 'rpo_alerts',
            'service': 'service',
            'source_network': 'source_network'
        }

        self._burst_memory_constraint = None
        self._burst_socket_buffer_size = None
        self._force_interface = None
        self._max_concurrent_jobs = None
        self._report_email = None
        self._report_max_age = None
        self._report_max_count = None
        self._restrict_target_network = None
        self._rpo_alerts = None
        self._service = None
        self._source_network = None

    @property
    def burst_memory_constraint(self):
        """
        Gets the burst_memory_constraint of this SyncSettingsSettings.
        The per-worker burst socket memory constraint, in bytes.

        :return: The burst_memory_constraint of this SyncSettingsSettings.
        :rtype: int
        """
        return self._burst_memory_constraint

    @burst_memory_constraint.setter
    def burst_memory_constraint(self, burst_memory_constraint):
        """
        Sets the burst_memory_constraint of this SyncSettingsSettings.
        The per-worker burst socket memory constraint, in bytes.

        :param burst_memory_constraint: The burst_memory_constraint of this SyncSettingsSettings.
        :type: int
        """
        
        self._burst_memory_constraint = burst_memory_constraint

    @property
    def burst_socket_buffer_size(self):
        """
        Gets the burst_socket_buffer_size of this SyncSettingsSettings.
        The per-worker burst socket buffer coalesced data, in bytes.

        :return: The burst_socket_buffer_size of this SyncSettingsSettings.
        :rtype: int
        """
        return self._burst_socket_buffer_size

    @burst_socket_buffer_size.setter
    def burst_socket_buffer_size(self, burst_socket_buffer_size):
        """
        Sets the burst_socket_buffer_size of this SyncSettingsSettings.
        The per-worker burst socket buffer coalesced data, in bytes.

        :param burst_socket_buffer_size: The burst_socket_buffer_size of this SyncSettingsSettings.
        :type: int
        """
        
        self._burst_socket_buffer_size = burst_socket_buffer_size

    @property
    def force_interface(self):
        """
        Gets the force_interface of this SyncSettingsSettings.
        NOTE: This field should not be changed without the help of Isilon support.  Default for the \"force_interface\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \"source_network\" field. This option can be useful if there are multiple interfaces for the given source subnet.

        :return: The force_interface of this SyncSettingsSettings.
        :rtype: bool
        """
        return self._force_interface

    @force_interface.setter
    def force_interface(self, force_interface):
        """
        Sets the force_interface of this SyncSettingsSettings.
        NOTE: This field should not be changed without the help of Isilon support.  Default for the \"force_interface\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \"source_network\" field. This option can be useful if there are multiple interfaces for the given source subnet.

        :param force_interface: The force_interface of this SyncSettingsSettings.
        :type: bool
        """
        
        self._force_interface = force_interface

    @property
    def max_concurrent_jobs(self):
        """
        Gets the max_concurrent_jobs of this SyncSettingsSettings.
        The max concurrent jobs that SyncIQ can support. This number is based on the size of the current cluster and the current SyncIQ worker throttle rule.

        :return: The max_concurrent_jobs of this SyncSettingsSettings.
        :rtype: int
        """
        return self._max_concurrent_jobs

    @max_concurrent_jobs.setter
    def max_concurrent_jobs(self, max_concurrent_jobs):
        """
        Sets the max_concurrent_jobs of this SyncSettingsSettings.
        The max concurrent jobs that SyncIQ can support. This number is based on the size of the current cluster and the current SyncIQ worker throttle rule.

        :param max_concurrent_jobs: The max_concurrent_jobs of this SyncSettingsSettings.
        :type: int
        """
        
        self._max_concurrent_jobs = max_concurrent_jobs

    @property
    def report_email(self):
        """
        Gets the report_email of this SyncSettingsSettings.
        Email sync reports to these addresses.

        :return: The report_email of this SyncSettingsSettings.
        :rtype: list[str]
        """
        return self._report_email

    @report_email.setter
    def report_email(self, report_email):
        """
        Sets the report_email of this SyncSettingsSettings.
        Email sync reports to these addresses.

        :param report_email: The report_email of this SyncSettingsSettings.
        :type: list[str]
        """
        
        self._report_email = report_email

    @property
    def report_max_age(self):
        """
        Gets the report_max_age of this SyncSettingsSettings.
        The default length of time (in seconds) a policy report will be stored.

        :return: The report_max_age of this SyncSettingsSettings.
        :rtype: int
        """
        return self._report_max_age

    @report_max_age.setter
    def report_max_age(self, report_max_age):
        """
        Sets the report_max_age of this SyncSettingsSettings.
        The default length of time (in seconds) a policy report will be stored.

        :param report_max_age: The report_max_age of this SyncSettingsSettings.
        :type: int
        """
        
        self._report_max_age = report_max_age

    @property
    def report_max_count(self):
        """
        Gets the report_max_count of this SyncSettingsSettings.
        The default maximum number of reports to retain for a policy.

        :return: The report_max_count of this SyncSettingsSettings.
        :rtype: int
        """
        return self._report_max_count

    @report_max_count.setter
    def report_max_count(self, report_max_count):
        """
        Sets the report_max_count of this SyncSettingsSettings.
        The default maximum number of reports to retain for a policy.

        :param report_max_count: The report_max_count of this SyncSettingsSettings.
        :type: int
        """
        
        if not report_max_count:
            raise ValueError("Invalid value for `report_max_count`, must not be `None`")
        if report_max_count > 2000.0: 
            raise ValueError("Invalid value for `report_max_count`, must be a value less than or equal to `2000.0`")
        if report_max_count < 1.0: 
            raise ValueError("Invalid value for `report_max_count`, must be a value greater than or equal to `1.0`")

        self._report_max_count = report_max_count

    @property
    def restrict_target_network(self):
        """
        Gets the restrict_target_network of this SyncSettingsSettings.
        Default for the \"restrict_target_network\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \"target_host\" field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster.

        :return: The restrict_target_network of this SyncSettingsSettings.
        :rtype: bool
        """
        return self._restrict_target_network

    @restrict_target_network.setter
    def restrict_target_network(self, restrict_target_network):
        """
        Sets the restrict_target_network of this SyncSettingsSettings.
        Default for the \"restrict_target_network\" property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \"target_host\" field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster.

        :param restrict_target_network: The restrict_target_network of this SyncSettingsSettings.
        :type: bool
        """
        
        self._restrict_target_network = restrict_target_network

    @property
    def rpo_alerts(self):
        """
        Gets the rpo_alerts of this SyncSettingsSettings.
        If disabled, no RPO alerts will be generated.

        :return: The rpo_alerts of this SyncSettingsSettings.
        :rtype: bool
        """
        return self._rpo_alerts

    @rpo_alerts.setter
    def rpo_alerts(self, rpo_alerts):
        """
        Sets the rpo_alerts of this SyncSettingsSettings.
        If disabled, no RPO alerts will be generated.

        :param rpo_alerts: The rpo_alerts of this SyncSettingsSettings.
        :type: bool
        """
        
        self._rpo_alerts = rpo_alerts

    @property
    def service(self):
        """
        Gets the service of this SyncSettingsSettings.
        Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled.

        :return: The service of this SyncSettingsSettings.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this SyncSettingsSettings.
        Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled.

        :param service: The service of this SyncSettingsSettings.
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
    def source_network(self):
        """
        Gets the source_network of this SyncSettingsSettings.
        Restricts replication policies on the local cluster to running on the specified subnet and pool.

        :return: The source_network of this SyncSettingsSettings.
        :rtype: SyncPolicySourceNetwork
        """
        return self._source_network

    @source_network.setter
    def source_network(self, source_network):
        """
        Sets the source_network of this SyncSettingsSettings.
        Restricts replication policies on the local cluster to running on the specified subnet and pool.

        :param source_network: The source_network of this SyncSettingsSettings.
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

