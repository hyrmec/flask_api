#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from flask import Blueprint
mod_auth = Blueprint('auth',__name__)

from application.controllers.auth import authenticate