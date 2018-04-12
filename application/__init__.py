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
from flask_marshmallow import Marshmallow
from config import DevelopConfig, ProductionConfig

db = SQLAlchemy()
migrate = Migrate()
jsonrpc = JSONRPC(service_url='/api/v1',enable_web_browsable_api=True)
flask_cli = FlaskCLI()
cors = CORS()
ma = Marshmallow()
auth = HTTPTokenAuth(scheme='WWWToken')


@auth.verify_token
def verify_token(token):
    """Верификация токена авторизации

    """
    return True


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
    ma.init_app(app)

    # Models
    from application import models

    migrate.init_app(app, db)
    jsonrpc.init_app(app)

    # Register blueprints
    from application import controllers
    app.register_blueprint(controllers.auth.mod_auth)

    return app
