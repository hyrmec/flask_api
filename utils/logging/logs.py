#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
import logging

from raven import Client
from raven.handlers.logging import SentryHandler


def run_logging(app):
    """ Запуск логов Sentry (оповещение об ошибках на production)

    """
    # Sentry
    sentry_client = Client(dsn=app.config.get('SENTRY_DSN'))
    sentry_handler = SentryHandler(sentry_client)
    sentry_handler.setLevel('ERROR')
    app.logger.addHandler(sentry_handler)

    # Логи в файл
    handler = logging.StreamHandler()
    app.logger.addHandler(handler)
    app.logger.setLevel('ERROR')
