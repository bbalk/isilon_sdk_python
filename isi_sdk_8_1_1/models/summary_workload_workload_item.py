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


class SummaryWorkloadWorkloadItem(object):
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
        'cpu': 'float',
        'job_type': 'str',
        'l2': 'float',
        'l3': 'float',
        'node': 'float',
        'reads': 'float',
        'system_name': 'str',
        'writes': 'float'
    }

    attribute_map = {
        'cpu': 'cpu',
        'job_type': 'job_type',
        'l2': 'l2',
        'l3': 'l3',
        'node': 'node',
        'reads': 'reads',
        'system_name': 'system_name',
        'writes': 'writes'
    }

    def __init__(self, cpu=None, job_type=None, l2=None, l3=None, node=None, reads=None, system_name=None, writes=None):  # noqa: E501
        """SummaryWorkloadWorkloadItem - a model defined in Swagger"""  # noqa: E501

        self._cpu = None
        self._job_type = None
        self._l2 = None
        self._l3 = None
        self._node = None
        self._reads = None
        self._system_name = None
        self._writes = None
        self.discriminator = None

        self.cpu = cpu
        if job_type is not None:
            self.job_type = job_type
        self.l2 = l2
        self.l3 = l3
        self.node = node
        self.reads = reads
        if system_name is not None:
            self.system_name = system_name
        self.writes = writes

    @property
    def cpu(self):
        """Gets the cpu of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The number (across all cores) of micro-seconds per second.  # noqa: E501

        :return: The cpu of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this SummaryWorkloadWorkloadItem.

        The number (across all cores) of micro-seconds per second.  # noqa: E501

        :param cpu: The cpu of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if cpu is None:
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def job_type(self):
        """Gets the job_type of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The canonical name for the job followed by phase in brackets, ie. 'AVscan[1]', etc...  # noqa: E501

        :return: The job_type of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this SummaryWorkloadWorkloadItem.

        The canonical name for the job followed by phase in brackets, ie. 'AVscan[1]', etc...  # noqa: E501

        :param job_type: The job_type of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._job_type = job_type

    @property
    def l2(self):
        """Gets the l2 of this SummaryWorkloadWorkloadItem.  # noqa: E501

        L2 cache hits per second.  # noqa: E501

        :return: The l2 of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this SummaryWorkloadWorkloadItem.

        L2 cache hits per second.  # noqa: E501

        :param l2: The l2 of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if l2 is None:
            raise ValueError("Invalid value for `l2`, must not be `None`")  # noqa: E501

        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this SummaryWorkloadWorkloadItem.  # noqa: E501

        L3 cache hits per second.  # noqa: E501

        :return: The l3 of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this SummaryWorkloadWorkloadItem.

        L3 cache hits per second.  # noqa: E501

        :param l3: The l3 of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if l3 is None:
            raise ValueError("Invalid value for `l3`, must not be `None`")  # noqa: E501

        self._l3 = l3

    @property
    def node(self):
        """Gets the node of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The node on which the operation was performed.  # noqa: E501

        :return: The node of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this SummaryWorkloadWorkloadItem.

        The node on which the operation was performed.  # noqa: E501

        :param node: The node of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def reads(self):
        """Gets the reads of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Disk read operations per second.  # noqa: E501

        :return: The reads of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._reads

    @reads.setter
    def reads(self, reads):
        """Sets the reads of this SummaryWorkloadWorkloadItem.

        Disk read operations per second.  # noqa: E501

        :param reads: The reads of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if reads is None:
            raise ValueError("Invalid value for `reads`, must not be `None`")  # noqa: E501

        self._reads = reads

    @property
    def system_name(self):
        """Gets the system_name of this SummaryWorkloadWorkloadItem.  # noqa: E501

        The process name, job ID, etc...  # noqa: E501

        :return: The system_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this SummaryWorkloadWorkloadItem.

        The process name, job ID, etc...  # noqa: E501

        :param system_name: The system_name of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def writes(self):
        """Gets the writes of this SummaryWorkloadWorkloadItem.  # noqa: E501

        Disk write operations per second.  # noqa: E501

        :return: The writes of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :rtype: float
        """
        return self._writes

    @writes.setter
    def writes(self, writes):
        """Sets the writes of this SummaryWorkloadWorkloadItem.

        Disk write operations per second.  # noqa: E501

        :param writes: The writes of this SummaryWorkloadWorkloadItem.  # noqa: E501
        :type: float
        """
        if writes is None:
            raise ValueError("Invalid value for `writes`, must not be `None`")  # noqa: E501

        self._writes = writes

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
        if issubclass(SummaryWorkloadWorkloadItem, dict):
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
        if not isinstance(other, SummaryWorkloadWorkloadItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
