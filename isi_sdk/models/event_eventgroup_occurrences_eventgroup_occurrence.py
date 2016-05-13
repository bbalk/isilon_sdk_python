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


class EventEventgroupOccurrencesEventgroupOccurrence(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EventEventgroupOccurrencesEventgroupOccurrence - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'causes': 'list[ERRORUNKNOWN]',
            'channels': 'list[str]',
            'event_count': 'int',
            'eventgroup_instance': 'str',
            'id': 'str',
            'ignore': 'bool',
            'ignore_time': 'int',
            'last_event': 'int',
            'resolve_time': 'int',
            'resolved': 'bool',
            'resolver': 'str',
            'sequence': 'int',
            'severity': 'str',
            'specifier': 'Empty',
            'time_noticed': 'int'
        }

        self.attribute_map = {
            'causes': 'causes',
            'channels': 'channels',
            'event_count': 'event_count',
            'eventgroup_instance': 'eventgroup_instance',
            'id': 'id',
            'ignore': 'ignore',
            'ignore_time': 'ignore_time',
            'last_event': 'last_event',
            'resolve_time': 'resolve_time',
            'resolved': 'resolved',
            'resolver': 'resolver',
            'sequence': 'sequence',
            'severity': 'severity',
            'specifier': 'specifier',
            'time_noticed': 'time_noticed'
        }

        self._causes = None
        self._channels = None
        self._event_count = None
        self._eventgroup_instance = None
        self._id = None
        self._ignore = None
        self._ignore_time = None
        self._last_event = None
        self._resolve_time = None
        self._resolved = None
        self._resolver = None
        self._sequence = None
        self._severity = None
        self._specifier = None
        self._time_noticed = None

    @property
    def causes(self):
        """
        Gets the causes of this EventEventgroupOccurrencesEventgroupOccurrence.
        List of eventgroup IDs that may be causes of this occurrence.

        :return: The causes of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: list[ERRORUNKNOWN]
        """
        return self._causes

    @causes.setter
    def causes(self, causes):
        """
        Sets the causes of this EventEventgroupOccurrencesEventgroupOccurrence.
        List of eventgroup IDs that may be causes of this occurrence.

        :param causes: The causes of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: list[ERRORUNKNOWN]
        """
        
        self._causes = causes

    @property
    def channels(self):
        """
        Gets the channels of this EventEventgroupOccurrencesEventgroupOccurrence.
        List of channels to which alerts are configured for this eventgroup

        :return: The channels of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """
        Sets the channels of this EventEventgroupOccurrencesEventgroupOccurrence.
        List of channels to which alerts are configured for this eventgroup

        :param channels: The channels of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: list[str]
        """
        
        self._channels = channels

    @property
    def event_count(self):
        """
        Gets the event_count of this EventEventgroupOccurrencesEventgroupOccurrence.
        Number of events linked to this eventgroup.

        :return: The event_count of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: int
        """
        return self._event_count

    @event_count.setter
    def event_count(self, event_count):
        """
        Sets the event_count of this EventEventgroupOccurrencesEventgroupOccurrence.
        Number of events linked to this eventgroup.

        :param event_count: The event_count of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: int
        """
        
        self._event_count = event_count

    @property
    def eventgroup_instance(self):
        """
        Gets the eventgroup_instance of this EventEventgroupOccurrencesEventgroupOccurrence.
        Unique identifier of eventgroup instance.

        :return: The eventgroup_instance of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: str
        """
        return self._eventgroup_instance

    @eventgroup_instance.setter
    def eventgroup_instance(self, eventgroup_instance):
        """
        Sets the eventgroup_instance of this EventEventgroupOccurrencesEventgroupOccurrence.
        Unique identifier of eventgroup instance.

        :param eventgroup_instance: The eventgroup_instance of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: str
        """
        
        self._eventgroup_instance = eventgroup_instance

    @property
    def id(self):
        """
        Gets the id of this EventEventgroupOccurrencesEventgroupOccurrence.
        Same as eventgroup_instance.

        :return: The id of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EventEventgroupOccurrencesEventgroupOccurrence.
        Same as eventgroup_instance.

        :param id: The id of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: str
        """
        
        self._id = id

    @property
    def ignore(self):
        """
        Gets the ignore of this EventEventgroupOccurrencesEventgroupOccurrence.
        True if eventgroup is marked as 'ignore'.

        :return: The ignore of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: bool
        """
        return self._ignore

    @ignore.setter
    def ignore(self, ignore):
        """
        Sets the ignore of this EventEventgroupOccurrencesEventgroupOccurrence.
        True if eventgroup is marked as 'ignore'.

        :param ignore: The ignore of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: bool
        """
        
        self._ignore = ignore

    @property
    def ignore_time(self):
        """
        Gets the ignore_time of this EventEventgroupOccurrencesEventgroupOccurrence.
        Time eventgroup was marked as 'ignore'.

        :return: The ignore_time of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: int
        """
        return self._ignore_time

    @ignore_time.setter
    def ignore_time(self, ignore_time):
        """
        Sets the ignore_time of this EventEventgroupOccurrencesEventgroupOccurrence.
        Time eventgroup was marked as 'ignore'.

        :param ignore_time: The ignore_time of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: int
        """
        
        self._ignore_time = ignore_time

    @property
    def last_event(self):
        """
        Gets the last_event of this EventEventgroupOccurrencesEventgroupOccurrence.
        Time the most recent event was added to this eventgroup.

        :return: The last_event of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: int
        """
        return self._last_event

    @last_event.setter
    def last_event(self, last_event):
        """
        Sets the last_event of this EventEventgroupOccurrencesEventgroupOccurrence.
        Time the most recent event was added to this eventgroup.

        :param last_event: The last_event of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: int
        """
        
        self._last_event = last_event

    @property
    def resolve_time(self):
        """
        Gets the resolve_time of this EventEventgroupOccurrencesEventgroupOccurrence.
        When the eventgroup became resolved.

        :return: The resolve_time of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: int
        """
        return self._resolve_time

    @resolve_time.setter
    def resolve_time(self, resolve_time):
        """
        Sets the resolve_time of this EventEventgroupOccurrencesEventgroupOccurrence.
        When the eventgroup became resolved.

        :param resolve_time: The resolve_time of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: int
        """
        
        self._resolve_time = resolve_time

    @property
    def resolved(self):
        """
        Gets the resolved of this EventEventgroupOccurrencesEventgroupOccurrence.
        True if eventgroup is resolved.

        :return: The resolved of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """
        Sets the resolved of this EventEventgroupOccurrencesEventgroupOccurrence.
        True if eventgroup is resolved.

        :param resolved: The resolved of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: bool
        """
        
        self._resolved = resolved

    @property
    def resolver(self):
        """
        Gets the resolver of this EventEventgroupOccurrencesEventgroupOccurrence.
        'USER' if the eventgroup was marked resolved via PAPI <event_instance> if eventgroup was marked resolved as a result of an event.

        :return: The resolver of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: str
        """
        return self._resolver

    @resolver.setter
    def resolver(self, resolver):
        """
        Sets the resolver of this EventEventgroupOccurrencesEventgroupOccurrence.
        'USER' if the eventgroup was marked resolved via PAPI <event_instance> if eventgroup was marked resolved as a result of an event.

        :param resolver: The resolver of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: str
        """
        
        self._resolver = resolver

    @property
    def sequence(self):
        """
        Gets the sequence of this EventEventgroupOccurrencesEventgroupOccurrence.
        XXX description needed.

        :return: The sequence of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """
        Sets the sequence of this EventEventgroupOccurrencesEventgroupOccurrence.
        XXX description needed.

        :param sequence: The sequence of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: int
        """
        
        self._sequence = sequence

    @property
    def severity(self):
        """
        Gets the severity of this EventEventgroupOccurrencesEventgroupOccurrence.
        Event Group severity.

        :return: The severity of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this EventEventgroupOccurrencesEventgroupOccurrence.
        Event Group severity.

        :param severity: The severity of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: str
        """
        
        self._severity = severity

    @property
    def specifier(self):
        """
        Gets the specifier of this EventEventgroupOccurrencesEventgroupOccurrence.
        A collection of parameters defined per eventgroup_id.

        :return: The specifier of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: Empty
        """
        return self._specifier

    @specifier.setter
    def specifier(self, specifier):
        """
        Sets the specifier of this EventEventgroupOccurrencesEventgroupOccurrence.
        A collection of parameters defined per eventgroup_id.

        :param specifier: The specifier of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: Empty
        """
        
        self._specifier = specifier

    @property
    def time_noticed(self):
        """
        Gets the time_noticed of this EventEventgroupOccurrencesEventgroupOccurrence.
        Time of first event linked to this eventgroup.

        :return: The time_noticed of this EventEventgroupOccurrencesEventgroupOccurrence.
        :rtype: int
        """
        return self._time_noticed

    @time_noticed.setter
    def time_noticed(self, time_noticed):
        """
        Sets the time_noticed of this EventEventgroupOccurrencesEventgroupOccurrence.
        Time of first event linked to this eventgroup.

        :param time_noticed: The time_noticed of this EventEventgroupOccurrencesEventgroupOccurrence.
        :type: int
        """
        
        self._time_noticed = time_noticed

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

