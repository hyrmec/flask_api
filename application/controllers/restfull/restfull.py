#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from flask import current_app

from application.controllers.restfull import mod_restfull


@mod_restfull.route("/")
def hello():
    print(current_app.config.get('TEST_LOGIN'))
    return 'Welcome to API!'
