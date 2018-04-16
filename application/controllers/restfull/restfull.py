#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from application.controllers.restfull import mod_restfull


@mod_restfull.route("/")
def hello():
    return "Hello World!"
