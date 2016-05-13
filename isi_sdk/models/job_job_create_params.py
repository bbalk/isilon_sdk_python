# coding: utf-8

"""
Copyright 2016 SmartBear Software

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
import re


class JobJobCreateParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JobJobCreateParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allow_dup': 'bool',
            'avscan_params': 'JobJobAvscanParams',
            'changelistcreate_params': 'JobJobChangelistcreateParams',
            'domainmark_params': 'JobJobDomainmarkParams',
            'paths': 'list[str]',
            'policy': 'str',
            'prepair_params': 'JobJobPrepairParams',
            'priority': 'int',
            'smartpoolstree_params': 'JobJobSmartpoolstreeParams',
            'snaprevert_params': 'JobJobSnaprevertParams',
            'type': 'str'
        }

        self.attribute_map = {
            'allow_dup': 'allow_dup',
            'avscan_params': 'avscan_params',
            'changelistcreate_params': 'changelistcreate_params',
            'domainmark_params': 'domainmark_params',
            'paths': 'paths',
            'policy': 'policy',
            'prepair_params': 'prepair_params',
            'priority': 'priority',
            'smartpoolstree_params': 'smartpoolstree_params',
            'snaprevert_params': 'snaprevert_params',
            'type': 'type'
        }

        self._allow_dup = None
        self._avscan_params = None
        self._changelistcreate_params = None
        self._domainmark_params = None
        self._paths = None
        self._policy = None
        self._prepair_params = None
        self._priority = None
        self._smartpoolstree_params = None
        self._snaprevert_params = None
        self._type = None

    @property
    def allow_dup(self):
        """
        Gets the allow_dup of this JobJobCreateParams.
        Whether or not to queue the job if one of the same type is already running or queued.

        :return: The allow_dup of this JobJobCreateParams.
        :rtype: bool
        """
        return self._allow_dup

    @allow_dup.setter
    def allow_dup(self, allow_dup):
        """
        Sets the allow_dup of this JobJobCreateParams.
        Whether or not to queue the job if one of the same type is already running or queued.

        :param allow_dup: The allow_dup of this JobJobCreateParams.
        :type: bool
        """
        
        self._allow_dup = allow_dup

    @property
    def avscan_params(self):
        """
        Gets the avscan_params of this JobJobCreateParams.
        

        :return: The avscan_params of this JobJobCreateParams.
        :rtype: JobJobAvscanParams
        """
        return self._avscan_params

    @avscan_params.setter
    def avscan_params(self, avscan_params):
        """
        Sets the avscan_params of this JobJobCreateParams.
        

        :param avscan_params: The avscan_params of this JobJobCreateParams.
        :type: JobJobAvscanParams
        """
        
        self._avscan_params = avscan_params

    @property
    def changelistcreate_params(self):
        """
        Gets the changelistcreate_params of this JobJobCreateParams.
        

        :return: The changelistcreate_params of this JobJobCreateParams.
        :rtype: JobJobChangelistcreateParams
        """
        return self._changelistcreate_params

    @changelistcreate_params.setter
    def changelistcreate_params(self, changelistcreate_params):
        """
        Sets the changelistcreate_params of this JobJobCreateParams.
        

        :param changelistcreate_params: The changelistcreate_params of this JobJobCreateParams.
        :type: JobJobChangelistcreateParams
        """
        
        self._changelistcreate_params = changelistcreate_params

    @property
    def domainmark_params(self):
        """
        Gets the domainmark_params of this JobJobCreateParams.
        

        :return: The domainmark_params of this JobJobCreateParams.
        :rtype: JobJobDomainmarkParams
        """
        return self._domainmark_params

    @domainmark_params.setter
    def domainmark_params(self, domainmark_params):
        """
        Sets the domainmark_params of this JobJobCreateParams.
        

        :param domainmark_params: The domainmark_params of this JobJobCreateParams.
        :type: JobJobDomainmarkParams
        """
        
        self._domainmark_params = domainmark_params

    @property
    def paths(self):
        """
        Gets the paths of this JobJobCreateParams.
        For jobs which take paths, the IFS paths to pass to the job.

        :return: The paths of this JobJobCreateParams.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """
        Sets the paths of this JobJobCreateParams.
        For jobs which take paths, the IFS paths to pass to the job.

        :param paths: The paths of this JobJobCreateParams.
        :type: list[str]
        """
        
        self._paths = paths

    @property
    def policy(self):
        """
        Gets the policy of this JobJobCreateParams.
        Impact policy of this job instance.

        :return: The policy of this JobJobCreateParams.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this JobJobCreateParams.
        Impact policy of this job instance.

        :param policy: The policy of this JobJobCreateParams.
        :type: str
        """
        
        self._policy = policy

    @property
    def prepair_params(self):
        """
        Gets the prepair_params of this JobJobCreateParams.
        

        :return: The prepair_params of this JobJobCreateParams.
        :rtype: JobJobPrepairParams
        """
        return self._prepair_params

    @prepair_params.setter
    def prepair_params(self, prepair_params):
        """
        Sets the prepair_params of this JobJobCreateParams.
        

        :param prepair_params: The prepair_params of this JobJobCreateParams.
        :type: JobJobPrepairParams
        """
        
        self._prepair_params = prepair_params

    @property
    def priority(self):
        """
        Gets the priority of this JobJobCreateParams.
        Priority of this job instance; lower numbers preempt higher numbers.

        :return: The priority of this JobJobCreateParams.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this JobJobCreateParams.
        Priority of this job instance; lower numbers preempt higher numbers.

        :param priority: The priority of this JobJobCreateParams.
        :type: int
        """
        
        if not priority:
            raise ValueError("Invalid value for `priority`, must not be `None`")
        if priority > 10.0: 
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `10.0`")
        if priority < 1.0: 
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `1.0`")

        self._priority = priority

    @property
    def smartpoolstree_params(self):
        """
        Gets the smartpoolstree_params of this JobJobCreateParams.
        

        :return: The smartpoolstree_params of this JobJobCreateParams.
        :rtype: JobJobSmartpoolstreeParams
        """
        return self._smartpoolstree_params

    @smartpoolstree_params.setter
    def smartpoolstree_params(self, smartpoolstree_params):
        """
        Sets the smartpoolstree_params of this JobJobCreateParams.
        

        :param smartpoolstree_params: The smartpoolstree_params of this JobJobCreateParams.
        :type: JobJobSmartpoolstreeParams
        """
        
        self._smartpoolstree_params = smartpoolstree_params

    @property
    def snaprevert_params(self):
        """
        Gets the snaprevert_params of this JobJobCreateParams.
        

        :return: The snaprevert_params of this JobJobCreateParams.
        :rtype: JobJobSnaprevertParams
        """
        return self._snaprevert_params

    @snaprevert_params.setter
    def snaprevert_params(self, snaprevert_params):
        """
        Sets the snaprevert_params of this JobJobCreateParams.
        

        :param snaprevert_params: The snaprevert_params of this JobJobCreateParams.
        :type: JobJobSnaprevertParams
        """
        
        self._snaprevert_params = snaprevert_params

    @property
    def type(self):
        """
        Gets the type of this JobJobCreateParams.
        Job type to queue.

        :return: The type of this JobJobCreateParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this JobJobCreateParams.
        Job type to queue.

        :param type: The type of this JobJobCreateParams.
        :type: str
        """
        
        self._type = type

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

