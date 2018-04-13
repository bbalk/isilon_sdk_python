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


class AdsProviderDomainsDomain(object):
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
        'client_site': 'str',
        'dc_address': 'str',
        'dc_name': 'str',
        'dc_site': 'str',
        'domain': 'str',
        'guid': 'str',
        'id': 'str',
        'netbios_name': 'str',
        'sid': 'str',
        'status': 'str',
        'trust_type': 'str'
    }

    attribute_map = {
        'client_site': 'client_site',
        'dc_address': 'dc_address',
        'dc_name': 'dc_name',
        'dc_site': 'dc_site',
        'domain': 'domain',
        'guid': 'guid',
        'id': 'id',
        'netbios_name': 'netbios_name',
        'sid': 'sid',
        'status': 'status',
        'trust_type': 'trust_type'
    }

    def __init__(self, client_site=None, dc_address=None, dc_name=None, dc_site=None, domain=None, guid=None, id=None, netbios_name=None, sid=None, status=None, trust_type=None):  # noqa: E501
        """AdsProviderDomainsDomain - a model defined in Swagger"""  # noqa: E501

        self._client_site = None
        self._dc_address = None
        self._dc_name = None
        self._dc_site = None
        self._domain = None
        self._guid = None
        self._id = None
        self._netbios_name = None
        self._sid = None
        self._status = None
        self._trust_type = None
        self.discriminator = None

        if client_site is not None:
            self.client_site = client_site
        if dc_address is not None:
            self.dc_address = dc_address
        if dc_name is not None:
            self.dc_name = dc_name
        if dc_site is not None:
            self.dc_site = dc_site
        if domain is not None:
            self.domain = domain
        if guid is not None:
            self.guid = guid
        if id is not None:
            self.id = id
        if netbios_name is not None:
            self.netbios_name = netbios_name
        if sid is not None:
            self.sid = sid
        if status is not None:
            self.status = status
        if trust_type is not None:
            self.trust_type = trust_type

    @property
    def client_site(self):
        """Gets the client_site of this AdsProviderDomainsDomain.  # noqa: E501

        The Nodes Site.  # noqa: E501

        :return: The client_site of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._client_site

    @client_site.setter
    def client_site(self, client_site):
        """Sets the client_site of this AdsProviderDomainsDomain.

        The Nodes Site.  # noqa: E501

        :param client_site: The client_site of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._client_site = client_site

    @property
    def dc_address(self):
        """Gets the dc_address of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies the address for the domain controller.  # noqa: E501

        :return: The dc_address of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._dc_address

    @dc_address.setter
    def dc_address(self, dc_address):
        """Sets the dc_address of this AdsProviderDomainsDomain.

        Specifies the address for the domain controller.  # noqa: E501

        :param dc_address: The dc_address of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._dc_address = dc_address

    @property
    def dc_name(self):
        """Gets the dc_name of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies the name for the domain controller.  # noqa: E501

        :return: The dc_name of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        """Sets the dc_name of this AdsProviderDomainsDomain.

        Specifies the name for the domain controller.  # noqa: E501

        :param dc_name: The dc_name of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._dc_name = dc_name

    @property
    def dc_site(self):
        """Gets the dc_site of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies the site for the domain controller.  # noqa: E501

        :return: The dc_site of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._dc_site

    @dc_site.setter
    def dc_site(self, dc_site):
        """Sets the dc_site of this AdsProviderDomainsDomain.

        Specifies the site for the domain controller.  # noqa: E501

        :param dc_site: The dc_site of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._dc_site = dc_site

    @property
    def domain(self):
        """Gets the domain of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies the name of the domain.  # noqa: E501

        :return: The domain of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AdsProviderDomainsDomain.

        Specifies the name of the domain.  # noqa: E501

        :param domain: The domain of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def guid(self):
        """Gets the guid of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies the globally unique ID for the domain.  # noqa: E501

        :return: The guid of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this AdsProviderDomainsDomain.

        Specifies the globally unique ID for the domain.  # noqa: E501

        :param guid: The guid of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def id(self):
        """Gets the id of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies a unique identifier for every domain returned.  # noqa: E501

        :return: The id of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdsProviderDomainsDomain.

        Specifies a unique identifier for every domain returned.  # noqa: E501

        :param id: The id of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def netbios_name(self):
        """Gets the netbios_name of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies the NetBIOS name for the domain.  # noqa: E501

        :return: The netbios_name of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._netbios_name

    @netbios_name.setter
    def netbios_name(self, netbios_name):
        """Sets the netbios_name of this AdsProviderDomainsDomain.

        Specifies the NetBIOS name for the domain.  # noqa: E501

        :param netbios_name: The netbios_name of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._netbios_name = netbios_name

    @property
    def sid(self):
        """Gets the sid of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies the security ID for the domain.  # noqa: E501

        :return: The sid of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this AdsProviderDomainsDomain.

        Specifies the security ID for the domain.  # noqa: E501

        :param sid: The sid of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._sid = sid

    @property
    def status(self):
        """Gets the status of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies the status of the domain.  # noqa: E501

        :return: The status of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AdsProviderDomainsDomain.

        Specifies the status of the domain.  # noqa: E501

        :param status: The status of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def trust_type(self):
        """Gets the trust_type of this AdsProviderDomainsDomain.  # noqa: E501

        Specifies the type of trust for this domain. Options include 'primary', 'unknown', 'external', and 'forest'.  # noqa: E501

        :return: The trust_type of this AdsProviderDomainsDomain.  # noqa: E501
        :rtype: str
        """
        return self._trust_type

    @trust_type.setter
    def trust_type(self, trust_type):
        """Sets the trust_type of this AdsProviderDomainsDomain.

        Specifies the type of trust for this domain. Options include 'primary', 'unknown', 'external', and 'forest'.  # noqa: E501

        :param trust_type: The trust_type of this AdsProviderDomainsDomain.  # noqa: E501
        :type: str
        """

        self._trust_type = trust_type

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
        if not isinstance(other, AdsProviderDomainsDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
