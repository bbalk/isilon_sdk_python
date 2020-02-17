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


class SnapshotChangelists(object):
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
        'id': 'str',
        'job_id': 'int',
        'num_entries': 'int',
        'root_path': 'str',
        'snap1': 'int',
        'snap2': 'int',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'job_id': 'job_id',
        'num_entries': 'num_entries',
        'root_path': 'root_path',
        'snap1': 'snap1',
        'snap2': 'snap2',
        'status': 'status'
    }

    def __init__(self, id=None, job_id=None, num_entries=None, root_path=None, snap1=None, snap2=None, status=None):  # noqa: E501
        """SnapshotChangelists - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._job_id = None
        self._num_entries = None
        self._root_path = None
        self._snap1 = None
        self._snap2 = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.job_id = job_id
        if num_entries is not None:
            self.num_entries = num_entries
        self.root_path = root_path
        self.snap1 = snap1
        self.snap2 = snap2
        self.status = status

    @property
    def id(self):
        """Gets the id of this SnapshotChangelists.  # noqa: E501

        The system ID given to the changelist.  # noqa: E501

        :return: The id of this SnapshotChangelists.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotChangelists.

        The system ID given to the changelist.  # noqa: E501

        :param id: The id of this SnapshotChangelists.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def job_id(self):
        """Gets the job_id of this SnapshotChangelists.  # noqa: E501

        The ID of the job which created the changelist.  # noqa: E501

        :return: The job_id of this SnapshotChangelists.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this SnapshotChangelists.

        The ID of the job which created the changelist.  # noqa: E501

        :param job_id: The job_id of this SnapshotChangelists.  # noqa: E501
        :type: int
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501

        self._job_id = job_id

    @property
    def num_entries(self):
        """Gets the num_entries of this SnapshotChangelists.  # noqa: E501

        Number of LIN entries in changelist.  # noqa: E501

        :return: The num_entries of this SnapshotChangelists.  # noqa: E501
        :rtype: int
        """
        return self._num_entries

    @num_entries.setter
    def num_entries(self, num_entries):
        """Sets the num_entries of this SnapshotChangelists.

        Number of LIN entries in changelist.  # noqa: E501

        :param num_entries: The num_entries of this SnapshotChangelists.  # noqa: E501
        :type: int
        """

        self._num_entries = num_entries

    @property
    def root_path(self):
        """Gets the root_path of this SnapshotChangelists.  # noqa: E501

        Root path of all LINs in changelist.  # noqa: E501

        :return: The root_path of this SnapshotChangelists.  # noqa: E501
        :rtype: str
        """
        return self._root_path

    @root_path.setter
    def root_path(self, root_path):
        """Sets the root_path of this SnapshotChangelists.

        Root path of all LINs in changelist.  # noqa: E501

        :param root_path: The root_path of this SnapshotChangelists.  # noqa: E501
        :type: str
        """
        if root_path is None:
            raise ValueError("Invalid value for `root_path`, must not be `None`")  # noqa: E501

        self._root_path = root_path

    @property
    def snap1(self):
        """Gets the snap1 of this SnapshotChangelists.  # noqa: E501

        The lower snapid used to compute the changelist.  # noqa: E501

        :return: The snap1 of this SnapshotChangelists.  # noqa: E501
        :rtype: int
        """
        return self._snap1

    @snap1.setter
    def snap1(self, snap1):
        """Sets the snap1 of this SnapshotChangelists.

        The lower snapid used to compute the changelist.  # noqa: E501

        :param snap1: The snap1 of this SnapshotChangelists.  # noqa: E501
        :type: int
        """
        if snap1 is None:
            raise ValueError("Invalid value for `snap1`, must not be `None`")  # noqa: E501

        self._snap1 = snap1

    @property
    def snap2(self):
        """Gets the snap2 of this SnapshotChangelists.  # noqa: E501

        The higher snapid used to compute the changelist.  # noqa: E501

        :return: The snap2 of this SnapshotChangelists.  # noqa: E501
        :rtype: int
        """
        return self._snap2

    @snap2.setter
    def snap2(self, snap2):
        """Sets the snap2 of this SnapshotChangelists.

        The higher snapid used to compute the changelist.  # noqa: E501

        :param snap2: The snap2 of this SnapshotChangelists.  # noqa: E501
        :type: int
        """
        if snap2 is None:
            raise ValueError("Invalid value for `snap2`, must not be `None`")  # noqa: E501

        self._snap2 = snap2

    @property
    def status(self):
        """Gets the status of this SnapshotChangelists.  # noqa: E501

        Status of changelist.  # noqa: E501

        :return: The status of this SnapshotChangelists.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SnapshotChangelists.

        Status of changelist.  # noqa: E501

        :param status: The status of this SnapshotChangelists.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(SnapshotChangelists, dict):
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
        if not isinstance(other, SnapshotChangelists):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
