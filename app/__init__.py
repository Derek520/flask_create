# -*- coding:utf-8 -*-
import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config_dict,Config
from flask_session import Session
from .tools.commons import RegexConverter

db = SQLAlchemy()

# 外界将来需要用到redis来做存储或读取. redis的创建应该放在和app创建一样的文件中. 留出对象供外界调用
redis_store = None

'''
开启csfr保护机制,restfull都需要
'''

# 定一个函数,返回两个参数app,db
def create_app(config_info):
    '''封装函数'''

    # 创建Flask实例对象
    app = Flask(__name__)

    app.url_map.converters['re']=RegexConverter
    # 配置文件需要紧跟着app创建
    app.config.from_object(config_info)
    # 创建数据库对象
    # db = SQLAlchemy(app)
    # 延迟导入app
    db.init_app(app)

    # 开启csrf保护机制
    # KeyError: 'A secret key is required to use CSRF.' // Werkzeug Debugger
    CSRFProtect(app)

    # 连接redis数据库
    # 声明全局变量
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
    # 创建Session, 将session数据从以前默认的cookie, 存放到redis中
    Session(app)
    # 3.注册蓝图对象
    from app.main import api
    app.register_blueprint(api,url_prefix='/api/v1_0')

    from .web_static_html import html
    app.register_blueprint(html)

    return app,db