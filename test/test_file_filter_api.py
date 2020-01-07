# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_2_1
from isi_sdk_8_2_1.api.file_filter_api import FileFilterApi  # noqa: E501
from isi_sdk_8_2_1.rest import ApiException


class TestFileFilterApi(unittest.TestCase):
    """FileFilterApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_1.api.file_filter_api.FileFilterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_file_filter_settings(self):
        """Test case for get_file_filter_settings

        """
        pass

    def test_update_file_filter_settings(self):
        """Test case for update_file_filter_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
