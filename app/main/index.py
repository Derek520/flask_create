# -*- coding:utf-8 -*-
from . import api
from app import db
import logging

# 2.在路由中使用蓝图
@api.route('/index', methods=['GET', 'POST'])
def index():
    logging.error('info')
    logging.error('debug')
    logging.error('bug')
    return 'index'