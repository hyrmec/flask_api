#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
import os
from flask import Flask
from flask_cli import FlaskCLI
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from flask_jsonrpc import JSONRPC
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
jsonrpc = JSONRPC(service_url='/api/v1', enable_web_browsable_api=True)
flask_cli = FlaskCLI()
cors = CORS()
ma = Marshmallow()
auth = HTTPTokenAuth(scheme='WWWToken')


@auth.verify_token
def verify_token(token):
    """Верификация токена авторизации

    """
    return True


def configure_app(app):
    config = {
        "dev": "config.DevelopConfig",
        "prod": "config.ProductionConfig",
        "test": "config.Test"
    }
    config_name = os.getenv('FLASK_CONFIGURATION', 'prod').replace("\r",'')
    app.config.from_object(config[config_name])


def create_app():
    app = Flask(__name__)
    configure_app(app)

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
    app.register_blueprint(controllers.restfull.mod_restfull)

    return app
