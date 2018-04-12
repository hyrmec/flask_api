#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from application.controllers.auth import jsonrpc
from application import auth

@jsonrpc.method('Auth.test')
@auth.login_required
def auth_test():
    return
