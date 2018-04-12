#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin

from application import jsonrpc, auth
from application.controllers.auth import mod_auth

jsonrpc.register_blueprint(mod_auth)

@jsonrpc.method('Auth.test')
@auth.login_required()
def auth_test():
    return
