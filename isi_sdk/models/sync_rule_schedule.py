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


class SyncRuleSchedule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SyncRuleSchedule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'begin': 'str',
            'end': 'str',
            'friday': 'bool',
            'monday': 'bool',
            'saturday': 'bool',
            'sunday': 'bool',
            'thursday': 'bool',
            'tuesday': 'bool',
            'wednesday': 'bool'
        }

        self.attribute_map = {
            'begin': 'begin',
            'end': 'end',
            'friday': 'friday',
            'monday': 'monday',
            'saturday': 'saturday',
            'sunday': 'sunday',
            'thursday': 'thursday',
            'tuesday': 'tuesday',
            'wednesday': 'wednesday'
        }

        self._begin = None
        self._end = None
        self._friday = None
        self._monday = None
        self._saturday = None
        self._sunday = None
        self._thursday = None
        self._tuesday = None
        self._wednesday = None

    @property
    def begin(self):
        """
        Gets the begin of this SyncRuleSchedule.
        Start time (inclusive) for this schedule, during its specified days.  Format is \"hh:mm\" (24h format hour, and minute).  A null value indicates the beginning of the day (\"00:00\").

        :return: The begin of this SyncRuleSchedule.
        :rtype: str
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """
        Sets the begin of this SyncRuleSchedule.
        Start time (inclusive) for this schedule, during its specified days.  Format is \"hh:mm\" (24h format hour, and minute).  A null value indicates the beginning of the day (\"00:00\").

        :param begin: The begin of this SyncRuleSchedule.
        :type: str
        """
        self._begin = begin

    @property
    def end(self):
        """
        Gets the end of this SyncRuleSchedule.
        End time (inclusive) for this schedule, during its specified days.  Format is \"hh:mm\" (three-letter weekday name abbreviation, 24h format hour, and minute).  A null value indicates the end of the day (\"23:59\").

        :return: The end of this SyncRuleSchedule.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this SyncRuleSchedule.
        End time (inclusive) for this schedule, during its specified days.  Format is \"hh:mm\" (three-letter weekday name abbreviation, 24h format hour, and minute).  A null value indicates the end of the day (\"23:59\").

        :param end: The end of this SyncRuleSchedule.
        :type: str
        """
        self._end = end

    @property
    def friday(self):
        """
        Gets the friday of this SyncRuleSchedule.
        If true, this rule is in effect on Friday.  If false, or unspecified, it is not.

        :return: The friday of this SyncRuleSchedule.
        :rtype: bool
        """
        return self._friday

    @friday.setter
    def friday(self, friday):
        """
        Sets the friday of this SyncRuleSchedule.
        If true, this rule is in effect on Friday.  If false, or unspecified, it is not.

        :param friday: The friday of this SyncRuleSchedule.
        :type: bool
        """
        self._friday = friday

    @property
    def monday(self):
        """
        Gets the monday of this SyncRuleSchedule.
        If true, this rule is in effect on Monday.  If false, or unspecified, it is not.

        :return: The monday of this SyncRuleSchedule.
        :rtype: bool
        """
        return self._monday

    @monday.setter
    def monday(self, monday):
        """
        Sets the monday of this SyncRuleSchedule.
        If true, this rule is in effect on Monday.  If false, or unspecified, it is not.

        :param monday: The monday of this SyncRuleSchedule.
        :type: bool
        """
        self._monday = monday

    @property
    def saturday(self):
        """
        Gets the saturday of this SyncRuleSchedule.
        If true, this rule is in effect on Saturday.  If false, or unspecified, it is not.

        :return: The saturday of this SyncRuleSchedule.
        :rtype: bool
        """
        return self._saturday

    @saturday.setter
    def saturday(self, saturday):
        """
        Sets the saturday of this SyncRuleSchedule.
        If true, this rule is in effect on Saturday.  If false, or unspecified, it is not.

        :param saturday: The saturday of this SyncRuleSchedule.
        :type: bool
        """
        self._saturday = saturday

    @property
    def sunday(self):
        """
        Gets the sunday of this SyncRuleSchedule.
        If true, this rule is in effect on Sunday.  If false, or unspecified, it is not.

        :return: The sunday of this SyncRuleSchedule.
        :rtype: bool
        """
        return self._sunday

    @sunday.setter
    def sunday(self, sunday):
        """
        Sets the sunday of this SyncRuleSchedule.
        If true, this rule is in effect on Sunday.  If false, or unspecified, it is not.

        :param sunday: The sunday of this SyncRuleSchedule.
        :type: bool
        """
        self._sunday = sunday

    @property
    def thursday(self):
        """
        Gets the thursday of this SyncRuleSchedule.
        If true, this rule is in effect on Thursday.  If false, or unspecified, it is not.

        :return: The thursday of this SyncRuleSchedule.
        :rtype: bool
        """
        return self._thursday

    @thursday.setter
    def thursday(self, thursday):
        """
        Sets the thursday of this SyncRuleSchedule.
        If true, this rule is in effect on Thursday.  If false, or unspecified, it is not.

        :param thursday: The thursday of this SyncRuleSchedule.
        :type: bool
        """
        self._thursday = thursday

    @property
    def tuesday(self):
        """
        Gets the tuesday of this SyncRuleSchedule.
        If true, this rule is in effect on Tuesday.  If false, or unspecified, it is not.

        :return: The tuesday of this SyncRuleSchedule.
        :rtype: bool
        """
        return self._tuesday

    @tuesday.setter
    def tuesday(self, tuesday):
        """
        Sets the tuesday of this SyncRuleSchedule.
        If true, this rule is in effect on Tuesday.  If false, or unspecified, it is not.

        :param tuesday: The tuesday of this SyncRuleSchedule.
        :type: bool
        """
        self._tuesday = tuesday

    @property
    def wednesday(self):
        """
        Gets the wednesday of this SyncRuleSchedule.
        If true, this rule is in effect on Wednesday.  If false, or unspecified, it is not.

        :return: The wednesday of this SyncRuleSchedule.
        :rtype: bool
        """
        return self._wednesday

    @wednesday.setter
    def wednesday(self, wednesday):
        """
        Sets the wednesday of this SyncRuleSchedule.
        If true, this rule is in effect on Wednesday.  If false, or unspecified, it is not.

        :param wednesday: The wednesday of this SyncRuleSchedule.
        :type: bool
        """
        self._wednesday = wednesday

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

