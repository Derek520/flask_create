# -*- coding:utf-8 -*-
from . import api
from app import db
# 2.在路由中使用蓝图


@api.route('/index', methods=['GET', 'POST'])
def index():
    return 'index'