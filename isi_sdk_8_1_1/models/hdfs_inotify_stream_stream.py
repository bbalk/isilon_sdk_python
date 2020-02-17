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


class HdfsInotifyStreamStream(object):
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
        'current_transaction_id': 'int',
        'sync_transaction_id': 'int'
    }

    attribute_map = {
        'current_transaction_id': 'current_transaction_id',
        'sync_transaction_id': 'sync_transaction_id'
    }

    def __init__(self, current_transaction_id=None, sync_transaction_id=None):  # noqa: E501
        """HdfsInotifyStreamStream - a model defined in Swagger"""  # noqa: E501

        self._current_transaction_id = None
        self._sync_transaction_id = None
        self.discriminator = None

        if current_transaction_id is not None:
            self.current_transaction_id = current_transaction_id
        if sync_transaction_id is not None:
            self.sync_transaction_id = sync_transaction_id

    @property
    def current_transaction_id(self):
        """Gets the current_transaction_id of this HdfsInotifyStreamStream.  # noqa: E501

        The transaction id of the most recent edit applied over HDFS.  # noqa: E501

        :return: The current_transaction_id of this HdfsInotifyStreamStream.  # noqa: E501
        :rtype: int
        """
        return self._current_transaction_id

    @current_transaction_id.setter
    def current_transaction_id(self, current_transaction_id):
        """Sets the current_transaction_id of this HdfsInotifyStreamStream.

        The transaction id of the most recent edit applied over HDFS.  # noqa: E501

        :param current_transaction_id: The current_transaction_id of this HdfsInotifyStreamStream.  # noqa: E501
        :type: int
        """
        if current_transaction_id is not None and current_transaction_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `current_transaction_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if current_transaction_id is not None and current_transaction_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `current_transaction_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._current_transaction_id = current_transaction_id

    @property
    def sync_transaction_id(self):
        """Gets the sync_transaction_id of this HdfsInotifyStreamStream.  # noqa: E501

        The transaction id of the latest edit exposed via HDFS INotify stream. This id usually lags behind the current_transaction_id.  # noqa: E501

        :return: The sync_transaction_id of this HdfsInotifyStreamStream.  # noqa: E501
        :rtype: int
        """
        return self._sync_transaction_id

    @sync_transaction_id.setter
    def sync_transaction_id(self, sync_transaction_id):
        """Sets the sync_transaction_id of this HdfsInotifyStreamStream.

        The transaction id of the latest edit exposed via HDFS INotify stream. This id usually lags behind the current_transaction_id.  # noqa: E501

        :param sync_transaction_id: The sync_transaction_id of this HdfsInotifyStreamStream.  # noqa: E501
        :type: int
        """
        if sync_transaction_id is not None and sync_transaction_id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `sync_transaction_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if sync_transaction_id is not None and sync_transaction_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `sync_transaction_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._sync_transaction_id = sync_transaction_id

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
        if issubclass(HdfsInotifyStreamStream, dict):
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
        if not isinstance(other, HdfsInotifyStreamStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
