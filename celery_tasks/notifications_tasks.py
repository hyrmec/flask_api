#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikulshin
from utils.celery import create_celery

celery = create_celery()


@celery.task()
def test(x,y):

    return x+y


