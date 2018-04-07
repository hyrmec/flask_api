#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikulshin

from utils.celery import create_celery_notify

celery = create_celery_notify()


@celery.task()
def celery(x,y):
    """ celery test

    :param x:
    :param y:
    :return:
    """

    return x+y
