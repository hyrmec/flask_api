#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from flask import Blueprint
from application import jsonrpc

mod_auth = Blueprint('auth',__name__)
jsonrpc.register_blueprint(mod_auth)

from application.controllers.auth import authenticate