#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
import unittest

from application.tests.flask_test import FlaskTestCase


class Auth(FlaskTestCase):
    def test_filter_status_get_list(self):
        """

        :return:
        """
        response = self._call('App.index')
        self.result = response['error']['message'] if 'error' in response.keys() else '...ok'
        self.assertFalse("error" in response.keys())
        self.assertTrue("result" in response.keys())

    def test_indexx(self):
        """

        :return:
        """
        response = self._call('App.indexx')
        self.result = response['error']['message'] if 'error' in response.keys() else '...ok'
        self.assertFalse("error" in response.keys())
        self.assertTrue("result" in response.keys())


if __name__ == '__main__':
    unittest.main()
