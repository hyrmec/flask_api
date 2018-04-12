#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from application import create_app
from utils.cli.cli import register_cli
from utils.logging import logs

app = create_app()
register_cli(app)
if "__main__" == __name__:
    logs.run_logging(app)
    app.run(host='0.0.0.0', port=8000)