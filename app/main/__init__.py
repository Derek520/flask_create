# -*- coding:utf-8 -*-
# 蓝图
from flask import Blueprint
# 1. 创建蓝图
api = Blueprint('api',__name__)

# 导入子模块
import index