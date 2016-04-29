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


class GroupnetsGroupnetSubnetsSubnetPool(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        GroupnetsGroupnetSubnetsSubnetPool - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_zone': 'str',
            'aggregation_mode': 'str',
            'alloc_method': 'str',
            'description': 'str',
            'ifaces': 'list[GroupnetsGroupnetSubnetsSubnetPoolIface]',
            'name': 'str',
            'ranges': 'list[GroupnetsGroupnetSubnetsSubnetPoolRange]',
            'rebalance_policy': 'str',
            'sc_auto_unsuspend_delay': 'int',
            'sc_connect_policy': 'str',
            'sc_dns_zone': 'str',
            'sc_dns_zone_aliases': 'list[str]',
            'sc_failover_policy': 'str',
            'sc_subnet': 'str',
            'sc_ttl': 'int',
            'static_routes': 'list[GroupnetsGroupnetSubnetsSubnetPoolStaticRoute]'
        }

        self.attribute_map = {
            'access_zone': 'access_zone',
            'aggregation_mode': 'aggregation_mode',
            'alloc_method': 'alloc_method',
            'description': 'description',
            'ifaces': 'ifaces',
            'name': 'name',
            'ranges': 'ranges',
            'rebalance_policy': 'rebalance_policy',
            'sc_auto_unsuspend_delay': 'sc_auto_unsuspend_delay',
            'sc_connect_policy': 'sc_connect_policy',
            'sc_dns_zone': 'sc_dns_zone',
            'sc_dns_zone_aliases': 'sc_dns_zone_aliases',
            'sc_failover_policy': 'sc_failover_policy',
            'sc_subnet': 'sc_subnet',
            'sc_ttl': 'sc_ttl',
            'static_routes': 'static_routes'
        }

        self._access_zone = None
        self._aggregation_mode = None
        self._alloc_method = None
        self._description = None
        self._ifaces = None
        self._name = None
        self._ranges = None
        self._rebalance_policy = None
        self._sc_auto_unsuspend_delay = None
        self._sc_connect_policy = None
        self._sc_dns_zone = None
        self._sc_dns_zone_aliases = None
        self._sc_failover_policy = None
        self._sc_subnet = None
        self._sc_ttl = None
        self._static_routes = None

    @property
    def access_zone(self):
        """
        Gets the access_zone of this GroupnetsGroupnetSubnetsSubnetPool.
        Name of a valid access zone to map IP address pool to the zone.

        :return: The access_zone of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._access_zone

    @access_zone.setter
    def access_zone(self, access_zone):
        """
        Sets the access_zone of this GroupnetsGroupnetSubnetsSubnetPool.
        Name of a valid access zone to map IP address pool to the zone.

        :param access_zone: The access_zone of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        self._access_zone = access_zone

    @property
    def aggregation_mode(self):
        """
        Gets the aggregation_mode of this GroupnetsGroupnetSubnetsSubnetPool.
        OneFS supports the following NIC aggregation modes.

        :return: The aggregation_mode of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._aggregation_mode

    @aggregation_mode.setter
    def aggregation_mode(self, aggregation_mode):
        """
        Sets the aggregation_mode of this GroupnetsGroupnetSubnetsSubnetPool.
        OneFS supports the following NIC aggregation modes.

        :param aggregation_mode: The aggregation_mode of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        allowed_values = ["roundrobin", "failover", "lacp", "fec"]
        if aggregation_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_mode`, must be one of {0}"
                .format(allowed_values)
            )
        self._aggregation_mode = aggregation_mode

    @property
    def alloc_method(self):
        """
        Gets the alloc_method of this GroupnetsGroupnetSubnetsSubnetPool.
        Specifies how IP address allocation is done among pool members.

        :return: The alloc_method of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._alloc_method

    @alloc_method.setter
    def alloc_method(self, alloc_method):
        """
        Sets the alloc_method of this GroupnetsGroupnetSubnetsSubnetPool.
        Specifies how IP address allocation is done among pool members.

        :param alloc_method: The alloc_method of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        allowed_values = ["dynamic", "static"]
        if alloc_method not in allowed_values:
            raise ValueError(
                "Invalid value for `alloc_method`, must be one of {0}"
                .format(allowed_values)
            )
        self._alloc_method = alloc_method

    @property
    def description(self):
        """
        Gets the description of this GroupnetsGroupnetSubnetsSubnetPool.
        A description of the pool.

        :return: The description of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GroupnetsGroupnetSubnetsSubnetPool.
        A description of the pool.

        :param description: The description of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        self._description = description

    @property
    def ifaces(self):
        """
        Gets the ifaces of this GroupnetsGroupnetSubnetsSubnetPool.
        List of interface members in this pool.

        :return: The ifaces of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: list[GroupnetsGroupnetSubnetsSubnetPoolIface]
        """
        return self._ifaces

    @ifaces.setter
    def ifaces(self, ifaces):
        """
        Sets the ifaces of this GroupnetsGroupnetSubnetsSubnetPool.
        List of interface members in this pool.

        :param ifaces: The ifaces of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: list[GroupnetsGroupnetSubnetsSubnetPoolIface]
        """
        self._ifaces = ifaces

    @property
    def name(self):
        """
        Gets the name of this GroupnetsGroupnetSubnetsSubnetPool.
        The name of the pool. It must be unique throughout the given subnet.It's a required field with POST method.

        :return: The name of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupnetsGroupnetSubnetsSubnetPool.
        The name of the pool. It must be unique throughout the given subnet.It's a required field with POST method.

        :param name: The name of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        self._name = name

    @property
    def ranges(self):
        """
        Gets the ranges of this GroupnetsGroupnetSubnetsSubnetPool.
        List of IP address ranges in this pool.

        :return: The ranges of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: list[GroupnetsGroupnetSubnetsSubnetPoolRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """
        Sets the ranges of this GroupnetsGroupnetSubnetsSubnetPool.
        List of IP address ranges in this pool.

        :param ranges: The ranges of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: list[GroupnetsGroupnetSubnetsSubnetPoolRange]
        """
        self._ranges = ranges

    @property
    def rebalance_policy(self):
        """
        Gets the rebalance_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        Rebalance policy..

        :return: The rebalance_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._rebalance_policy

    @rebalance_policy.setter
    def rebalance_policy(self, rebalance_policy):
        """
        Sets the rebalance_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        Rebalance policy..

        :param rebalance_policy: The rebalance_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        allowed_values = ["auto", "manual"]
        if rebalance_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `rebalance_policy`, must be one of {0}"
                .format(allowed_values)
            )
        self._rebalance_policy = rebalance_policy

    @property
    def sc_auto_unsuspend_delay(self):
        """
        Gets the sc_auto_unsuspend_delay of this GroupnetsGroupnetSubnetsSubnetPool.
        Time delay in seconds before a node which has been                 automatically unsuspended becomes usable in SmartConnect                responses for pool zones.

        :return: The sc_auto_unsuspend_delay of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: int
        """
        return self._sc_auto_unsuspend_delay

    @sc_auto_unsuspend_delay.setter
    def sc_auto_unsuspend_delay(self, sc_auto_unsuspend_delay):
        """
        Sets the sc_auto_unsuspend_delay of this GroupnetsGroupnetSubnetsSubnetPool.
        Time delay in seconds before a node which has been                 automatically unsuspended becomes usable in SmartConnect                responses for pool zones.

        :param sc_auto_unsuspend_delay: The sc_auto_unsuspend_delay of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: int
        """
        self._sc_auto_unsuspend_delay = sc_auto_unsuspend_delay

    @property
    def sc_connect_policy(self):
        """
        Gets the sc_connect_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        SmartConnect client connection balancing policy.

        :return: The sc_connect_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._sc_connect_policy

    @sc_connect_policy.setter
    def sc_connect_policy(self, sc_connect_policy):
        """
        Sets the sc_connect_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        SmartConnect client connection balancing policy.

        :param sc_connect_policy: The sc_connect_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        allowed_values = ["round_robin", "conn_count", "throughput", "cpu_usage"]
        if sc_connect_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `sc_connect_policy`, must be one of {0}"
                .format(allowed_values)
            )
        self._sc_connect_policy = sc_connect_policy

    @property
    def sc_dns_zone(self):
        """
        Gets the sc_dns_zone of this GroupnetsGroupnetSubnetsSubnetPool.
        SmartConnect zone name for the pool.

        :return: The sc_dns_zone of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._sc_dns_zone

    @sc_dns_zone.setter
    def sc_dns_zone(self, sc_dns_zone):
        """
        Sets the sc_dns_zone of this GroupnetsGroupnetSubnetsSubnetPool.
        SmartConnect zone name for the pool.

        :param sc_dns_zone: The sc_dns_zone of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        self._sc_dns_zone = sc_dns_zone

    @property
    def sc_dns_zone_aliases(self):
        """
        Gets the sc_dns_zone_aliases of this GroupnetsGroupnetSubnetsSubnetPool.
        List of SmartConnect zone aliases (DNS names) to the pool.

        :return: The sc_dns_zone_aliases of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: list[str]
        """
        return self._sc_dns_zone_aliases

    @sc_dns_zone_aliases.setter
    def sc_dns_zone_aliases(self, sc_dns_zone_aliases):
        """
        Sets the sc_dns_zone_aliases of this GroupnetsGroupnetSubnetsSubnetPool.
        List of SmartConnect zone aliases (DNS names) to the pool.

        :param sc_dns_zone_aliases: The sc_dns_zone_aliases of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: list[str]
        """
        self._sc_dns_zone_aliases = sc_dns_zone_aliases

    @property
    def sc_failover_policy(self):
        """
        Gets the sc_failover_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        SmartConnect IP failover policy.

        :return: The sc_failover_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._sc_failover_policy

    @sc_failover_policy.setter
    def sc_failover_policy(self, sc_failover_policy):
        """
        Sets the sc_failover_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        SmartConnect IP failover policy.

        :param sc_failover_policy: The sc_failover_policy of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        allowed_values = ["round_robin", "conn_count", "throughput", "cpu_usage"]
        if sc_failover_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `sc_failover_policy`, must be one of {0}"
                .format(allowed_values)
            )
        self._sc_failover_policy = sc_failover_policy

    @property
    def sc_subnet(self):
        """
        Gets the sc_subnet of this GroupnetsGroupnetSubnetsSubnetPool.
        Name of SmartConnect service subnet for this pool.

        :return: The sc_subnet of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: str
        """
        return self._sc_subnet

    @sc_subnet.setter
    def sc_subnet(self, sc_subnet):
        """
        Sets the sc_subnet of this GroupnetsGroupnetSubnetsSubnetPool.
        Name of SmartConnect service subnet for this pool.

        :param sc_subnet: The sc_subnet of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: str
        """
        self._sc_subnet = sc_subnet

    @property
    def sc_ttl(self):
        """
        Gets the sc_ttl of this GroupnetsGroupnetSubnetsSubnetPool.
        Time to live value for SmartConnect DNS query responses in seconds.

        :return: The sc_ttl of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: int
        """
        return self._sc_ttl

    @sc_ttl.setter
    def sc_ttl(self, sc_ttl):
        """
        Sets the sc_ttl of this GroupnetsGroupnetSubnetsSubnetPool.
        Time to live value for SmartConnect DNS query responses in seconds.

        :param sc_ttl: The sc_ttl of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: int
        """
        self._sc_ttl = sc_ttl

    @property
    def static_routes(self):
        """
        Gets the static_routes of this GroupnetsGroupnetSubnetsSubnetPool.
        List of interface members in this pool.

        :return: The static_routes of this GroupnetsGroupnetSubnetsSubnetPool.
        :rtype: list[GroupnetsGroupnetSubnetsSubnetPoolStaticRoute]
        """
        return self._static_routes

    @static_routes.setter
    def static_routes(self, static_routes):
        """
        Sets the static_routes of this GroupnetsGroupnetSubnetsSubnetPool.
        List of interface members in this pool.

        :param static_routes: The static_routes of this GroupnetsGroupnetSubnetsSubnetPool.
        :type: list[GroupnetsGroupnetSubnetsSubnetPoolStaticRoute]
        """
        self._static_routes = static_routes

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

