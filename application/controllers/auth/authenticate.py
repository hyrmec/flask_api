#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from application.controllers.auth import jsonrpc
from flask import current_app
from utils.celery import create_celery


@jsonrpc.method('App.index')
def index():
    celery = create_celery(current_app)
    res = celery.send_task('tasks.test', args=(5,4))
    return u'Welcome to Flask JSON-RPC'


@jsonrpc.method('App.indexx')
def indexx():
    celery = create_celery(current_app)
    res = celery.send_task('tasks.test', args=(2,0))
    return u'Welcome to Flask JSON-RPC'
