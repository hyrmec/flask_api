#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from flask import Blueprint

mod_test = Blueprint('test',__name__)

from application.controllers.test import test