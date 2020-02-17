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


class AdsProviderControllersController(object):
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
        'dc_address': 'str',
        'dc_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'dc_address': 'dc_address',
        'dc_name': 'dc_name',
        'id': 'id'
    }

    def __init__(self, dc_address=None, dc_name=None, id=None):  # noqa: E501
        """AdsProviderControllersController - a model defined in Swagger"""  # noqa: E501

        self._dc_address = None
        self._dc_name = None
        self._id = None
        self.discriminator = None

        if dc_address is not None:
            self.dc_address = dc_address
        if dc_name is not None:
            self.dc_name = dc_name
        if id is not None:
            self.id = id

    @property
    def dc_address(self):
        """Gets the dc_address of this AdsProviderControllersController.  # noqa: E501

        Specifies the address for the domain controller.  # noqa: E501

        :return: The dc_address of this AdsProviderControllersController.  # noqa: E501
        :rtype: str
        """
        return self._dc_address

    @dc_address.setter
    def dc_address(self, dc_address):
        """Sets the dc_address of this AdsProviderControllersController.

        Specifies the address for the domain controller.  # noqa: E501

        :param dc_address: The dc_address of this AdsProviderControllersController.  # noqa: E501
        :type: str
        """
        if dc_address is not None and len(dc_address) > 255:
            raise ValueError("Invalid value for `dc_address`, length must be less than or equal to `255`")  # noqa: E501
        if dc_address is not None and len(dc_address) < 0:
            raise ValueError("Invalid value for `dc_address`, length must be greater than or equal to `0`")  # noqa: E501

        self._dc_address = dc_address

    @property
    def dc_name(self):
        """Gets the dc_name of this AdsProviderControllersController.  # noqa: E501

        Specifies the name of the domain controller.  # noqa: E501

        :return: The dc_name of this AdsProviderControllersController.  # noqa: E501
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        """Sets the dc_name of this AdsProviderControllersController.

        Specifies the name of the domain controller.  # noqa: E501

        :param dc_name: The dc_name of this AdsProviderControllersController.  # noqa: E501
        :type: str
        """
        if dc_name is not None and len(dc_name) > 255:
            raise ValueError("Invalid value for `dc_name`, length must be less than or equal to `255`")  # noqa: E501
        if dc_name is not None and len(dc_name) < 0:
            raise ValueError("Invalid value for `dc_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._dc_name = dc_name

    @property
    def id(self):
        """Gets the id of this AdsProviderControllersController.  # noqa: E501

        Specifies the address for the domain controller. This value is the same as the 'dc_address' value.  # noqa: E501

        :return: The id of this AdsProviderControllersController.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdsProviderControllersController.

        Specifies the address for the domain controller. This value is the same as the 'dc_address' value.  # noqa: E501

        :param id: The id of this AdsProviderControllersController.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

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
        if issubclass(AdsProviderControllersController, dict):
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
        if not isinstance(other, AdsProviderControllersController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
