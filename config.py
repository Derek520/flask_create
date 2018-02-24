# -*- coding:utf-8 -*-
# config.py实现配置信息

class Config(object):
    '''配置文件'''
    # mysql数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/ihome21'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


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