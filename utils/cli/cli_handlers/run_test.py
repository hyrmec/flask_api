##!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikulshun
import unittest


def run():
    """ Запуск unittests

    :return:
    """
    tests = [
        # your tests
    ]

    base_tests = [unittest.TestLoader().loadTestsFromModule(test) for test in tests]

    runner = unittest.TextTestRunner(verbosity=2)

    for test in base_tests:
        runner.run(test)
