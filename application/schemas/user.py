#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from application import ma
from application.models.user import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User