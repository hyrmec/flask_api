##!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikulshun
import unittest
from application.tests import auth

def run():
    """ Запуск unittests

    :return:
    """
    tests = [
        auth,
    ]

    base_tests = [unittest.TestLoader().loadTestsFromModule(test) for test in tests]

    runner = unittest.TextTestRunner(verbosity=2)

    for test in base_tests:
        runner.run(test)
