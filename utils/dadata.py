#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Author: Pavel Nikylshin
import datetime
import json

import requests

from application import create_app
from utils.exceptions import flask as flask_exc


class Dadata(object):
    """ Класс для работы с dadata

    """
    def __init__(self):
        self.app = create_app()

    def dadata_housing(self, value, limit):
        """Обращение к API dadata для получения информации о корпусе
            #         CC A RRR GGG GGG2PPP XUUUUUUUU2XUUUU3
            #         СС А РРР ГГГ ВВВ ППП УУУУ ЭЭЭЭ ЦЦЦ
            # ФИАС:   74 0 026 000 000 032 0021 0000 000
            # КЛАДР:  74   026 000     032 0021
            #         50   021 001     000 0102 0100
            #         50   021 001     000 0102 0100

        :param value: str
        :param limit: int
        :return:
        """
        url = self.app.config.get('DADATA_URL') + "address"
        headers = {
            'Authorization': 'Token ' + self.app.config.get('DADATA_KEY'),
            'Content-Type': 'application/json',
            'X-Secret': self.app.config.get('DADATA_SECRET_KEY')
        }
        data = [value]
        r = requests.post(url, headers=headers, data=json.dumps(data))

        if r.status_code == 200:
            text = json.loads(r.content.decode('utf-8'))
            res = []
            for elem in text:
                res.append({
                    'label': elem.get('result'),
                    'XCC': elem.get('kladr_id')[:2],
                    'XA': '0',
                    'XRRR': elem.get('kladr_id')[2:5],
                    'XGGG': elem.get('kladr_id')[5:8],
                    'XGGG2': '0',
                    'XPPP': elem.get('kladr_id')[8:11],
                    'XUUUU': elem.get('kladr_id')[11:15],
                    'XUUUU2': elem.get('kladr_id')[15:],
                    'XUUUU3': '0',
                    'DDD': elem.get('house'),
                    'lat': elem.get('geo_lat'),
                    'lon': elem.get('geo_lon')
                })
            return res
        else:
            raise flask_exc.InvalidUsage("Ошибка отправки запроса DADATA")

    def dadata_adress(self, query):
        """ Получение адресов с координатами

        :return:
        """
        url = self.app.config.get('DADATA_URL_SUGGEST') + 'address'
        headers = {
            'Authorization': 'Token ' + self.app.config.get('DADATA_KEY'),
            'Content-Type': 'application/json',
            'X-Secret': self.app.config.get('DADATA_SECRET_KEY')
        }
        data = {"query": query, "count": 5}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        if r.status_code == 200:
            text = json.loads(r.content.decode('utf-8'))
            res = []
            for elem in text.get('suggestions'):
                if elem.get('data').get('geo_lat') and elem.get('data').get('geo_lon'):
                    res.append({
                        'label': elem.get('value'),
                        'XCC': elem.get('data').get('kladr_id')[:2],
                        'XA': '0',
                        'XRRR': elem.get('data').get('kladr_id')[2:5],
                        'XGGG': elem.get('data').get('kladr_id')[5:8],
                        'XGGG2': '0',
                        'XPPP': elem.get('data').get('kladr_id')[8:11],
                        'XUUUU': elem.get('data').get('kladr_id')[11:15],
                        'XUUUU2': elem.get('data').get('kladr_id')[15:],
                        'XUUUU3': '0',
                        'DDD': elem.get('data').get('house'),
                        'lat': elem.get('data').get('geo_lat'),
                        'lon': elem.get('data').get('geo_lon')
                    })
                else:
                    geo = Dadata.get_geo_yandex(elem.get('value'))
                    res.append({
                        'label': elem.get('value'),
                        'XCC': elem.get('data').get('kladr_id')[:2],
                        'XA': '0',
                        'XRRR': elem.get('data').get('kladr_id')[2:5],
                        'XGGG': elem.get('data').get('kladr_id')[5:8],
                        'XGGG2': '0',
                        'XPPP': elem.get('data').get('kladr_id')[8:11],
                        'XUUUU': elem.get('data').get('kladr_id')[11:15],
                        'XUUUU2': elem.get('data').get('kladr_id')[15:],
                        'XUUUU3': '0',
                        'DDD': elem.get('data').get('house'),
                        'lat': geo[1],
                        'lon': geo[0]
                    })

            return res
        else:
            raise flask_exc.InvalidUsage("Ошибка отправки запроса DADATA")

    def dadata_suggest_org(self, query, limit=5):
        """ Подсказки по организациям

        :param query: str
        :param limit: int
        :return:
        """
        url = self.app.config.get('DADATA_URL_SUGGEST') + 'party'
        headers = {
            'Authorization': 'Token ' + self.app.config.get('DADATA_KEY'),
            'Content-Type': 'application/json',
            'X-Secret': self.app.config.get('DADATA_SECRET_KEY')
        }
        data = {"query": query, "count": limit}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        if r.status_code == 200:
            text = json.loads(r.content.decode('utf-8'))
            res = []
            for elem in text.get('suggestions'):
                if elem.get('value') and elem.get('data').get('inn'):
                    res.append({
                        'organisation_socrach_caption': elem.get('value'),
                        'organisation_caption': elem.get('data').get('name').get('full_with_opf')
                        if elem.get('data').get('name') else None,
                        'organisation_address': elem.get('data').get('address').get('value')
                        if elem.get('data').get('address') else None,
                        'organisation_inn': elem.get('data').get('inn'),
                        'organisation_kpp': elem.get('data').get('kpp'),
                        'organisation_ogrn': elem.get('data').get('ogrn'),
                        'organisation_okpo': elem.get('data').get('okpo'),
                        'organisation_okved': elem.get('data').get('okved'),
                        'organisation_opf': elem.get('data').get('opf').get('full')
                        if elem.get('data').get('opf') else None,
                        'organisation_gen_dir': elem.get('data').get('management').get('name')
                        if elem.get('data').get('management') else None,
                        'organisation_gen_dir_doljn': elem.get('data').get('management').get('post')
                        if elem.get('data').get('management') else None,
                        'organisation_registration_date': datetime.datetime.fromtimestamp((elem.get('data').get('state')
                            .get(
                            'registration_date')) / 1000)
                            .strftime("%d.%m.%Y")
                        if elem.get('data').get('state').get('registration_date') else None,
                        'organisation_emails': elem.get('data').get('emails') if elem.get('data').get(
                            'emails') else None,
                        'organisation_phones': elem.get('data').get('phones') if elem.get('data').get(
                            'phones') else None,
                    })
            return res
        else:
            raise flask_exc.InvalidUsage("Ошибка отправки запроса DADATA")

    @staticmethod
    def get_geo_yandex(query):
        """ Получение координат из яндекса по адресу

        :param query:string
        :return:
        """
        url_yandex = 'https://geocode-maps.yandex.ru/1.x/'
        params = {'format': 'json', 'geocode': query}
        yandex = requests.get(url_yandex, params=params)
        if yandex.status_code == 200:
            content = json.loads(yandex.content.decode('utf-8')).get('response').get('GeoObjectCollection').get(
                'featureMember')
            latlon = content[0].get('GeoObject').get('Point').get('pos')
            if len(latlon) > 0:
                lat_lon = latlon.split(' ')
            else:
                lat_lon = [None, None]
            return lat_lon
        else:
            raise flask_exc.InvalidUsage("Ошибка отправки запроса yandex")
