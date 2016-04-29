# coding: utf-8

"""
HardwareApi.py
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
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class HardwareApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_hardware_fcport(self, hardware_fcport_id, **kwargs):
        """
        
        Get one fibre-channel port

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hardware_fcport(hardware_fcport_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int hardware_fcport_id: Get one fibre-channel port (required)
        :return: HardwareFcports
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_fcport_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hardware_fcport" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'hardware_fcport_id' is set
        if ('hardware_fcport_id' not in params) or (params['hardware_fcport_id'] is None):
            raise ValueError("Missing the required parameter `hardware_fcport_id` when calling `get_hardware_fcport`")

        resource_path = '/platform/3/hardware/fcports/{HardwareFcportId}'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        if 'hardware_fcport_id' in params:
            path_params['HardwareFcportId'] = params['hardware_fcport_id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='HardwareFcports',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_hardware_fcport(self, hardware_fcport, hardware_fcport_id, **kwargs):
        """
        
        Change wwnn, wwpn, state, topology, or rate of a FC port

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_hardware_fcport(hardware_fcport, hardware_fcport_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param HardwareFcport hardware_fcport:  (required)
        :param int hardware_fcport_id: Change wwnn, wwpn, state, topology, or rate of a FC port (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_fcport', 'hardware_fcport_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_hardware_fcport" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'hardware_fcport' is set
        if ('hardware_fcport' not in params) or (params['hardware_fcport'] is None):
            raise ValueError("Missing the required parameter `hardware_fcport` when calling `update_hardware_fcport`")
        # verify the required parameter 'hardware_fcport_id' is set
        if ('hardware_fcport_id' not in params) or (params['hardware_fcport_id'] is None):
            raise ValueError("Missing the required parameter `hardware_fcport_id` when calling `update_hardware_fcport`")

        resource_path = '/platform/3/hardware/fcports/{HardwareFcportId}'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        if 'hardware_fcport_id' in params:
            path_params['HardwareFcportId'] = params['hardware_fcport_id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None
        if 'hardware_fcport' in params:
            body_params = params['hardware_fcport']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_hardware_tape_name(self, hardware_tape_name_params, hardware_tape_name, **kwargs):
        """
        
        Tape/Changer device modify

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_hardware_tape_name(hardware_tape_name_params, hardware_tape_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param HardwareTapeNameParams hardware_tape_name_params:  (required)
        :param str hardware_tape_name: Tape/Changer device modify (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_tape_name_params', 'hardware_tape_name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_hardware_tape_name" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'hardware_tape_name_params' is set
        if ('hardware_tape_name_params' not in params) or (params['hardware_tape_name_params'] is None):
            raise ValueError("Missing the required parameter `hardware_tape_name_params` when calling `update_hardware_tape_name`")
        # verify the required parameter 'hardware_tape_name' is set
        if ('hardware_tape_name' not in params) or (params['hardware_tape_name'] is None):
            raise ValueError("Missing the required parameter `hardware_tape_name` when calling `update_hardware_tape_name`")

        resource_path = '/platform/3/hardware/tape/{HardwareTapeName}'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        if 'hardware_tape_name' in params:
            path_params['HardwareTapeName'] = params['hardware_tape_name']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None
        if 'hardware_tape_name_params' in params:
            body_params = params['hardware_tape_name_params']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def create_hardware_tape_name(self, hardware_tape_name, **kwargs):
        """
        
        Tape/Changer devices rescan

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_hardware_tape_name(hardware_tape_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Empty hardware_tape_name:  (required)
        :return: Empty
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_tape_name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_hardware_tape_name" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'hardware_tape_name' is set
        if ('hardware_tape_name' not in params) or (params['hardware_tape_name'] is None):
            raise ValueError("Missing the required parameter `hardware_tape_name` when calling `create_hardware_tape_name`")

        resource_path = '/platform/3/hardware/tape/{HardwareTapeName}'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None
        if 'hardware_tape_name' in params:
            body_params = params['hardware_tape_name']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='Empty',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_hardware_tape_name(self, hardware_tape_name, **kwargs):
        """
        
        Tape/Changer devices remove

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_hardware_tape_name(hardware_tape_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str hardware_tape_name: Tape/Changer devices remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['hardware_tape_name']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_hardware_tape_name" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'hardware_tape_name' is set
        if ('hardware_tape_name' not in params) or (params['hardware_tape_name'] is None):
            raise ValueError("Missing the required parameter `hardware_tape_name` when calling `delete_hardware_tape_name`")

        resource_path = '/platform/3/hardware/tape/{HardwareTapeName}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        if 'hardware_tape_name' in params:
            path_params['HardwareTapeName'] = params['hardware_tape_name']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_hardware_tapes(self, **kwargs):
        """
        
        Get list Tape and Changer devices

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_hardware_tapes(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: HardwareTapes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_hardware_tapes" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/platform/3/hardware/tapes'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='HardwareTapes',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
