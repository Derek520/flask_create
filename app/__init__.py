# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main import api
from config import config_dict

# 创建Flask实例对象
app = Flask(__name__)
# 配置文件需要紧跟着app创建
app.config.from_object(config_dict['develop'])
# 创建数据库对象
db = SQLAlchemy(app)

# 3.注册蓝图对象
app.register_blueprint(api,url_prefix='/api/v1_0')