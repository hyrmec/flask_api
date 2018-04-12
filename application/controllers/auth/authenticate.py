#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from application.controllers.auth import jsonrpc
from application import db, auth
from application.models.user import User
from utils.oauth2.oauth2 import OAuthSignIn
from utils.exceptions import flask as flask_exeptions


@jsonrpc.method('OAuth2.authorize(provider=String)', validate=True)
@auth.login_required
def oauth_authorize(provider):
    """ Авторизация пользователя через OAuth2 выбранного провайдера

    :param provider: str
    :return:
    """
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@jsonrpc.method('OAuth2.callback(provider=String)', validate=True)
@auth.login_required
def oauth_callback(provider):
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        raise flask_exeptions.InvalidLogin()
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    #login_user(user, True)
    return True

