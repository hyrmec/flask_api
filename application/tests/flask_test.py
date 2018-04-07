#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikulshin

import sys

import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/../'))

import json
import unittest
import logging
from application import create_app, db, current_app
from utils.flask.decorators import flask_exceptions
from datetime import datetime
from config import Test


class FlaskTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        """Конструктор класса
        :param args: tuple
        :param kwargs: dict

        """

        app = create_app(Test)
        self.app = app.test_client(self)
        db.init_app(app)
        self.login = app.config.get('TEST_LOGIN')
        self.password = app.config.get('TEST_PASSWORD')
        self.is_subagent = app.config.get('TEST_IS_SUBAGENT')
        self.test_rollback = app.config.get('TEST_ROLLBACK')

        super(FlaskTestCase, self).__init__(*args, **kwargs)
        self.session_id = None
        self.www_uuid = None
        self.wizard_token = None

        if 'TESTS_DIRECTORY' in app.config:
            logging.basicConfig(format='%(message)s', filename='%s/test_%s.log' % (app.root_path + app.config['TESTS_DIRECTORY'], datetime.now().strftime('%y-%m-%d_%H-%M')))
        else:
            logging.basicConfig(format='%(message)s')

    def user_signin(self):
        """Авторизация пользователя
        :return: str

        """
        response = self._call('Session.signin', {"username": self.login, "password": self.password, "is_subagent": self.is_subagent})
        if 'error' in response and response['error']['code'] == 500:
            raise flask_exceptions.InvalidUsage(response['error']['stack'])
        return response["result"]["session_id"]

    def user_signout(self):
        """Завершение сессии
        :return: None

        """
        self.auth_call('Session.signout')

    def setUp(self):
        """setUp for test"""

        self.session_id = self.user_signin()
        self.www_uuid = 'b4b16ca2-f8d3-4791-9119-f2a6eb9b7e94'


    def _call(self, method, request_data=None):
        """Запрос к серверу
        :param method: str
        :param request_data: dict
        :return: dict

        """
        request_data = request_data or {}
        data = json.dumps({'id': '1', 'jsonrpc': '2.0', 'method': method, 'params': request_data})

        headers = {'Content-Type': 'application/json'}
        response = self.app.post("/api/v1", data=data, headers=headers)
        return json.loads(response.data.decode("UTF-8"))

    def auth_call(self, method, request_data=None):
        """Авторизованный запрос к серверу
        :param method: str
        :param request_data: dict
        :return: dict

        """
        request_data = request_data or {}
        data = json.dumps({'id': '1', 'jsonrpc': '2.0', 'method': method, 'params': request_data})

        headers = {'Content-Type': 'application/json', 'Authorization': 'WWWToken ' + self.session_id}
        if self.test_rollback:
            with self.app.app_context():
                db.session.begin_nested()
                response = self.app.post("/api/v1", data=data, headers=headers)
        else:
            response = self.app.post("/api/v1", data=data, headers=headers)
        return json.loads(response.data.decode("UTF-8"))

    def auth_uuid_call(self, method, request_data=None):
        """Авторизованный через uuid запрос к серверу
        :param method: str
        :param request_data: dict
        :return: dict

        """
        request_data = request_data or {}
        data = json.dumps({'id': '1', 'jsonrpc': '2.0', 'method': method, 'params': request_data})

        headers = {'Content-Type': 'application/json', 'Authorization': 'WWWUUID ' + self.www_uuid}
        if current_app.config.get('TEST_ROLLBACK'):
            with current_app.app_context():
                db.session.begin_nested()
                response = self.app.post("/api/v1", data=data, headers=headers)
        else:
            response = self.app.post("/api/v1", data=data, headers=headers)
        return json.loads(response.data.decode("UTF-8"))

    def auth_wizard_call(self, method, request_data=None):
        """Авторизованный через wizard запрос к серверу
        :param method: str
        :param request_data: dict
        :return: dict

        """
        request_data = request_data or {}
        data = json.dumps({'id': '1', 'jsonrpc': '2.0', 'method': method, 'params': request_data})

        headers = {'Content-Type': 'application/json', 'Authorization': 'WWWWizard ' + self.wizard_token}
        if current_app.config.get('TEST_ROLLBACK'):
            with current_app.app_context():
                db.session.begin_nested()
                response = self.app.post("/api/v1", data=data, headers=headers)
        else:
            response = self.app.post("/api/v1", data=data, headers=headers)
        return json.loads(response.data.decode("UTF-8"))


if __name__ == '__main__':
    unittest.main()
