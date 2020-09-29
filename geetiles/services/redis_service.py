""" Redis service """

import json

import redis

from geetiles.config import SETTINGS

print(SETTINGS.get('redis').get('url'))

r = redis.StrictRedis.from_url(url=SETTINGS.get('redis').get('url'))


class RedisService(object):

    @staticmethod
    def check_layer_mapid(layer):
        text = r.get(layer)
        if text is not None:
            return json.loads(text)
        return None

    @staticmethod
    def get(layer):
        text = r.get(layer)
        if text is not None:
            return text
        return None

    @staticmethod
    def set(key, value):
        return r.set(key, value)

    @staticmethod
    def expire_layer(layer):
        for key in r.scan_iter("*" + layer + "*"):
            r.delete(key)

    @staticmethod
    def set_layer_mapid(layer, mapid, token):
        return r.set(layer, json.dumps({'mapid': mapid, 'token': token}), ex=2 * 24 * 60 * 60)
