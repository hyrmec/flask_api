#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
from application.controllers.auth import jsonrpc
from application import db, auth
from application.models.user import User
from utils.oauth2.oauth2 import OAuthSignIn
from utils.exceptions import flask as flask_exeptions


@jsonrpc.method('OAuth2.authorize(provider=String)', validate=True)
def oauth_authorize(provider):
    """ Получение ссылки на авторизацию сервиса

    :param provider: str
    :return:
    """
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@jsonrpc.method('OAuth2.signin(provider=String)', validate=True)
def oauth_signin(provider):
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        raise flask_exeptions.InvalidLogin()
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    return True


if __name__ == '__main__':
    oauth_authorize('facebook')