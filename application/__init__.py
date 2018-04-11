#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin

from flask import Flask, current_app
from flask_cli import FlaskCLI
from flask_jsonrpc import JSONRPC
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
jsonrpc = JSONRPC()
flask_cli = FlaskCLI()
cors = CORS()


def create_app(config_class=Config):
    app = Flask(__name__)
    conf = os.environ.get('APP_CONFIG_SET')
    if 'DEV' in conf:
        app.config.from_object(DevelopConfig)
    elif 'PROD' in conf:
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(config_class)
    cors.init_app(app)
    flask_cli.init_app(app)
    db.init_app(app)

    from application import models
    from application import controllers
    migrate.init_app(app, db)
    jsonrpc.init_app(app)
    jsonrpc.enable_web_browsable_api = True
    jsonrpc.service_url = '/api/v1'
    mail.init_app(app)

    return app
