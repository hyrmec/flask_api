#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Стандартная конфигурация сервера

    """
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@0.0.0.0:5432/database'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    PASS_AUTORISATION = 'aunQHNhY80=g[`0'

    CELERY_BROKER_URL_NOTIFICATIONS = ''

    DADATA_URL = 'https://dadata.ru/api/v2/clean/'
    DADATA_URL_SUGGEST = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/'
    DADATA_KEY = ''
    DADATA_SECRET_KEY = ''

    # email settings
    TEST_EMAIL = ''
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT= 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = ['test','test@test.test']
    MAIL_SENDER = ['test','test@test.test']

    # sms settings
    TEST_PHONE = ''
    API_ID_SMS = 'CA9560FF-4D9D-FD83-30DB-205676BE224D'
    LOGIN_SMS = ''
    PASSWORD_SMS = ''
    SENDER_SMS = ''

    TEST_LOGIN = 'admin'
    TEST_PASSWORD = 'pass'
    TEST_IS_SUBAGENT = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopConfig(Config):
    LOGS_PATH = '/'
    LOG_REQUESTS = True
    TEST_ROLLBACK = False


class Test(Config):
    DEBUG = True
    TESTING = True
