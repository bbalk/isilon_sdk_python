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


class ClusterEmailExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterEmailExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'batch_mode': 'str',
            'mail_relay': 'str',
            'mail_sender': 'str',
            'mail_subject': 'str',
            'smtp_auth_passwd': 'str',
            'smtp_auth_security': 'str',
            'smtp_auth_username': 'str',
            'smtp_port': 'int',
            'use_smtp_auth': 'bool',
            'user_template': 'str'
        }

        self.attribute_map = {
            'batch_mode': 'batch_mode',
            'mail_relay': 'mail_relay',
            'mail_sender': 'mail_sender',
            'mail_subject': 'mail_subject',
            'smtp_auth_passwd': 'smtp_auth_passwd',
            'smtp_auth_security': 'smtp_auth_security',
            'smtp_auth_username': 'smtp_auth_username',
            'smtp_port': 'smtp_port',
            'use_smtp_auth': 'use_smtp_auth',
            'user_template': 'user_template'
        }

        self._batch_mode = None
        self._mail_relay = None
        self._mail_sender = None
        self._mail_subject = None
        self._smtp_auth_passwd = None
        self._smtp_auth_security = None
        self._smtp_auth_username = None
        self._smtp_port = None
        self._use_smtp_auth = None
        self._user_template = None

    @property
    def batch_mode(self):
        """
        Gets the batch_mode of this ClusterEmailExtended.
        This setting determines how notifications will be batched together to be sent by email.  'none' means each notification will be sent separately.  'severity' means notifications of the same severity will be sent together.  'category' means notifications of the same category will be sent together.  'all' means all notifications will be batched together and sent in a single email.

        :return: The batch_mode of this ClusterEmailExtended.
        :rtype: str
        """
        return self._batch_mode

    @batch_mode.setter
    def batch_mode(self, batch_mode):
        """
        Sets the batch_mode of this ClusterEmailExtended.
        This setting determines how notifications will be batched together to be sent by email.  'none' means each notification will be sent separately.  'severity' means notifications of the same severity will be sent together.  'category' means notifications of the same category will be sent together.  'all' means all notifications will be batched together and sent in a single email.

        :param batch_mode: The batch_mode of this ClusterEmailExtended.
        :type: str
        """
        allowed_values = ["all", "severity", "category", "none"]
        if batch_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `batch_mode`, must be one of {0}"
                .format(allowed_values)
            )

        self._batch_mode = batch_mode

    @property
    def mail_relay(self):
        """
        Gets the mail_relay of this ClusterEmailExtended.
        The address of the SMTP server to be used for relaying the notification messages.  An SMTP server is required in order to send notifications.  If this string is empty, no emails will be sent.

        :return: The mail_relay of this ClusterEmailExtended.
        :rtype: str
        """
        return self._mail_relay

    @mail_relay.setter
    def mail_relay(self, mail_relay):
        """
        Sets the mail_relay of this ClusterEmailExtended.
        The address of the SMTP server to be used for relaying the notification messages.  An SMTP server is required in order to send notifications.  If this string is empty, no emails will be sent.

        :param mail_relay: The mail_relay of this ClusterEmailExtended.
        :type: str
        """
        
        self._mail_relay = mail_relay

    @property
    def mail_sender(self):
        """
        Gets the mail_sender of this ClusterEmailExtended.
        The full email address that will appear as the sender of notification messages.

        :return: The mail_sender of this ClusterEmailExtended.
        :rtype: str
        """
        return self._mail_sender

    @mail_sender.setter
    def mail_sender(self, mail_sender):
        """
        Sets the mail_sender of this ClusterEmailExtended.
        The full email address that will appear as the sender of notification messages.

        :param mail_sender: The mail_sender of this ClusterEmailExtended.
        :type: str
        """
        
        self._mail_sender = mail_sender

    @property
    def mail_subject(self):
        """
        Gets the mail_subject of this ClusterEmailExtended.
        The subject line for notification messages from this cluster.

        :return: The mail_subject of this ClusterEmailExtended.
        :rtype: str
        """
        return self._mail_subject

    @mail_subject.setter
    def mail_subject(self, mail_subject):
        """
        Sets the mail_subject of this ClusterEmailExtended.
        The subject line for notification messages from this cluster.

        :param mail_subject: The mail_subject of this ClusterEmailExtended.
        :type: str
        """
        
        self._mail_subject = mail_subject

    @property
    def smtp_auth_passwd(self):
        """
        Gets the smtp_auth_passwd of this ClusterEmailExtended.
        Password to authenticate with if SMTP authentication is being used.

        :return: The smtp_auth_passwd of this ClusterEmailExtended.
        :rtype: str
        """
        return self._smtp_auth_passwd

    @smtp_auth_passwd.setter
    def smtp_auth_passwd(self, smtp_auth_passwd):
        """
        Sets the smtp_auth_passwd of this ClusterEmailExtended.
        Password to authenticate with if SMTP authentication is being used.

        :param smtp_auth_passwd: The smtp_auth_passwd of this ClusterEmailExtended.
        :type: str
        """
        
        self._smtp_auth_passwd = smtp_auth_passwd

    @property
    def smtp_auth_security(self):
        """
        Gets the smtp_auth_security of this ClusterEmailExtended.
        The type of secure communication protocol to use if SMTP is being used.  If 'none', plain text will be used, if 'starttls', the encrypted STARTTLS protocol will be used.

        :return: The smtp_auth_security of this ClusterEmailExtended.
        :rtype: str
        """
        return self._smtp_auth_security

    @smtp_auth_security.setter
    def smtp_auth_security(self, smtp_auth_security):
        """
        Sets the smtp_auth_security of this ClusterEmailExtended.
        The type of secure communication protocol to use if SMTP is being used.  If 'none', plain text will be used, if 'starttls', the encrypted STARTTLS protocol will be used.

        :param smtp_auth_security: The smtp_auth_security of this ClusterEmailExtended.
        :type: str
        """
        allowed_values = ["none", "starttls"]
        if smtp_auth_security not in allowed_values:
            raise ValueError(
                "Invalid value for `smtp_auth_security`, must be one of {0}"
                .format(allowed_values)
            )

        self._smtp_auth_security = smtp_auth_security

    @property
    def smtp_auth_username(self):
        """
        Gets the smtp_auth_username of this ClusterEmailExtended.
        Username to authenticate with if SMTP authentication is being used.

        :return: The smtp_auth_username of this ClusterEmailExtended.
        :rtype: str
        """
        return self._smtp_auth_username

    @smtp_auth_username.setter
    def smtp_auth_username(self, smtp_auth_username):
        """
        Sets the smtp_auth_username of this ClusterEmailExtended.
        Username to authenticate with if SMTP authentication is being used.

        :param smtp_auth_username: The smtp_auth_username of this ClusterEmailExtended.
        :type: str
        """
        
        self._smtp_auth_username = smtp_auth_username

    @property
    def smtp_port(self):
        """
        Gets the smtp_port of this ClusterEmailExtended.
        The port on the SMTP server to be used for relaying the notification messages.  

        :return: The smtp_port of this ClusterEmailExtended.
        :rtype: int
        """
        return self._smtp_port

    @smtp_port.setter
    def smtp_port(self, smtp_port):
        """
        Sets the smtp_port of this ClusterEmailExtended.
        The port on the SMTP server to be used for relaying the notification messages.  

        :param smtp_port: The smtp_port of this ClusterEmailExtended.
        :type: int
        """
        
        self._smtp_port = smtp_port

    @property
    def use_smtp_auth(self):
        """
        Gets the use_smtp_auth of this ClusterEmailExtended.
        If true, this cluster will send SMTP authentication credentials to the SMTP relay server in order to send its notification emails.  If false, the cluster will attempt to send its notification emails without authentication.

        :return: The use_smtp_auth of this ClusterEmailExtended.
        :rtype: bool
        """
        return self._use_smtp_auth

    @use_smtp_auth.setter
    def use_smtp_auth(self, use_smtp_auth):
        """
        Sets the use_smtp_auth of this ClusterEmailExtended.
        If true, this cluster will send SMTP authentication credentials to the SMTP relay server in order to send its notification emails.  If false, the cluster will attempt to send its notification emails without authentication.

        :param use_smtp_auth: The use_smtp_auth of this ClusterEmailExtended.
        :type: bool
        """
        
        self._use_smtp_auth = use_smtp_auth

    @property
    def user_template(self):
        """
        Gets the user_template of this ClusterEmailExtended.
        Location of a custom template file that can be used to specify the layout of the notification emails.

        :return: The user_template of this ClusterEmailExtended.
        :rtype: str
        """
        return self._user_template

    @user_template.setter
    def user_template(self, user_template):
        """
        Sets the user_template of this ClusterEmailExtended.
        Location of a custom template file that can be used to specify the layout of the notification emails.

        :param user_template: The user_template of this ClusterEmailExtended.
        :type: str
        """
        
        self._user_template = user_template

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

