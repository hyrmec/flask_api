#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from flask import Blueprint

mod_restfull = Blueprint('restfull',__name__)

from application.controllers.restfull import restfull