#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin

from application import db

class User(db.Model):
    __table__ = 'test_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))