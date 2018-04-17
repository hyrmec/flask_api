#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from celery import Celery
from raven import Client
from raven.contrib.celery import register_signal, register_logger_signal

from application import create_app


def create_celery(app=None):
    application = app or create_app()
    celery = Celery(application.import_name, broker=application.config.get("CELERY_BROKER_URL_NOTIFICATIONS"))
    celery.conf.update(application.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with application.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    # logging
    client = Client(dsn=application.config.get('SENTRY_DSN'))
    register_logger_signal(client, loglevel='ERROR')
    register_signal(client)
    return celery

