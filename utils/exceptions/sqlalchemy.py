#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikulshin


class InvalidPassword(Exception):
    pass


class DuplicateLogin(Exception):
    pass


class EmptyField(Exception):
    pass


class InvalidField(Exception):
    pass
