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


class NdmpContextsBackupSession(object):
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
        'bre_context_id': 'str',
        'session_id': 'str',
        'start_time': 'int',
        'status': 'str',
        'stream_id': 'str'
    }

    attribute_map = {
        'bre_context_id': 'bre_context_id',
        'session_id': 'session_id',
        'start_time': 'start_time',
        'status': 'status',
        'stream_id': 'stream_id'
    }

    def __init__(self, bre_context_id=None, session_id=None, start_time=None, status=None, stream_id=None):  # noqa: E501
        """NdmpContextsBackupSession - a model defined in Swagger"""  # noqa: E501

        self._bre_context_id = None
        self._session_id = None
        self._start_time = None
        self._status = None
        self._stream_id = None
        self.discriminator = None

        if bre_context_id is not None:
            self.bre_context_id = bre_context_id
        if session_id is not None:
            self.session_id = session_id
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if stream_id is not None:
            self.stream_id = stream_id

    @property
    def bre_context_id(self):
        """Gets the bre_context_id of this NdmpContextsBackupSession.  # noqa: E501

        bre context id; This is not applicable to restore sessions.  # noqa: E501

        :return: The bre_context_id of this NdmpContextsBackupSession.  # noqa: E501
        :rtype: str
        """
        return self._bre_context_id

    @bre_context_id.setter
    def bre_context_id(self, bre_context_id):
        """Sets the bre_context_id of this NdmpContextsBackupSession.

        bre context id; This is not applicable to restore sessions.  # noqa: E501

        :param bre_context_id: The bre_context_id of this NdmpContextsBackupSession.  # noqa: E501
        :type: str
        """

        self._bre_context_id = bre_context_id

    @property
    def session_id(self):
        """Gets the session_id of this NdmpContextsBackupSession.  # noqa: E501

        Session ID  # noqa: E501

        :return: The session_id of this NdmpContextsBackupSession.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this NdmpContextsBackupSession.

        Session ID  # noqa: E501

        :param session_id: The session_id of this NdmpContextsBackupSession.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def start_time(self):
        """Gets the start_time of this NdmpContextsBackupSession.  # noqa: E501

        Session creation time  # noqa: E501

        :return: The start_time of this NdmpContextsBackupSession.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this NdmpContextsBackupSession.

        Session creation time  # noqa: E501

        :param start_time: The start_time of this NdmpContextsBackupSession.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this NdmpContextsBackupSession.  # noqa: E501

        The status of the session  # noqa: E501

        :return: The status of this NdmpContextsBackupSession.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NdmpContextsBackupSession.

        The status of the session  # noqa: E501

        :param status: The status of this NdmpContextsBackupSession.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def stream_id(self):
        """Gets the stream_id of this NdmpContextsBackupSession.  # noqa: E501

        Stream ID  # noqa: E501

        :return: The stream_id of this NdmpContextsBackupSession.  # noqa: E501
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this NdmpContextsBackupSession.

        Stream ID  # noqa: E501

        :param stream_id: The stream_id of this NdmpContextsBackupSession.  # noqa: E501
        :type: str
        """

        self._stream_id = stream_id

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
        if issubclass(NdmpContextsBackupSession, dict):
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
        if not isinstance(other, NdmpContextsBackupSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
