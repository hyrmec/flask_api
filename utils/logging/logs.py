#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
import logging
from logging.handlers import SMTPHandler

def run_logging(app):
    """ Запуск логера для отправки ошибок приложения на email и логирование в файл

    """
    # Логи на email
    mail_handler = SMTPHandler(mailhost=(app.config.get('MAIL_SERVER'),app.config.get('MAIL_PORT')),
                               fromaddr=app.config.get('MAIL_USERNAME'),
                               toaddrs=app.config.get('SEND_ERROR_EMAILS'), subject='Ошибка API',
                               credentials=(app.config.get('MAIL_USERNAME'),app.config.get('MAIL_PASSWORD')))
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
    # Логи в файл
    handler = logging.StreamHandler()
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config.get("DEBUG_LVL", logging.ERROR))