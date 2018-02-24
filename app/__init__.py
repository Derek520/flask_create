# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main import api


# 创建Flask实例对象
app = Flask(__name__)

# 创建数据库对象
db = SQLAlchemy(app)

# 3.注册蓝图对象
app.register_blueprint(api,url_prefix='/api/v1_0')