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


class SummaryProtocolStatsProtocolStatsNetworkIn(object):
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
        'errors_per_sec': 'float',
        'megabytes_per_sec': 'float',
        'packets_per_sec': 'float'
    }

    attribute_map = {
        'errors_per_sec': 'errors_per_sec',
        'megabytes_per_sec': 'megabytes_per_sec',
        'packets_per_sec': 'packets_per_sec'
    }

    def __init__(self, errors_per_sec=None, megabytes_per_sec=None, packets_per_sec=None):  # noqa: E501
        """SummaryProtocolStatsProtocolStatsNetworkIn - a model defined in Swagger"""  # noqa: E501

        self._errors_per_sec = None
        self._megabytes_per_sec = None
        self._packets_per_sec = None
        self.discriminator = None

        self.errors_per_sec = errors_per_sec
        self.megabytes_per_sec = megabytes_per_sec
        self.packets_per_sec = packets_per_sec

    @property
    def errors_per_sec(self):
        """Gets the errors_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.  # noqa: E501

        Network input errors per-second  # noqa: E501

        :return: The errors_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.  # noqa: E501
        :rtype: float
        """
        return self._errors_per_sec

    @errors_per_sec.setter
    def errors_per_sec(self, errors_per_sec):
        """Sets the errors_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.

        Network input errors per-second  # noqa: E501

        :param errors_per_sec: The errors_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.  # noqa: E501
        :type: float
        """
        if errors_per_sec is None:
            raise ValueError("Invalid value for `errors_per_sec`, must not be `None`")  # noqa: E501

        self._errors_per_sec = errors_per_sec

    @property
    def megabytes_per_sec(self):
        """Gets the megabytes_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.  # noqa: E501

        Network input megabytes per-second  # noqa: E501

        :return: The megabytes_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.  # noqa: E501
        :rtype: float
        """
        return self._megabytes_per_sec

    @megabytes_per_sec.setter
    def megabytes_per_sec(self, megabytes_per_sec):
        """Sets the megabytes_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.

        Network input megabytes per-second  # noqa: E501

        :param megabytes_per_sec: The megabytes_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.  # noqa: E501
        :type: float
        """
        if megabytes_per_sec is None:
            raise ValueError("Invalid value for `megabytes_per_sec`, must not be `None`")  # noqa: E501

        self._megabytes_per_sec = megabytes_per_sec

    @property
    def packets_per_sec(self):
        """Gets the packets_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.  # noqa: E501

        Network input packets per-second  # noqa: E501

        :return: The packets_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.  # noqa: E501
        :rtype: float
        """
        return self._packets_per_sec

    @packets_per_sec.setter
    def packets_per_sec(self, packets_per_sec):
        """Sets the packets_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.

        Network input packets per-second  # noqa: E501

        :param packets_per_sec: The packets_per_sec of this SummaryProtocolStatsProtocolStatsNetworkIn.  # noqa: E501
        :type: float
        """
        if packets_per_sec is None:
            raise ValueError("Invalid value for `packets_per_sec`, must not be `None`")  # noqa: E501

        self._packets_per_sec = packets_per_sec

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
        if not isinstance(other, SummaryProtocolStatsProtocolStatsNetworkIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
