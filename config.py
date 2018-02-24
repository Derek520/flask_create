# -*- coding:utf-8 -*-
# config.py实现配置信息
import redis

class Config(object):
    '''配置文件'''
    # mysql数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/ihome21'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # csrf的secret_key相关配置
    # import os, base64
    # base64.b64encode(os.urandom(32))
    # 'y8P8rzqR0HOgWq+beq6g+KfGYw+xTLyRqr0QZCQEOXM='
    SECRET_KEY = 'y8P8rzqR0HOgWq+beq6g+KfGYw+xTLyRqr0QZCQEOXM='

    # redis
    REDIS_HOST = '47.94.238.54'
    REDIS_PORT = 6379
    # 配置session存储到redis中
    PERMANENT_SESSION_LIFETIME = 86400  # 单位是秒, 设置session过期的时间
    SESSION_TYPE = 'redis'  # 指定存储session的位置为redis
    SESSION_USE_SIGNER = True  # 对数据进行签名加密, 提高安全性
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 设置redis的ip和端口


class DevelopmentConfig(Config):
  DEBUG = True

class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/ihome21'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass

config_dict = {
    'develop':DevelopmentConfig,
    'production':ProductionConfig
}