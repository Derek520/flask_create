# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config_dict

db = SQLAlchemy()


'''
开启csfr保护机制,rustfull都需要
'''

# 定一个函数,返回两个参数app,db
def create_app(config_info):
    '''封装函数'''

    # 创建Flask实例对象
    app = Flask(__name__)
    # 配置文件需要紧跟着app创建
    app.config.from_object(config_info)
    # 创建数据库对象
    # db = SQLAlchemy(app)
    # 延迟导入app
    db.init_app(app)

    # 开启csrf保护机制
    # KeyError: 'A secret key is required to use CSRF.' // Werkzeug Debugger
    CSRFProtect(app)
    # 3.注册蓝图对象
    from app.main import api
    app.register_blueprint(api,url_prefix='/api/v1_0')

    return app,db