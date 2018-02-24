# -*- coding:utf-8 -*-
from . import api
from app import db
# 2.在路由中使用蓝图
@api.route('/')
def hello_world():
    return 'Hello World!'