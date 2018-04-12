#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikulshin

import binascii

from sqlalchemy import LargeBinary, TypeDecorator

from Crypto.Cipher import AES
from uuid import UUID
from base64 import b64encode, b64decode

key = UUID("17c2c38d-e93d-40c3-8053-71e14aaa39cd").bytes


def aes_encrypt(data):
    """Encryption AES data
    :param data: str
    :return: bytes
    
    """
    if data is None:
        return

    cipher = AES.new(key)
    data = b64encode(data.encode("utf-8")).decode("utf-8")
    data += " " * (16 - (len(data) % 16))

    return binascii.hexlify(cipher.encrypt(data))


def aes_decrypt(data):
    """Decryption AES data
    :param data: bytes
    :return: str
    
    """
    if data is None:
        return

    cipher = AES.new(key)
    data = cipher.decrypt(binascii.unhexlify(data)).rstrip()
    return b64decode(data)


class AESField(TypeDecorator):
    """Column for AES encrypted data
    
    """
    impl = LargeBinary

    def process_bind_param(self, value, dialect):
        """Binding parameter
        :param value: str
        :param dialect: str
        :return: bytes
        
        """
        return aes_encrypt(value)

    def process_result_value(self, value, dialect):
        """Returning value
        :param value: bytes
        :param dialect: str
        :return: str
        
        """
        encrypt_value = aes_decrypt(value)

        if encrypt_value:
            return encrypt_value.decode("utf-8")
