#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikulshin

from flask_jsonrpc.exceptions import Error


class InvalidUsage(Error):
    """Абстрактная ошибка JSON-RPC
    
    """
    code = 500

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
        self.data = {'clear_message': message}

    def to_dict(self):
        rv = dict()
        rv['message'] = self.message
        return rv


class EmptyField(InvalidUsage):
    """ Незаполненное поле
    
    """
    code = 40001

    def __init__(self, caption: str):
        super(EmptyField, self).__init__("Empty field %r" % caption)


class DuplicateObject(InvalidUsage):
    """ Дублирующий объект
    
    """
    code = 40002

    def __init__(self, obj):
        super(DuplicateObject, self).__init__("Duplicate object %r" % obj)


class InvalidDateFormat(InvalidUsage):
    """

    """
    code = 40003

    def __init__(self):
        super(InvalidDateFormat, self).__init__("Invalid date format")


class NotEnoughSpace(Error):
    """ Доступ авторизованному пользователю закрыт к запрашиваемой функциональности

    """
    code = 40400

    def __init__(self, caption='NotEnoughSpace'):
        super(NotEnoughSpace, self).__init__(caption)


class Forbidden(Error):
    """ Доступ авторизованному пользователю закрыт к запрашиваемой функциональности

    """
    code = 40403

    def __init__(self):
        super(Forbidden, self).__init__("The user might not have the necessary permissions for a resource")


class ObjectDoesNotExists(InvalidUsage):
    """ Объект не существует

    """
    code = 40404

    def __init__(self):
        super(ObjectDoesNotExists, self).__init__("Object does not exists")


class ObjectExistsInDB(InvalidUsage):
    """ Объект существует в базе данных, но не должен

    """
    code = 40405

    def __init__(self):
        super(ObjectExistsInDB, self).__init__("Object exists in DB")


class InvalidLoginOrPassword(InvalidUsage):
    """Неправильный логин или пароль
    
    """
    code = 40010

    def __init__(self):
        super(InvalidLoginOrPassword, self).__init__("Invalid login or password")


class InvalidLogin(InvalidUsage):
    """Неправильный логин
    
    """
    code = 40011

    def __init__(self):
        super(InvalidLogin, self).__init__("Invalid login")


class InvalidPassword(InvalidUsage):
    """Неправильный пароль
    
    """
    code = 40012

    def __init__(self):
        super(InvalidPassword, self).__init__("Invalid password")


class SessionTokenRequired(InvalidUsage):
    """ Необходим токен сессии
    
    """
    code = 40013

    def __init__(self):
        super(SessionTokenRequired, self).__init__("Session token required")


class InvalidLoginAction(InvalidUsage):
    """ Доступ к системе закрыт

    """
    code = 40014

    def __init__(self, message=None):
        super(InvalidLoginAction, self).__init__(message or "Доступ к системе закрыт")
        if message:
            self.message = message
            self.data = {'clear_message': message}


class InvalidCRC32(InvalidUsage):
    """

    """
    code = 50020

    def __init__(self):
        super(InvalidCRC32, self).__init__("Invalid CRC32 checksum")


class NotLastOperation(InvalidUsage):
    """

    """
    code = 50030

    def __init__(self):
        super(NotLastOperation, self).__init__("Not last operation")
