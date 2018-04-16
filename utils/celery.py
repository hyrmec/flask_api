#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from celery import Celery

from application import create_app


def create_celery():
    application = create_app()
    celery = Celery(application.import_name, broker=application.config.get("CELERY_BROKER_URL_NOTIFICATIONS"))
    celery.conf.update(application.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with application.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery

