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


class ProvidersNisItem(object):
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
        'groupnet': 'str',
        'home_directory_template': 'str',
        'hostname_lookup': 'bool',
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
        'unfindable_groups': 'list[str]',
        'unfindable_users': 'list[str]',
        'unlistable_groups': 'list[str]',
        'unlistable_users': 'list[str]',
        'user_domain': 'str',
        'ypmatch_using_tcp': 'bool'
    }

    attribute_map = {
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
        'groupnet': 'groupnet',
        'home_directory_template': 'home_directory_template',
        'hostname_lookup': 'hostname_lookup',
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
        'unfindable_groups': 'unfindable_groups',
        'unfindable_users': 'unfindable_users',
        'unlistable_groups': 'unlistable_groups',
        'unlistable_users': 'unlistable_users',
        'user_domain': 'user_domain',
        'ypmatch_using_tcp': 'ypmatch_using_tcp'
    }

    def __init__(self, authentication=None, balance_servers=None, check_online_interval=None, create_home_directory=None, enabled=None, enumerate_groups=None, enumerate_users=None, findable_groups=None, findable_users=None, group_domain=None, groupnet=None, home_directory_template=None, hostname_lookup=None, listable_groups=None, listable_users=None, login_shell=None, name=None, nis_domain=None, normalize_groups=None, normalize_users=None, ntlm_support=None, provider_domain=None, request_timeout=None, restrict_findable=None, restrict_listable=None, retry_time=None, servers=None, unfindable_groups=None, unfindable_users=None, unlistable_groups=None, unlistable_users=None, user_domain=None, ypmatch_using_tcp=None):  # noqa: E501
        """ProvidersNisItem - a model defined in Swagger"""  # noqa: E501

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
        self._groupnet = None
        self._home_directory_template = None
        self._hostname_lookup = None
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
        self._unfindable_groups = None
        self._unfindable_users = None
        self._unlistable_groups = None
        self._unlistable_users = None
        self._user_domain = None
        self._ypmatch_using_tcp = None
        self.discriminator = None

        if authentication is not None:
            self.authentication = authentication
        if balance_servers is not None:
            self.balance_servers = balance_servers
        if check_online_interval is not None:
            self.check_online_interval = check_online_interval
        if create_home_directory is not None:
            self.create_home_directory = create_home_directory
        if enabled is not None:
            self.enabled = enabled
        if enumerate_groups is not None:
            self.enumerate_groups = enumerate_groups
        if enumerate_users is not None:
            self.enumerate_users = enumerate_users
        if findable_groups is not None:
            self.findable_groups = findable_groups
        if findable_users is not None:
            self.findable_users = findable_users
        if group_domain is not None:
            self.group_domain = group_domain
        if groupnet is not None:
            self.groupnet = groupnet
        if home_directory_template is not None:
            self.home_directory_template = home_directory_template
        if hostname_lookup is not None:
            self.hostname_lookup = hostname_lookup
        if listable_groups is not None:
            self.listable_groups = listable_groups
        if listable_users is not None:
            self.listable_users = listable_users
        if login_shell is not None:
            self.login_shell = login_shell
        self.name = name
        self.nis_domain = nis_domain
        if normalize_groups is not None:
            self.normalize_groups = normalize_groups
        if normalize_users is not None:
            self.normalize_users = normalize_users
        if ntlm_support is not None:
            self.ntlm_support = ntlm_support
        if provider_domain is not None:
            self.provider_domain = provider_domain
        if request_timeout is not None:
            self.request_timeout = request_timeout
        if restrict_findable is not None:
            self.restrict_findable = restrict_findable
        if restrict_listable is not None:
            self.restrict_listable = restrict_listable
        if retry_time is not None:
            self.retry_time = retry_time
        self.servers = servers
        if unfindable_groups is not None:
            self.unfindable_groups = unfindable_groups
        if unfindable_users is not None:
            self.unfindable_users = unfindable_users
        if unlistable_groups is not None:
            self.unlistable_groups = unlistable_groups
        if unlistable_users is not None:
            self.unlistable_users = unlistable_users
        if user_domain is not None:
            self.user_domain = user_domain
        if ypmatch_using_tcp is not None:
            self.ypmatch_using_tcp = ypmatch_using_tcp

    @property
    def authentication(self):
        """Gets the authentication of this ProvidersNisItem.  # noqa: E501

        If true, enables authentication and identity management through the authentication provider.  # noqa: E501

        :return: The authentication of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this ProvidersNisItem.

        If true, enables authentication and identity management through the authentication provider.  # noqa: E501

        :param authentication: The authentication of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._authentication = authentication

    @property
    def balance_servers(self):
        """Gets the balance_servers of this ProvidersNisItem.  # noqa: E501

        If true, connects the provider to a random server.  # noqa: E501

        :return: The balance_servers of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._balance_servers

    @balance_servers.setter
    def balance_servers(self, balance_servers):
        """Sets the balance_servers of this ProvidersNisItem.

        If true, connects the provider to a random server.  # noqa: E501

        :param balance_servers: The balance_servers of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._balance_servers = balance_servers

    @property
    def check_online_interval(self):
        """Gets the check_online_interval of this ProvidersNisItem.  # noqa: E501

        Specifies the time in seconds between provider online checks.  # noqa: E501

        :return: The check_online_interval of this ProvidersNisItem.  # noqa: E501
        :rtype: int
        """
        return self._check_online_interval

    @check_online_interval.setter
    def check_online_interval(self, check_online_interval):
        """Sets the check_online_interval of this ProvidersNisItem.

        Specifies the time in seconds between provider online checks.  # noqa: E501

        :param check_online_interval: The check_online_interval of this ProvidersNisItem.  # noqa: E501
        :type: int
        """
        if check_online_interval is not None and check_online_interval > 3600:  # noqa: E501
            raise ValueError("Invalid value for `check_online_interval`, must be a value less than or equal to `3600`")  # noqa: E501
        if check_online_interval is not None and check_online_interval < 0:  # noqa: E501
            raise ValueError("Invalid value for `check_online_interval`, must be a value greater than or equal to `0`")  # noqa: E501

        self._check_online_interval = check_online_interval

    @property
    def create_home_directory(self):
        """Gets the create_home_directory of this ProvidersNisItem.  # noqa: E501

        Automatically creates the home directory on the first login.  # noqa: E501

        :return: The create_home_directory of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._create_home_directory

    @create_home_directory.setter
    def create_home_directory(self, create_home_directory):
        """Sets the create_home_directory of this ProvidersNisItem.

        Automatically creates the home directory on the first login.  # noqa: E501

        :param create_home_directory: The create_home_directory of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._create_home_directory = create_home_directory

    @property
    def enabled(self):
        """Gets the enabled of this ProvidersNisItem.  # noqa: E501

        If true, enables the NIS provider.  # noqa: E501

        :return: The enabled of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ProvidersNisItem.

        If true, enables the NIS provider.  # noqa: E501

        :param enabled: The enabled of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def enumerate_groups(self):
        """Gets the enumerate_groups of this ProvidersNisItem.  # noqa: E501

        If true, allows the provider to enumerate groups.  # noqa: E501

        :return: The enumerate_groups of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._enumerate_groups

    @enumerate_groups.setter
    def enumerate_groups(self, enumerate_groups):
        """Sets the enumerate_groups of this ProvidersNisItem.

        If true, allows the provider to enumerate groups.  # noqa: E501

        :param enumerate_groups: The enumerate_groups of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._enumerate_groups = enumerate_groups

    @property
    def enumerate_users(self):
        """Gets the enumerate_users of this ProvidersNisItem.  # noqa: E501

        If true, allows the provider to enumerate users.  # noqa: E501

        :return: The enumerate_users of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._enumerate_users

    @enumerate_users.setter
    def enumerate_users(self, enumerate_users):
        """Sets the enumerate_users of this ProvidersNisItem.

        If true, allows the provider to enumerate users.  # noqa: E501

        :param enumerate_users: The enumerate_users of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._enumerate_users = enumerate_users

    @property
    def findable_groups(self):
        """Gets the findable_groups of this ProvidersNisItem.  # noqa: E501

        Specifies the list of groups that can be resolved.  # noqa: E501

        :return: The findable_groups of this ProvidersNisItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._findable_groups

    @findable_groups.setter
    def findable_groups(self, findable_groups):
        """Sets the findable_groups of this ProvidersNisItem.

        Specifies the list of groups that can be resolved.  # noqa: E501

        :param findable_groups: The findable_groups of this ProvidersNisItem.  # noqa: E501
        :type: list[str]
        """

        self._findable_groups = findable_groups

    @property
    def findable_users(self):
        """Gets the findable_users of this ProvidersNisItem.  # noqa: E501

        Specifies the list of users that can be resolved.  # noqa: E501

        :return: The findable_users of this ProvidersNisItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._findable_users

    @findable_users.setter
    def findable_users(self, findable_users):
        """Sets the findable_users of this ProvidersNisItem.

        Specifies the list of users that can be resolved.  # noqa: E501

        :param findable_users: The findable_users of this ProvidersNisItem.  # noqa: E501
        :type: list[str]
        """

        self._findable_users = findable_users

    @property
    def group_domain(self):
        """Gets the group_domain of this ProvidersNisItem.  # noqa: E501

        Specifies the domain for this provider through which groups are qualified.  # noqa: E501

        :return: The group_domain of this ProvidersNisItem.  # noqa: E501
        :rtype: str
        """
        return self._group_domain

    @group_domain.setter
    def group_domain(self, group_domain):
        """Sets the group_domain of this ProvidersNisItem.

        Specifies the domain for this provider through which groups are qualified.  # noqa: E501

        :param group_domain: The group_domain of this ProvidersNisItem.  # noqa: E501
        :type: str
        """
        if group_domain is not None and len(group_domain) > 255:
            raise ValueError("Invalid value for `group_domain`, length must be less than or equal to `255`")  # noqa: E501
        if group_domain is not None and len(group_domain) < 0:
            raise ValueError("Invalid value for `group_domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._group_domain = group_domain

    @property
    def groupnet(self):
        """Gets the groupnet of this ProvidersNisItem.  # noqa: E501

        Groupnet identifier.  # noqa: E501

        :return: The groupnet of this ProvidersNisItem.  # noqa: E501
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """Sets the groupnet of this ProvidersNisItem.

        Groupnet identifier.  # noqa: E501

        :param groupnet: The groupnet of this ProvidersNisItem.  # noqa: E501
        :type: str
        """
        if groupnet is not None and len(groupnet) > 255:
            raise ValueError("Invalid value for `groupnet`, length must be less than or equal to `255`")  # noqa: E501
        if groupnet is not None and len(groupnet) < 0:
            raise ValueError("Invalid value for `groupnet`, length must be greater than or equal to `0`")  # noqa: E501

        self._groupnet = groupnet

    @property
    def home_directory_template(self):
        """Gets the home_directory_template of this ProvidersNisItem.  # noqa: E501

        Specifies the path to the home directory template.  # noqa: E501

        :return: The home_directory_template of this ProvidersNisItem.  # noqa: E501
        :rtype: str
        """
        return self._home_directory_template

    @home_directory_template.setter
    def home_directory_template(self, home_directory_template):
        """Sets the home_directory_template of this ProvidersNisItem.

        Specifies the path to the home directory template.  # noqa: E501

        :param home_directory_template: The home_directory_template of this ProvidersNisItem.  # noqa: E501
        :type: str
        """
        if home_directory_template is not None and len(home_directory_template) > 4096:
            raise ValueError("Invalid value for `home_directory_template`, length must be less than or equal to `4096`")  # noqa: E501
        if home_directory_template is not None and len(home_directory_template) < 0:
            raise ValueError("Invalid value for `home_directory_template`, length must be greater than or equal to `0`")  # noqa: E501

        self._home_directory_template = home_directory_template

    @property
    def hostname_lookup(self):
        """Gets the hostname_lookup of this ProvidersNisItem.  # noqa: E501

        If true, enables host name look ups.  # noqa: E501

        :return: The hostname_lookup of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._hostname_lookup

    @hostname_lookup.setter
    def hostname_lookup(self, hostname_lookup):
        """Sets the hostname_lookup of this ProvidersNisItem.

        If true, enables host name look ups.  # noqa: E501

        :param hostname_lookup: The hostname_lookup of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._hostname_lookup = hostname_lookup

    @property
    def listable_groups(self):
        """Gets the listable_groups of this ProvidersNisItem.  # noqa: E501

        Specifies the groups that can be viewed in the provider.  # noqa: E501

        :return: The listable_groups of this ProvidersNisItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._listable_groups

    @listable_groups.setter
    def listable_groups(self, listable_groups):
        """Sets the listable_groups of this ProvidersNisItem.

        Specifies the groups that can be viewed in the provider.  # noqa: E501

        :param listable_groups: The listable_groups of this ProvidersNisItem.  # noqa: E501
        :type: list[str]
        """

        self._listable_groups = listable_groups

    @property
    def listable_users(self):
        """Gets the listable_users of this ProvidersNisItem.  # noqa: E501

        Specifies the users that can be viewed in the provider.  # noqa: E501

        :return: The listable_users of this ProvidersNisItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._listable_users

    @listable_users.setter
    def listable_users(self, listable_users):
        """Sets the listable_users of this ProvidersNisItem.

        Specifies the users that can be viewed in the provider.  # noqa: E501

        :param listable_users: The listable_users of this ProvidersNisItem.  # noqa: E501
        :type: list[str]
        """

        self._listable_users = listable_users

    @property
    def login_shell(self):
        """Gets the login_shell of this ProvidersNisItem.  # noqa: E501

        Specifies the login shell path.  # noqa: E501

        :return: The login_shell of this ProvidersNisItem.  # noqa: E501
        :rtype: str
        """
        return self._login_shell

    @login_shell.setter
    def login_shell(self, login_shell):
        """Sets the login_shell of this ProvidersNisItem.

        Specifies the login shell path.  # noqa: E501

        :param login_shell: The login_shell of this ProvidersNisItem.  # noqa: E501
        :type: str
        """
        if login_shell is not None and len(login_shell) > 4096:
            raise ValueError("Invalid value for `login_shell`, length must be less than or equal to `4096`")  # noqa: E501
        if login_shell is not None and len(login_shell) < 0:
            raise ValueError("Invalid value for `login_shell`, length must be greater than or equal to `0`")  # noqa: E501

        self._login_shell = login_shell

    @property
    def name(self):
        """Gets the name of this ProvidersNisItem.  # noqa: E501

        Specifies the NIS provider name.  # noqa: E501

        :return: The name of this ProvidersNisItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvidersNisItem.

        Specifies the NIS provider name.  # noqa: E501

        :param name: The name of this ProvidersNisItem.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def nis_domain(self):
        """Gets the nis_domain of this ProvidersNisItem.  # noqa: E501

        Specifies the NIS domain name.  # noqa: E501

        :return: The nis_domain of this ProvidersNisItem.  # noqa: E501
        :rtype: str
        """
        return self._nis_domain

    @nis_domain.setter
    def nis_domain(self, nis_domain):
        """Sets the nis_domain of this ProvidersNisItem.

        Specifies the NIS domain name.  # noqa: E501

        :param nis_domain: The nis_domain of this ProvidersNisItem.  # noqa: E501
        :type: str
        """
        if nis_domain is None:
            raise ValueError("Invalid value for `nis_domain`, must not be `None`")  # noqa: E501
        if nis_domain is not None and len(nis_domain) > 255:
            raise ValueError("Invalid value for `nis_domain`, length must be less than or equal to `255`")  # noqa: E501
        if nis_domain is not None and len(nis_domain) < 0:
            raise ValueError("Invalid value for `nis_domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._nis_domain = nis_domain

    @property
    def normalize_groups(self):
        """Gets the normalize_groups of this ProvidersNisItem.  # noqa: E501

        Normalizes group names to lowercase before look up.  # noqa: E501

        :return: The normalize_groups of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._normalize_groups

    @normalize_groups.setter
    def normalize_groups(self, normalize_groups):
        """Sets the normalize_groups of this ProvidersNisItem.

        Normalizes group names to lowercase before look up.  # noqa: E501

        :param normalize_groups: The normalize_groups of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._normalize_groups = normalize_groups

    @property
    def normalize_users(self):
        """Gets the normalize_users of this ProvidersNisItem.  # noqa: E501

        Normalizes user names to lowercase before look up.  # noqa: E501

        :return: The normalize_users of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._normalize_users

    @normalize_users.setter
    def normalize_users(self, normalize_users):
        """Sets the normalize_users of this ProvidersNisItem.

        Normalizes user names to lowercase before look up.  # noqa: E501

        :param normalize_users: The normalize_users of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._normalize_users = normalize_users

    @property
    def ntlm_support(self):
        """Gets the ntlm_support of this ProvidersNisItem.  # noqa: E501

        Specifies which NTLM versions to support for users with NTLM-compatible credentials.  # noqa: E501

        :return: The ntlm_support of this ProvidersNisItem.  # noqa: E501
        :rtype: str
        """
        return self._ntlm_support

    @ntlm_support.setter
    def ntlm_support(self, ntlm_support):
        """Sets the ntlm_support of this ProvidersNisItem.

        Specifies which NTLM versions to support for users with NTLM-compatible credentials.  # noqa: E501

        :param ntlm_support: The ntlm_support of this ProvidersNisItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["all", "v2only", "none"]  # noqa: E501
        if ntlm_support not in allowed_values:
            raise ValueError(
                "Invalid value for `ntlm_support` ({0}), must be one of {1}"  # noqa: E501
                .format(ntlm_support, allowed_values)
            )

        self._ntlm_support = ntlm_support

    @property
    def provider_domain(self):
        """Gets the provider_domain of this ProvidersNisItem.  # noqa: E501

        Specifies the domain for the provider.  # noqa: E501

        :return: The provider_domain of this ProvidersNisItem.  # noqa: E501
        :rtype: str
        """
        return self._provider_domain

    @provider_domain.setter
    def provider_domain(self, provider_domain):
        """Sets the provider_domain of this ProvidersNisItem.

        Specifies the domain for the provider.  # noqa: E501

        :param provider_domain: The provider_domain of this ProvidersNisItem.  # noqa: E501
        :type: str
        """
        if provider_domain is not None and len(provider_domain) > 255:
            raise ValueError("Invalid value for `provider_domain`, length must be less than or equal to `255`")  # noqa: E501
        if provider_domain is not None and len(provider_domain) < 0:
            raise ValueError("Invalid value for `provider_domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._provider_domain = provider_domain

    @property
    def request_timeout(self):
        """Gets the request_timeout of this ProvidersNisItem.  # noqa: E501

        Specifies the request timeout interval in seconds.  # noqa: E501

        :return: The request_timeout of this ProvidersNisItem.  # noqa: E501
        :rtype: int
        """
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, request_timeout):
        """Sets the request_timeout of this ProvidersNisItem.

        Specifies the request timeout interval in seconds.  # noqa: E501

        :param request_timeout: The request_timeout of this ProvidersNisItem.  # noqa: E501
        :type: int
        """
        if request_timeout is not None and request_timeout > 3600:  # noqa: E501
            raise ValueError("Invalid value for `request_timeout`, must be a value less than or equal to `3600`")  # noqa: E501
        if request_timeout is not None and request_timeout < 0:  # noqa: E501
            raise ValueError("Invalid value for `request_timeout`, must be a value greater than or equal to `0`")  # noqa: E501

        self._request_timeout = request_timeout

    @property
    def restrict_findable(self):
        """Gets the restrict_findable of this ProvidersNisItem.  # noqa: E501

        If true, checks the provider for filtered lists of findable and unfindable users and groups.  # noqa: E501

        :return: The restrict_findable of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_findable

    @restrict_findable.setter
    def restrict_findable(self, restrict_findable):
        """Sets the restrict_findable of this ProvidersNisItem.

        If true, checks the provider for filtered lists of findable and unfindable users and groups.  # noqa: E501

        :param restrict_findable: The restrict_findable of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._restrict_findable = restrict_findable

    @property
    def restrict_listable(self):
        """Gets the restrict_listable of this ProvidersNisItem.  # noqa: E501

        If true, checks the provider for filtered lists of listable and unlistable users and groups.  # noqa: E501

        :return: The restrict_listable of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_listable

    @restrict_listable.setter
    def restrict_listable(self, restrict_listable):
        """Sets the restrict_listable of this ProvidersNisItem.

        If true, checks the provider for filtered lists of listable and unlistable users and groups.  # noqa: E501

        :param restrict_listable: The restrict_listable of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._restrict_listable = restrict_listable

    @property
    def retry_time(self):
        """Gets the retry_time of this ProvidersNisItem.  # noqa: E501

        Specifies the timeout period in seconds after which a request will be retried.  # noqa: E501

        :return: The retry_time of this ProvidersNisItem.  # noqa: E501
        :rtype: int
        """
        return self._retry_time

    @retry_time.setter
    def retry_time(self, retry_time):
        """Sets the retry_time of this ProvidersNisItem.

        Specifies the timeout period in seconds after which a request will be retried.  # noqa: E501

        :param retry_time: The retry_time of this ProvidersNisItem.  # noqa: E501
        :type: int
        """
        if retry_time is not None and retry_time > 3600:  # noqa: E501
            raise ValueError("Invalid value for `retry_time`, must be a value less than or equal to `3600`")  # noqa: E501
        if retry_time is not None and retry_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `retry_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._retry_time = retry_time

    @property
    def servers(self):
        """Gets the servers of this ProvidersNisItem.  # noqa: E501

        Adds an NIS server for this provider.  # noqa: E501

        :return: The servers of this ProvidersNisItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this ProvidersNisItem.

        Adds an NIS server for this provider.  # noqa: E501

        :param servers: The servers of this ProvidersNisItem.  # noqa: E501
        :type: list[str]
        """
        if servers is None:
            raise ValueError("Invalid value for `servers`, must not be `None`")  # noqa: E501

        self._servers = servers

    @property
    def unfindable_groups(self):
        """Gets the unfindable_groups of this ProvidersNisItem.  # noqa: E501

        Specifies groups that cannot be resolved by the provider.  # noqa: E501

        :return: The unfindable_groups of this ProvidersNisItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unfindable_groups

    @unfindable_groups.setter
    def unfindable_groups(self, unfindable_groups):
        """Sets the unfindable_groups of this ProvidersNisItem.

        Specifies groups that cannot be resolved by the provider.  # noqa: E501

        :param unfindable_groups: The unfindable_groups of this ProvidersNisItem.  # noqa: E501
        :type: list[str]
        """

        self._unfindable_groups = unfindable_groups

    @property
    def unfindable_users(self):
        """Gets the unfindable_users of this ProvidersNisItem.  # noqa: E501

        Specifies users that cannot be resolved by the provider.  # noqa: E501

        :return: The unfindable_users of this ProvidersNisItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unfindable_users

    @unfindable_users.setter
    def unfindable_users(self, unfindable_users):
        """Sets the unfindable_users of this ProvidersNisItem.

        Specifies users that cannot be resolved by the provider.  # noqa: E501

        :param unfindable_users: The unfindable_users of this ProvidersNisItem.  # noqa: E501
        :type: list[str]
        """

        self._unfindable_users = unfindable_users

    @property
    def unlistable_groups(self):
        """Gets the unlistable_groups of this ProvidersNisItem.  # noqa: E501

        Specifies a group that cannot be listed by the provider.  # noqa: E501

        :return: The unlistable_groups of this ProvidersNisItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unlistable_groups

    @unlistable_groups.setter
    def unlistable_groups(self, unlistable_groups):
        """Sets the unlistable_groups of this ProvidersNisItem.

        Specifies a group that cannot be listed by the provider.  # noqa: E501

        :param unlistable_groups: The unlistable_groups of this ProvidersNisItem.  # noqa: E501
        :type: list[str]
        """

        self._unlistable_groups = unlistable_groups

    @property
    def unlistable_users(self):
        """Gets the unlistable_users of this ProvidersNisItem.  # noqa: E501

        Specifies a user that cannot be listed by the provider.  # noqa: E501

        :return: The unlistable_users of this ProvidersNisItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._unlistable_users

    @unlistable_users.setter
    def unlistable_users(self, unlistable_users):
        """Sets the unlistable_users of this ProvidersNisItem.

        Specifies a user that cannot be listed by the provider.  # noqa: E501

        :param unlistable_users: The unlistable_users of this ProvidersNisItem.  # noqa: E501
        :type: list[str]
        """

        self._unlistable_users = unlistable_users

    @property
    def user_domain(self):
        """Gets the user_domain of this ProvidersNisItem.  # noqa: E501

        Specifies the domain for this provider through which users are qualified.  # noqa: E501

        :return: The user_domain of this ProvidersNisItem.  # noqa: E501
        :rtype: str
        """
        return self._user_domain

    @user_domain.setter
    def user_domain(self, user_domain):
        """Sets the user_domain of this ProvidersNisItem.

        Specifies the domain for this provider through which users are qualified.  # noqa: E501

        :param user_domain: The user_domain of this ProvidersNisItem.  # noqa: E501
        :type: str
        """
        if user_domain is not None and len(user_domain) > 255:
            raise ValueError("Invalid value for `user_domain`, length must be less than or equal to `255`")  # noqa: E501
        if user_domain is not None and len(user_domain) < 0:
            raise ValueError("Invalid value for `user_domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._user_domain = user_domain

    @property
    def ypmatch_using_tcp(self):
        """Gets the ypmatch_using_tcp of this ProvidersNisItem.  # noqa: E501

        If true, specifies TCP for YP Match operations.  # noqa: E501

        :return: The ypmatch_using_tcp of this ProvidersNisItem.  # noqa: E501
        :rtype: bool
        """
        return self._ypmatch_using_tcp

    @ypmatch_using_tcp.setter
    def ypmatch_using_tcp(self, ypmatch_using_tcp):
        """Sets the ypmatch_using_tcp of this ProvidersNisItem.

        If true, specifies TCP for YP Match operations.  # noqa: E501

        :param ypmatch_using_tcp: The ypmatch_using_tcp of this ProvidersNisItem.  # noqa: E501
        :type: bool
        """

        self._ypmatch_using_tcp = ypmatch_using_tcp

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
        if issubclass(ProvidersNisItem, dict):
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
        if not isinstance(other, ProvidersNisItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
