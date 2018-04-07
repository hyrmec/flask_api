#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin

import logging

from application import create_app
from config import DevelopConfig
from utils.cli.cli import register_cli

app = create_app(DevelopConfig)
register_cli(app)
app.config.update(
    DEBUG_LVL=logging.ERROR,
)
if "__main__" == __name__:
    handler = logging.StreamHandler()
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config.get("DEBUG_LVL", logging.ERROR))

    app.run(host='0.0.0.0', port=8000)