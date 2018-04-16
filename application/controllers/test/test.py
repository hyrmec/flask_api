#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from application.controllers.test import mod_test
#from application import sentry


@mod_test.route("/")
def hello():
    try:
        1 / 0
    except ZeroDivisionError:
        a=10
        #sentry.captureException()
    return "Hello World!"

