# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建Flask实例对象
app = Flask(__name__)

# 创建数据库对象
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'