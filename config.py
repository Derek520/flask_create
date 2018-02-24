# -*- coding:utf-8 -*-
# config.py实现配置信息

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