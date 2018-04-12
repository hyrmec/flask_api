#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
import os
from flask import Flask, current_app
from flask_cli import FlaskCLI
from flask_jsonrpc import JSONRPC
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
from config import DevelopConfig, ProductionConfig

db = SQLAlchemy()
migrate = Migrate()
jsonrpc = JSONRPC()
flask_cli = FlaskCLI()
cors = CORS()

auth = HTTPTokenAuth(scheme='WWWToken')


@auth.verify_token
def verify_token(token):
    """Верификация токена авторизации

    """
    if token:
        return True
    else:
        return False


def create_app(config_class=DevelopConfig):
    app = Flask(__name__)
    conf = os.environ.get('APP_CONFIG_SET')
    if conf and 'DEV' in conf:
        app.config.from_object(DevelopConfig)
    elif conf and 'PROD' in conf:
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(config_class)

    cors.init_app(app)
    flask_cli.init_app(app)
    db.init_app(app)

    # Models
    from application import models

    migrate.init_app(app, db)
    jsonrpc.init_app(app)
    jsonrpc.enable_web_browsable_api = True
    jsonrpc.service_url = '/api/v1'

    # Register blueprints
    from application import controllers
    app.register_blueprint(controllers.auth.mod_auth)

    return app
