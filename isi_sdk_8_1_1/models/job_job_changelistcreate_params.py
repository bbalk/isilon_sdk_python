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


class JobJobChangelistcreateParams(object):
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
        'newer_snapid': 'int',
        'older_snapid': 'int',
        'retain_repstate': 'bool'
    }

    attribute_map = {
        'newer_snapid': 'newer_snapid',
        'older_snapid': 'older_snapid',
        'retain_repstate': 'retain_repstate'
    }

    def __init__(self, newer_snapid=None, older_snapid=None, retain_repstate=None):  # noqa: E501
        """JobJobChangelistcreateParams - a model defined in Swagger"""  # noqa: E501

        self._newer_snapid = None
        self._older_snapid = None
        self._retain_repstate = None
        self.discriminator = None

        self.newer_snapid = newer_snapid
        self.older_snapid = older_snapid
        if retain_repstate is not None:
            self.retain_repstate = retain_repstate

    @property
    def newer_snapid(self):
        """Gets the newer_snapid of this JobJobChangelistcreateParams.  # noqa: E501

        Newer snapshot ID.  # noqa: E501

        :return: The newer_snapid of this JobJobChangelistcreateParams.  # noqa: E501
        :rtype: int
        """
        return self._newer_snapid

    @newer_snapid.setter
    def newer_snapid(self, newer_snapid):
        """Sets the newer_snapid of this JobJobChangelistcreateParams.

        Newer snapshot ID.  # noqa: E501

        :param newer_snapid: The newer_snapid of this JobJobChangelistcreateParams.  # noqa: E501
        :type: int
        """
        if newer_snapid is None:
            raise ValueError("Invalid value for `newer_snapid`, must not be `None`")  # noqa: E501
        if newer_snapid is not None and newer_snapid < 1:  # noqa: E501
            raise ValueError("Invalid value for `newer_snapid`, must be a value greater than or equal to `1`")  # noqa: E501

        self._newer_snapid = newer_snapid

    @property
    def older_snapid(self):
        """Gets the older_snapid of this JobJobChangelistcreateParams.  # noqa: E501

        Older snapshot ID.  # noqa: E501

        :return: The older_snapid of this JobJobChangelistcreateParams.  # noqa: E501
        :rtype: int
        """
        return self._older_snapid

    @older_snapid.setter
    def older_snapid(self, older_snapid):
        """Sets the older_snapid of this JobJobChangelistcreateParams.

        Older snapshot ID.  # noqa: E501

        :param older_snapid: The older_snapid of this JobJobChangelistcreateParams.  # noqa: E501
        :type: int
        """
        if older_snapid is None:
            raise ValueError("Invalid value for `older_snapid`, must not be `None`")  # noqa: E501
        if older_snapid is not None and older_snapid < 1:  # noqa: E501
            raise ValueError("Invalid value for `older_snapid`, must be a value greater than or equal to `1`")  # noqa: E501

        self._older_snapid = older_snapid

    @property
    def retain_repstate(self):
        """Gets the retain_repstate of this JobJobChangelistcreateParams.  # noqa: E501

        Whether to retain the replication record after a changelist is created. Retaining a replication record allows a changelist to be recreated later.  # noqa: E501

        :return: The retain_repstate of this JobJobChangelistcreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._retain_repstate

    @retain_repstate.setter
    def retain_repstate(self, retain_repstate):
        """Sets the retain_repstate of this JobJobChangelistcreateParams.

        Whether to retain the replication record after a changelist is created. Retaining a replication record allows a changelist to be recreated later.  # noqa: E501

        :param retain_repstate: The retain_repstate of this JobJobChangelistcreateParams.  # noqa: E501
        :type: bool
        """

        self._retain_repstate = retain_repstate

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
        if issubclass(JobJobChangelistcreateParams, dict):
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
        if not isinstance(other, JobJobChangelistcreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
