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


class ProvidersNisNisItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProvidersNisNisItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'authentication': 'bool',
            'balance_servers': 'bool',
            'check_online_interval': 'int',
            'create_home_directory': 'bool',
            'enabled': 'bool',
            'enumerate_groups': 'bool',
            'enumerate_users': 'bool',
            'findable_groups': 'list[str]',
            'findable_users': 'list[str]',
            'group_domain': 'str',
            'home_directory_template': 'str',
            'hostname_lookup': 'bool',
            'id': 'str',
            'listable_groups': 'list[str]',
            'listable_users': 'list[str]',
            'login_shell': 'str',
            'name': 'str',
            'nis_domain': 'str',
            'normalize_groups': 'bool',
            'normalize_users': 'bool',
            'ntlm_support': 'str',
            'provider_domain': 'str',
            'request_timeout': 'int',
            'restrict_findable': 'bool',
            'restrict_listable': 'bool',
            'retry_time': 'int',
            'servers': 'list[str]',
            'status': 'str',
            'system': 'bool',
            'unfindable_groups': 'list[str]',
            'unfindable_users': 'list[str]',
            'unlistable_groups': 'list[str]',
            'unlistable_users': 'list[str]',
            'user_domain': 'str',
            'ypmatch_using_tcp': 'bool'
        }

        self.attribute_map = {
            'authentication': 'authentication',
            'balance_servers': 'balance_servers',
            'check_online_interval': 'check_online_interval',
            'create_home_directory': 'create_home_directory',
            'enabled': 'enabled',
            'enumerate_groups': 'enumerate_groups',
            'enumerate_users': 'enumerate_users',
            'findable_groups': 'findable_groups',
            'findable_users': 'findable_users',
            'group_domain': 'group_domain',
            'home_directory_template': 'home_directory_template',
            'hostname_lookup': 'hostname_lookup',
            'id': 'id',
            'listable_groups': 'listable_groups',
            'listable_users': 'listable_users',
            'login_shell': 'login_shell',
            'name': 'name',
            'nis_domain': 'nis_domain',
            'normalize_groups': 'normalize_groups',
            'normalize_users': 'normalize_users',
            'ntlm_support': 'ntlm_support',
            'provider_domain': 'provider_domain',
            'request_timeout': 'request_timeout',
            'restrict_findable': 'restrict_findable',
            'restrict_listable': 'restrict_listable',
            'retry_time': 'retry_time',
            'servers': 'servers',
            'status': 'status',
            'system': 'system',
            'unfindable_groups': 'unfindable_groups',
            'unfindable_users': 'unfindable_users',
            'unlistable_groups': 'unlistable_groups',
            'unlistable_users': 'unlistable_users',
            'user_domain': 'user_domain',
            'ypmatch_using_tcp': 'ypmatch_using_tcp'
        }

        self._authentication = None
        self._balance_servers = None
        self._check_online_interval = None
        self._create_home_directory = None
        self._enabled = None
        self._enumerate_groups = None
        self._enumerate_users = None
        self._findable_groups = None
        self._findable_users = None
        self._group_domain = None
        self._home_directory_template = None
        self._hostname_lookup = None
        self._id = None
        self._listable_groups = None
        self._listable_users = None
        self._login_shell = None
        self._name = None
        self._nis_domain = None
        self._normalize_groups = None
        self._normalize_users = None
        self._ntlm_support = None
        self._provider_domain = None
        self._request_timeout = None
        self._restrict_findable = None
        self._restrict_listable = None
        self._retry_time = None
        self._servers = None
        self._status = None
        self._system = None
        self._unfindable_groups = None
        self._unfindable_users = None
        self._unlistable_groups = None
        self._unlistable_users = None
        self._user_domain = None
        self._ypmatch_using_tcp = None

    @property
    def authentication(self):
        """
        Gets the authentication of this ProvidersNisNisItem.
        If true, enables authentication and identity management through the authentication provider.

        :return: The authentication of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """
        Sets the authentication of this ProvidersNisNisItem.
        If true, enables authentication and identity management through the authentication provider.

        :param authentication: The authentication of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._authentication = authentication

    @property
    def balance_servers(self):
        """
        Gets the balance_servers of this ProvidersNisNisItem.
        If true, connects the provider to a random server.

        :return: The balance_servers of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._balance_servers

    @balance_servers.setter
    def balance_servers(self, balance_servers):
        """
        Sets the balance_servers of this ProvidersNisNisItem.
        If true, connects the provider to a random server.

        :param balance_servers: The balance_servers of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._balance_servers = balance_servers

    @property
    def check_online_interval(self):
        """
        Gets the check_online_interval of this ProvidersNisNisItem.
        Specifies the time in seconds between provider online checks.

        :return: The check_online_interval of this ProvidersNisNisItem.
        :rtype: int
        """
        return self._check_online_interval

    @check_online_interval.setter
    def check_online_interval(self, check_online_interval):
        """
        Sets the check_online_interval of this ProvidersNisNisItem.
        Specifies the time in seconds between provider online checks.

        :param check_online_interval: The check_online_interval of this ProvidersNisNisItem.
        :type: int
        """
        
        self._check_online_interval = check_online_interval

    @property
    def create_home_directory(self):
        """
        Gets the create_home_directory of this ProvidersNisNisItem.
        Automatically creates the home directory on the first login.

        :return: The create_home_directory of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._create_home_directory

    @create_home_directory.setter
    def create_home_directory(self, create_home_directory):
        """
        Sets the create_home_directory of this ProvidersNisNisItem.
        Automatically creates the home directory on the first login.

        :param create_home_directory: The create_home_directory of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._create_home_directory = create_home_directory

    @property
    def enabled(self):
        """
        Gets the enabled of this ProvidersNisNisItem.
        If true, enables the NIS provider.

        :return: The enabled of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ProvidersNisNisItem.
        If true, enables the NIS provider.

        :param enabled: The enabled of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def enumerate_groups(self):
        """
        Gets the enumerate_groups of this ProvidersNisNisItem.
        If true, allows the provider to enumerate groups.

        :return: The enumerate_groups of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._enumerate_groups

    @enumerate_groups.setter
    def enumerate_groups(self, enumerate_groups):
        """
        Sets the enumerate_groups of this ProvidersNisNisItem.
        If true, allows the provider to enumerate groups.

        :param enumerate_groups: The enumerate_groups of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._enumerate_groups = enumerate_groups

    @property
    def enumerate_users(self):
        """
        Gets the enumerate_users of this ProvidersNisNisItem.
        If true, allows the provider to enumerate users.

        :return: The enumerate_users of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._enumerate_users

    @enumerate_users.setter
    def enumerate_users(self, enumerate_users):
        """
        Sets the enumerate_users of this ProvidersNisNisItem.
        If true, allows the provider to enumerate users.

        :param enumerate_users: The enumerate_users of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._enumerate_users = enumerate_users

    @property
    def findable_groups(self):
        """
        Gets the findable_groups of this ProvidersNisNisItem.
        Specifies the list of groups that can be resolved.

        :return: The findable_groups of this ProvidersNisNisItem.
        :rtype: list[str]
        """
        return self._findable_groups

    @findable_groups.setter
    def findable_groups(self, findable_groups):
        """
        Sets the findable_groups of this ProvidersNisNisItem.
        Specifies the list of groups that can be resolved.

        :param findable_groups: The findable_groups of this ProvidersNisNisItem.
        :type: list[str]
        """
        
        self._findable_groups = findable_groups

    @property
    def findable_users(self):
        """
        Gets the findable_users of this ProvidersNisNisItem.
        Specifies the list of users that can be resolved.

        :return: The findable_users of this ProvidersNisNisItem.
        :rtype: list[str]
        """
        return self._findable_users

    @findable_users.setter
    def findable_users(self, findable_users):
        """
        Sets the findable_users of this ProvidersNisNisItem.
        Specifies the list of users that can be resolved.

        :param findable_users: The findable_users of this ProvidersNisNisItem.
        :type: list[str]
        """
        
        self._findable_users = findable_users

    @property
    def group_domain(self):
        """
        Gets the group_domain of this ProvidersNisNisItem.
        Specifies the domain for this provider through which groups are qualified.

        :return: The group_domain of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._group_domain

    @group_domain.setter
    def group_domain(self, group_domain):
        """
        Sets the group_domain of this ProvidersNisNisItem.
        Specifies the domain for this provider through which groups are qualified.

        :param group_domain: The group_domain of this ProvidersNisNisItem.
        :type: str
        """
        
        self._group_domain = group_domain

    @property
    def home_directory_template(self):
        """
        Gets the home_directory_template of this ProvidersNisNisItem.
        Specifies the path to the home directory template.

        :return: The home_directory_template of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._home_directory_template

    @home_directory_template.setter
    def home_directory_template(self, home_directory_template):
        """
        Sets the home_directory_template of this ProvidersNisNisItem.
        Specifies the path to the home directory template.

        :param home_directory_template: The home_directory_template of this ProvidersNisNisItem.
        :type: str
        """
        
        self._home_directory_template = home_directory_template

    @property
    def hostname_lookup(self):
        """
        Gets the hostname_lookup of this ProvidersNisNisItem.
        If true, enables host name look ups.

        :return: The hostname_lookup of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._hostname_lookup

    @hostname_lookup.setter
    def hostname_lookup(self, hostname_lookup):
        """
        Sets the hostname_lookup of this ProvidersNisNisItem.
        If true, enables host name look ups.

        :param hostname_lookup: The hostname_lookup of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._hostname_lookup = hostname_lookup

    @property
    def id(self):
        """
        Gets the id of this ProvidersNisNisItem.
        Specifies the NIS provider ID.

        :return: The id of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProvidersNisNisItem.
        Specifies the NIS provider ID.

        :param id: The id of this ProvidersNisNisItem.
        :type: str
        """
        
        self._id = id

    @property
    def listable_groups(self):
        """
        Gets the listable_groups of this ProvidersNisNisItem.
        Specifies the groups that can be viewed in the provider.

        :return: The listable_groups of this ProvidersNisNisItem.
        :rtype: list[str]
        """
        return self._listable_groups

    @listable_groups.setter
    def listable_groups(self, listable_groups):
        """
        Sets the listable_groups of this ProvidersNisNisItem.
        Specifies the groups that can be viewed in the provider.

        :param listable_groups: The listable_groups of this ProvidersNisNisItem.
        :type: list[str]
        """
        
        self._listable_groups = listable_groups

    @property
    def listable_users(self):
        """
        Gets the listable_users of this ProvidersNisNisItem.
        Specifies the users that can be viewed in the provider.

        :return: The listable_users of this ProvidersNisNisItem.
        :rtype: list[str]
        """
        return self._listable_users

    @listable_users.setter
    def listable_users(self, listable_users):
        """
        Sets the listable_users of this ProvidersNisNisItem.
        Specifies the users that can be viewed in the provider.

        :param listable_users: The listable_users of this ProvidersNisNisItem.
        :type: list[str]
        """
        
        self._listable_users = listable_users

    @property
    def login_shell(self):
        """
        Gets the login_shell of this ProvidersNisNisItem.
        Specifies the login shell path.

        :return: The login_shell of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._login_shell

    @login_shell.setter
    def login_shell(self, login_shell):
        """
        Sets the login_shell of this ProvidersNisNisItem.
        Specifies the login shell path.

        :param login_shell: The login_shell of this ProvidersNisNisItem.
        :type: str
        """
        
        self._login_shell = login_shell

    @property
    def name(self):
        """
        Gets the name of this ProvidersNisNisItem.
        Specifies the NIS provider name.

        :return: The name of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProvidersNisNisItem.
        Specifies the NIS provider name.

        :param name: The name of this ProvidersNisNisItem.
        :type: str
        """
        
        self._name = name

    @property
    def nis_domain(self):
        """
        Gets the nis_domain of this ProvidersNisNisItem.
        Specifies the NIS domain name.

        :return: The nis_domain of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._nis_domain

    @nis_domain.setter
    def nis_domain(self, nis_domain):
        """
        Sets the nis_domain of this ProvidersNisNisItem.
        Specifies the NIS domain name.

        :param nis_domain: The nis_domain of this ProvidersNisNisItem.
        :type: str
        """
        
        self._nis_domain = nis_domain

    @property
    def normalize_groups(self):
        """
        Gets the normalize_groups of this ProvidersNisNisItem.
        Normalizes group names to lowercase before look up.

        :return: The normalize_groups of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._normalize_groups

    @normalize_groups.setter
    def normalize_groups(self, normalize_groups):
        """
        Sets the normalize_groups of this ProvidersNisNisItem.
        Normalizes group names to lowercase before look up.

        :param normalize_groups: The normalize_groups of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._normalize_groups = normalize_groups

    @property
    def normalize_users(self):
        """
        Gets the normalize_users of this ProvidersNisNisItem.
        Normalizes user names to lowercase before look up.

        :return: The normalize_users of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._normalize_users

    @normalize_users.setter
    def normalize_users(self, normalize_users):
        """
        Sets the normalize_users of this ProvidersNisNisItem.
        Normalizes user names to lowercase before look up.

        :param normalize_users: The normalize_users of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._normalize_users = normalize_users

    @property
    def ntlm_support(self):
        """
        Gets the ntlm_support of this ProvidersNisNisItem.
        Specifies which NTLM versions to support for users with NTLM-compatible credentials.

        :return: The ntlm_support of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._ntlm_support

    @ntlm_support.setter
    def ntlm_support(self, ntlm_support):
        """
        Sets the ntlm_support of this ProvidersNisNisItem.
        Specifies which NTLM versions to support for users with NTLM-compatible credentials.

        :param ntlm_support: The ntlm_support of this ProvidersNisNisItem.
        :type: str
        """
        allowed_values = ["all", "v2only", "none"]
        if ntlm_support not in allowed_values:
            raise ValueError(
                "Invalid value for `ntlm_support`, must be one of {0}"
                .format(allowed_values)
            )

        self._ntlm_support = ntlm_support

    @property
    def provider_domain(self):
        """
        Gets the provider_domain of this ProvidersNisNisItem.
        Specifies the domain for the provider.

        :return: The provider_domain of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._provider_domain

    @provider_domain.setter
    def provider_domain(self, provider_domain):
        """
        Sets the provider_domain of this ProvidersNisNisItem.
        Specifies the domain for the provider.

        :param provider_domain: The provider_domain of this ProvidersNisNisItem.
        :type: str
        """
        
        self._provider_domain = provider_domain

    @property
    def request_timeout(self):
        """
        Gets the request_timeout of this ProvidersNisNisItem.
        Specifies the request timeout interval in seconds.

        :return: The request_timeout of this ProvidersNisNisItem.
        :rtype: int
        """
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, request_timeout):
        """
        Sets the request_timeout of this ProvidersNisNisItem.
        Specifies the request timeout interval in seconds.

        :param request_timeout: The request_timeout of this ProvidersNisNisItem.
        :type: int
        """
        
        self._request_timeout = request_timeout

    @property
    def restrict_findable(self):
        """
        Gets the restrict_findable of this ProvidersNisNisItem.
        If true, checks the provider for filtered lists of findable and unfindable users and groups.

        :return: The restrict_findable of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._restrict_findable

    @restrict_findable.setter
    def restrict_findable(self, restrict_findable):
        """
        Sets the restrict_findable of this ProvidersNisNisItem.
        If true, checks the provider for filtered lists of findable and unfindable users and groups.

        :param restrict_findable: The restrict_findable of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._restrict_findable = restrict_findable

    @property
    def restrict_listable(self):
        """
        Gets the restrict_listable of this ProvidersNisNisItem.
        If true, checks the provider for filtered lists of listable and unlistable users and groups.

        :return: The restrict_listable of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._restrict_listable

    @restrict_listable.setter
    def restrict_listable(self, restrict_listable):
        """
        Sets the restrict_listable of this ProvidersNisNisItem.
        If true, checks the provider for filtered lists of listable and unlistable users and groups.

        :param restrict_listable: The restrict_listable of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._restrict_listable = restrict_listable

    @property
    def retry_time(self):
        """
        Gets the retry_time of this ProvidersNisNisItem.
        Specifies the timeout period in seconds after which a request will be retried.

        :return: The retry_time of this ProvidersNisNisItem.
        :rtype: int
        """
        return self._retry_time

    @retry_time.setter
    def retry_time(self, retry_time):
        """
        Sets the retry_time of this ProvidersNisNisItem.
        Specifies the timeout period in seconds after which a request will be retried.

        :param retry_time: The retry_time of this ProvidersNisNisItem.
        :type: int
        """
        
        self._retry_time = retry_time

    @property
    def servers(self):
        """
        Gets the servers of this ProvidersNisNisItem.
        Adds an NIS server for this provider.

        :return: The servers of this ProvidersNisNisItem.
        :rtype: list[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """
        Sets the servers of this ProvidersNisNisItem.
        Adds an NIS server for this provider.

        :param servers: The servers of this ProvidersNisNisItem.
        :type: list[str]
        """
        
        self._servers = servers

    @property
    def status(self):
        """
        Gets the status of this ProvidersNisNisItem.
        Specifies the status of the provider.

        :return: The status of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ProvidersNisNisItem.
        Specifies the status of the provider.

        :param status: The status of this ProvidersNisNisItem.
        :type: str
        """
        
        self._status = status

    @property
    def system(self):
        """
        Gets the system of this ProvidersNisNisItem.
        If true, indicates that this provider instance was created by OneFS and cannot be removed.

        :return: The system of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this ProvidersNisNisItem.
        If true, indicates that this provider instance was created by OneFS and cannot be removed.

        :param system: The system of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._system = system

    @property
    def unfindable_groups(self):
        """
        Gets the unfindable_groups of this ProvidersNisNisItem.
        Specifies groups that cannot be resolved by the provider.

        :return: The unfindable_groups of this ProvidersNisNisItem.
        :rtype: list[str]
        """
        return self._unfindable_groups

    @unfindable_groups.setter
    def unfindable_groups(self, unfindable_groups):
        """
        Sets the unfindable_groups of this ProvidersNisNisItem.
        Specifies groups that cannot be resolved by the provider.

        :param unfindable_groups: The unfindable_groups of this ProvidersNisNisItem.
        :type: list[str]
        """
        
        self._unfindable_groups = unfindable_groups

    @property
    def unfindable_users(self):
        """
        Gets the unfindable_users of this ProvidersNisNisItem.
        Specifies users that cannot be resolved by the provider.

        :return: The unfindable_users of this ProvidersNisNisItem.
        :rtype: list[str]
        """
        return self._unfindable_users

    @unfindable_users.setter
    def unfindable_users(self, unfindable_users):
        """
        Sets the unfindable_users of this ProvidersNisNisItem.
        Specifies users that cannot be resolved by the provider.

        :param unfindable_users: The unfindable_users of this ProvidersNisNisItem.
        :type: list[str]
        """
        
        self._unfindable_users = unfindable_users

    @property
    def unlistable_groups(self):
        """
        Gets the unlistable_groups of this ProvidersNisNisItem.
        Specifies a group that cannot be listed by the provider.

        :return: The unlistable_groups of this ProvidersNisNisItem.
        :rtype: list[str]
        """
        return self._unlistable_groups

    @unlistable_groups.setter
    def unlistable_groups(self, unlistable_groups):
        """
        Sets the unlistable_groups of this ProvidersNisNisItem.
        Specifies a group that cannot be listed by the provider.

        :param unlistable_groups: The unlistable_groups of this ProvidersNisNisItem.
        :type: list[str]
        """
        
        self._unlistable_groups = unlistable_groups

    @property
    def unlistable_users(self):
        """
        Gets the unlistable_users of this ProvidersNisNisItem.
        Specifies a user that cannot be listed by the provider.

        :return: The unlistable_users of this ProvidersNisNisItem.
        :rtype: list[str]
        """
        return self._unlistable_users

    @unlistable_users.setter
    def unlistable_users(self, unlistable_users):
        """
        Sets the unlistable_users of this ProvidersNisNisItem.
        Specifies a user that cannot be listed by the provider.

        :param unlistable_users: The unlistable_users of this ProvidersNisNisItem.
        :type: list[str]
        """
        
        self._unlistable_users = unlistable_users

    @property
    def user_domain(self):
        """
        Gets the user_domain of this ProvidersNisNisItem.
        Specifies the domain for this provider through which users are qualified.

        :return: The user_domain of this ProvidersNisNisItem.
        :rtype: str
        """
        return self._user_domain

    @user_domain.setter
    def user_domain(self, user_domain):
        """
        Sets the user_domain of this ProvidersNisNisItem.
        Specifies the domain for this provider through which users are qualified.

        :param user_domain: The user_domain of this ProvidersNisNisItem.
        :type: str
        """
        
        self._user_domain = user_domain

    @property
    def ypmatch_using_tcp(self):
        """
        Gets the ypmatch_using_tcp of this ProvidersNisNisItem.
        If true, specifies TCP for YP Match operations.

        :return: The ypmatch_using_tcp of this ProvidersNisNisItem.
        :rtype: bool
        """
        return self._ypmatch_using_tcp

    @ypmatch_using_tcp.setter
    def ypmatch_using_tcp(self, ypmatch_using_tcp):
        """
        Sets the ypmatch_using_tcp of this ProvidersNisNisItem.
        If true, specifies TCP for YP Match operations.

        :param ypmatch_using_tcp: The ypmatch_using_tcp of this ProvidersNisNisItem.
        :type: bool
        """
        
        self._ypmatch_using_tcp = ypmatch_using_tcp

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

