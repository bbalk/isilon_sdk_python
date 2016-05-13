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


class AuthGroupExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuthGroupExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'gid': 'int',
            'dn': 'str',
            'dns_domain': 'str',
            'domain': 'str',
            'generated_gid': 'bool',
            'id': 'str',
            'member_of': 'list[GroupMember]',
            'name': 'str',
            'provider': 'str',
            'sam_account_name': 'str',
            'sid': 'GroupMember',
            'type': 'str'
        }

        self.attribute_map = {
            'gid': 'gid',
            'dn': 'dn',
            'dns_domain': 'dns_domain',
            'domain': 'domain',
            'generated_gid': 'generated_gid',
            'id': 'id',
            'member_of': 'member_of',
            'name': 'name',
            'provider': 'provider',
            'sam_account_name': 'sam_account_name',
            'sid': 'sid',
            'type': 'type'
        }

        self._gid = None
        self._dn = None
        self._dns_domain = None
        self._domain = None
        self._generated_gid = None
        self._id = None
        self._member_of = None
        self._name = None
        self._provider = None
        self._sam_account_name = None
        self._sid = None
        self._type = None

    @property
    def gid(self):
        """
        Gets the gid of this AuthGroupExtended.
        Specifies the numeric group identifier.

        :return: The gid of this AuthGroupExtended.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """
        Sets the gid of this AuthGroupExtended.
        Specifies the numeric group identifier.

        :param gid: The gid of this AuthGroupExtended.
        :type: int
        """
        
        self._gid = gid

    @property
    def dn(self):
        """
        Gets the dn of this AuthGroupExtended.
        Specifies the distinguished name for the user.

        :return: The dn of this AuthGroupExtended.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this AuthGroupExtended.
        Specifies the distinguished name for the user.

        :param dn: The dn of this AuthGroupExtended.
        :type: str
        """
        
        self._dn = dn

    @property
    def dns_domain(self):
        """
        Gets the dns_domain of this AuthGroupExtended.
        Specifies the DNS domain.

        :return: The dns_domain of this AuthGroupExtended.
        :rtype: str
        """
        return self._dns_domain

    @dns_domain.setter
    def dns_domain(self, dns_domain):
        """
        Sets the dns_domain of this AuthGroupExtended.
        Specifies the DNS domain.

        :param dns_domain: The dns_domain of this AuthGroupExtended.
        :type: str
        """
        
        self._dns_domain = dns_domain

    @property
    def domain(self):
        """
        Gets the domain of this AuthGroupExtended.
        Specifies the domain that the object is part of.

        :return: The domain of this AuthGroupExtended.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this AuthGroupExtended.
        Specifies the domain that the object is part of.

        :param domain: The domain of this AuthGroupExtended.
        :type: str
        """
        
        self._domain = domain

    @property
    def generated_gid(self):
        """
        Gets the generated_gid of this AuthGroupExtended.
        If true, the GID was generated.

        :return: The generated_gid of this AuthGroupExtended.
        :rtype: bool
        """
        return self._generated_gid

    @generated_gid.setter
    def generated_gid(self, generated_gid):
        """
        Sets the generated_gid of this AuthGroupExtended.
        If true, the GID was generated.

        :param generated_gid: The generated_gid of this AuthGroupExtended.
        :type: bool
        """
        
        self._generated_gid = generated_gid

    @property
    def id(self):
        """
        Gets the id of this AuthGroupExtended.
        Specifies the user or group ID.

        :return: The id of this AuthGroupExtended.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuthGroupExtended.
        Specifies the user or group ID.

        :param id: The id of this AuthGroupExtended.
        :type: str
        """
        
        self._id = id

    @property
    def member_of(self):
        """
        Gets the member_of of this AuthGroupExtended.


        :return: The member_of of this AuthGroupExtended.
        :rtype: list[GroupMember]
        """
        return self._member_of

    @member_of.setter
    def member_of(self, member_of):
        """
        Sets the member_of of this AuthGroupExtended.


        :param member_of: The member_of of this AuthGroupExtended.
        :type: list[GroupMember]
        """
        
        self._member_of = member_of

    @property
    def name(self):
        """
        Gets the name of this AuthGroupExtended.
        Specifies a user or group name.

        :return: The name of this AuthGroupExtended.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AuthGroupExtended.
        Specifies a user or group name.

        :param name: The name of this AuthGroupExtended.
        :type: str
        """
        
        self._name = name

    @property
    def provider(self):
        """
        Gets the provider of this AuthGroupExtended.
        Specifies the authentication provider that the object belongs to.

        :return: The provider of this AuthGroupExtended.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this AuthGroupExtended.
        Specifies the authentication provider that the object belongs to.

        :param provider: The provider of this AuthGroupExtended.
        :type: str
        """
        
        self._provider = provider

    @property
    def sam_account_name(self):
        """
        Gets the sam_account_name of this AuthGroupExtended.
        Specifies a user or group name.

        :return: The sam_account_name of this AuthGroupExtended.
        :rtype: str
        """
        return self._sam_account_name

    @sam_account_name.setter
    def sam_account_name(self, sam_account_name):
        """
        Sets the sam_account_name of this AuthGroupExtended.
        Specifies a user or group name.

        :param sam_account_name: The sam_account_name of this AuthGroupExtended.
        :type: str
        """
        
        self._sam_account_name = sam_account_name

    @property
    def sid(self):
        """
        Gets the sid of this AuthGroupExtended.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :return: The sid of this AuthGroupExtended.
        :rtype: GroupMember
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this AuthGroupExtended.
        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.

        :param sid: The sid of this AuthGroupExtended.
        :type: GroupMember
        """
        
        self._sid = sid

    @property
    def type(self):
        """
        Gets the type of this AuthGroupExtended.
        Specifies the object type.

        :return: The type of this AuthGroupExtended.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AuthGroupExtended.
        Specifies the object type.

        :param type: The type of this AuthGroupExtended.
        :type: str
        """
        
        self._type = type

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

