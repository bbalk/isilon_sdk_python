# coding: utf-8

"""
Copyright 2015 SmartBear Software

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


class SyncJobCreateParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SyncJobCreateParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'log_level': 'str',
            'action': 'str',
            'state': 'str',
            'id': 'str',
            'source_snapshot': 'str',
            'workers_per_node': 'int'
        }

        self.attribute_map = {
            'log_level': 'log_level',
            'action': 'action',
            'state': 'state',
            'id': 'id',
            'source_snapshot': 'source_snapshot',
            'workers_per_node': 'workers_per_node'
        }

        self._log_level = None
        self._action = None
        self._state = None
        self._id = None
        self._source_snapshot = None
        self._workers_per_node = None

    @property
    def log_level(self):
        """
        Gets the log_level of this SyncJobCreateParams.
        Only valid for allow_write, and allow_write_revert; specify the desired logging level, will be stored in the logs for isi_migrate, defaults to 'info'.

        :return: The log_level of this SyncJobCreateParams.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """
        Sets the log_level of this SyncJobCreateParams.
        Only valid for allow_write, and allow_write_revert; specify the desired logging level, will be stored in the logs for isi_migrate, defaults to 'info'.

        :param log_level: The log_level of this SyncJobCreateParams.
        :type: str
        """
        allowed_values = ["fatal", "error", "notice", "info", "copy", "debug", "trace"]
        if log_level not in allowed_values:
            raise ValueError(
                "Invalid value for `log_level`, must be one of {0}"
                .format(allowed_values)
            )
        self._log_level = log_level

    @property
    def action(self):
        """
        Gets the action of this SyncJobCreateParams.
        The action to be taken by this job.

        :return: The action of this SyncJobCreateParams.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this SyncJobCreateParams.
        The action to be taken by this job.

        :param action: The action of this SyncJobCreateParams.
        :type: str
        """
        allowed_values = ["resync_prep", "allow_write", "allow_write_revert", "test"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action`, must be one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def state(self):
        """
        Gets the state of this SyncJobCreateParams.
        The state of the job.

        :return: The state of this SyncJobCreateParams.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this SyncJobCreateParams.
        The state of the job.

        :param state: The state of this SyncJobCreateParams.
        :type: str
        """
        allowed_values = ["canceled", "running", "paused"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def id(self):
        """
        Gets the id of this SyncJobCreateParams.
        The ID or Name of the policy

        :return: The id of this SyncJobCreateParams.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SyncJobCreateParams.
        The ID or Name of the policy

        :param id: The id of this SyncJobCreateParams.
        :type: str
        """
        self._id = id

    @property
    def source_snapshot(self):
        """
        Gets the source_snapshot of this SyncJobCreateParams.
        An optional snapshot to copy/sync from.

        :return: The source_snapshot of this SyncJobCreateParams.
        :rtype: str
        """
        return self._source_snapshot

    @source_snapshot.setter
    def source_snapshot(self, source_snapshot):
        """
        Sets the source_snapshot of this SyncJobCreateParams.
        An optional snapshot to copy/sync from.

        :param source_snapshot: The source_snapshot of this SyncJobCreateParams.
        :type: str
        """
        self._source_snapshot = source_snapshot

    @property
    def workers_per_node(self):
        """
        Gets the workers_per_node of this SyncJobCreateParams.
        Only valid for allow_write, and allow_write_revert; specify the desired workers per node, defaults to 3.

        :return: The workers_per_node of this SyncJobCreateParams.
        :rtype: int
        """
        return self._workers_per_node

    @workers_per_node.setter
    def workers_per_node(self, workers_per_node):
        """
        Sets the workers_per_node of this SyncJobCreateParams.
        Only valid for allow_write, and allow_write_revert; specify the desired workers per node, defaults to 3.

        :param workers_per_node: The workers_per_node of this SyncJobCreateParams.
        :type: int
        """
        self._workers_per_node = workers_per_node

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

