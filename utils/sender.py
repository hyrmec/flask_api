#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
import smsru
from flask_mail import Mail, Message

from application import create_app, mail
from config import Config


class Sender(object):
    """ Класс для отправки смс и email сообщений

    """

    def __init__(self, subject=None, html_body=None, recipients=None, reply_to=None, file=None, to=None, text=None):
        self.app = create_app(Config)
        self.subject = subject
        self.html_body = html_body
        if self.app.config.get('DEBUG'):
            self.recipients = [self.app.config.get('TEST_EMAIL')]
        else:
            self.recipients = recipients
        self.reply_to = reply_to
        self.file = file
        if self.app.config.get('DEBUG'):
            self.to = self.app.config.get('TEST_PHONE')
        else:
            self.to = to
        self.text = text

    def send_email(self):
        Mail(self.app)
        msg = Message(subject=self.subject, sender=self.app.config.get('MAIL_SENDER'), recipients=self.recipients)
        msg.html = self.html_body
        with self.app.app_context():
            mail.send(msg)
        return True

    def send_email_attach(self):
        Mail(self.app)
        msg = Message(subject=self.subject, sender=self.app.config.get('MAIL_SENDER'), reply_to=self.reply_to,
                      recipients=self.recipients)
        msg.html = self.html_body
        msg.attach("flats.pdf", "application/pdf", self.file.read())
        with self.app.app_context():
            mail.send(msg)
        return True

    def send_sms(self):
        API_ID = self.app.config.get('API_ID_SMS')
        LOGIN = self.app.config.get('LOGIN_SMS')
        PASSWORD = self.app.config.get('PASSWORD_SMS')
        SENDER = self.app.config.get('SENDER_SMS')
        client = smsru.SmsClient(API_ID, LOGIN, PASSWORD, SENDER)
        api = client.get_api()
        sms_id = api.sms.send(to=self.to, text=self.text)[1]  # translit=1 - если хотим транслитом
        return api.sms.status(sms_id=sms_id)
