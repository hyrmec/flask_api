# coding: utf-8

from lxml import etree

from sqlalchemy.types import TypeDecorator
from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, Numeric, String, Table, Text, CLOB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.sql.functions import GenericFunction


class XMLTypeFunc(GenericFunction):
    type=CLOB
    name='XMLType'
    identifier='XMLTypeFunc'


class XMLType(TypeDecorator):

    impl = CLOB
    type = 'XMLTYPE' #etree.Element

    def get_col_spec(self):
        return 'XMLTYPE'

    def bind_processor(self, dialect):
        def process(value):
            if value is not None:
                return etree.tostring(value, encoding='UTF-8', pretty_print='True')
                #return etree.dump(value)
            else:
                return None
        return process

    def process_result_value(self, value, dialect):
        if value is not None:
            value = etree.fromstring(value)
        return value

    def bind_expression(self, bindvalue):
        return XMLTypeFunc(bindvalue)
