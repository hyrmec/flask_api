#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from application.controllers.auth import jsonrpc


@jsonrpc.method('App.index')
def index():
    return u'Welcome to Flask JSON-RPC'
