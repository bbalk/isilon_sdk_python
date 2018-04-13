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


class SyncJobWorker(object):
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
        'connected': 'bool',
        'last_split': 'int',
        'last_work': 'int',
        'lin': 'int',
        'lnn': 'int',
        'process_id': 'int',
        'source_host': 'str',
        'target_host': 'str',
        'worker_id': 'int'
    }

    attribute_map = {
        'connected': 'connected',
        'last_split': 'last_split',
        'last_work': 'last_work',
        'lin': 'lin',
        'lnn': 'lnn',
        'process_id': 'process_id',
        'source_host': 'source_host',
        'target_host': 'target_host',
        'worker_id': 'worker_id'
    }

    def __init__(self, connected=None, last_split=None, last_work=None, lin=None, lnn=None, process_id=None, source_host=None, target_host=None, worker_id=None):  # noqa: E501
        """SyncJobWorker - a model defined in Swagger"""  # noqa: E501

        self._connected = None
        self._last_split = None
        self._last_work = None
        self._lin = None
        self._lnn = None
        self._process_id = None
        self._source_host = None
        self._target_host = None
        self._worker_id = None
        self.discriminator = None

        if connected is not None:
            self.connected = connected
        if last_split is not None:
            self.last_split = last_split
        if last_work is not None:
            self.last_work = last_work
        if lin is not None:
            self.lin = lin
        if lnn is not None:
            self.lnn = lnn
        if process_id is not None:
            self.process_id = process_id
        if source_host is not None:
            self.source_host = source_host
        if target_host is not None:
            self.target_host = target_host
        if worker_id is not None:
            self.worker_id = worker_id

    @property
    def connected(self):
        """Gets the connected of this SyncJobWorker.  # noqa: E501

        Whether there is a connection between the source and target.  # noqa: E501

        :return: The connected of this SyncJobWorker.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this SyncJobWorker.

        Whether there is a connection between the source and target.  # noqa: E501

        :param connected: The connected of this SyncJobWorker.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def last_split(self):
        """Gets the last_split of this SyncJobWorker.  # noqa: E501

        The last time a network split occurred.  # noqa: E501

        :return: The last_split of this SyncJobWorker.  # noqa: E501
        :rtype: int
        """
        return self._last_split

    @last_split.setter
    def last_split(self, last_split):
        """Sets the last_split of this SyncJobWorker.

        The last time a network split occurred.  # noqa: E501

        :param last_split: The last_split of this SyncJobWorker.  # noqa: E501
        :type: int
        """

        self._last_split = last_split

    @property
    def last_work(self):
        """Gets the last_work of this SyncJobWorker.  # noqa: E501

        The last time the worker performed work.  # noqa: E501

        :return: The last_work of this SyncJobWorker.  # noqa: E501
        :rtype: int
        """
        return self._last_work

    @last_work.setter
    def last_work(self, last_work):
        """Sets the last_work of this SyncJobWorker.

        The last time the worker performed work.  # noqa: E501

        :param last_work: The last_work of this SyncJobWorker.  # noqa: E501
        :type: int
        """

        self._last_work = last_work

    @property
    def lin(self):
        """Gets the lin of this SyncJobWorker.  # noqa: E501

        The LIN being worked on.  # noqa: E501

        :return: The lin of this SyncJobWorker.  # noqa: E501
        :rtype: int
        """
        return self._lin

    @lin.setter
    def lin(self, lin):
        """Sets the lin of this SyncJobWorker.

        The LIN being worked on.  # noqa: E501

        :param lin: The lin of this SyncJobWorker.  # noqa: E501
        :type: int
        """

        self._lin = lin

    @property
    def lnn(self):
        """Gets the lnn of this SyncJobWorker.  # noqa: E501

        The lnn the worker is assigned to run on.  # noqa: E501

        :return: The lnn of this SyncJobWorker.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this SyncJobWorker.

        The lnn the worker is assigned to run on.  # noqa: E501

        :param lnn: The lnn of this SyncJobWorker.  # noqa: E501
        :type: int
        """

        self._lnn = lnn

    @property
    def process_id(self):
        """Gets the process_id of this SyncJobWorker.  # noqa: E501

        The process ID of the worker.  # noqa: E501

        :return: The process_id of this SyncJobWorker.  # noqa: E501
        :rtype: int
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        """Sets the process_id of this SyncJobWorker.

        The process ID of the worker.  # noqa: E501

        :param process_id: The process_id of this SyncJobWorker.  # noqa: E501
        :type: int
        """

        self._process_id = process_id

    @property
    def source_host(self):
        """Gets the source_host of this SyncJobWorker.  # noqa: E501

        The source host for this worker.  # noqa: E501

        :return: The source_host of this SyncJobWorker.  # noqa: E501
        :rtype: str
        """
        return self._source_host

    @source_host.setter
    def source_host(self, source_host):
        """Sets the source_host of this SyncJobWorker.

        The source host for this worker.  # noqa: E501

        :param source_host: The source_host of this SyncJobWorker.  # noqa: E501
        :type: str
        """

        self._source_host = source_host

    @property
    def target_host(self):
        """Gets the target_host of this SyncJobWorker.  # noqa: E501

        The target host for this worker.  # noqa: E501

        :return: The target_host of this SyncJobWorker.  # noqa: E501
        :rtype: str
        """
        return self._target_host

    @target_host.setter
    def target_host(self, target_host):
        """Sets the target_host of this SyncJobWorker.

        The target host for this worker.  # noqa: E501

        :param target_host: The target_host of this SyncJobWorker.  # noqa: E501
        :type: str
        """

        self._target_host = target_host

    @property
    def worker_id(self):
        """Gets the worker_id of this SyncJobWorker.  # noqa: E501

        The ID of the worker.  # noqa: E501

        :return: The worker_id of this SyncJobWorker.  # noqa: E501
        :rtype: int
        """
        return self._worker_id

    @worker_id.setter
    def worker_id(self, worker_id):
        """Sets the worker_id of this SyncJobWorker.

        The ID of the worker.  # noqa: E501

        :param worker_id: The worker_id of this SyncJobWorker.  # noqa: E501
        :type: int
        """

        self._worker_id = worker_id

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
        if not isinstance(other, SyncJobWorker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
