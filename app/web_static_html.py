# -*- coding:utf-8 -*-
# 处理首页静态文件访问
from flask import Blueprint, current_app, make_response
from flask_wtf.csrf import generate_csrf

from .tools.commons import RegexConverter
html = Blueprint('html',__name__)

@html.route('/<re(".*"):file_name>')
def get_html(file_name):
    '''根路径访问'''
    print file_name
    if not file_name:
        print 123
        file_name = 'index.html'

    if file_name != 'favicon.ico':
        file_name = 'html/' + file_name
    print file_name
    # return current_app.send_static_file(file_name)
    # 生成 csrf_token
    csrf_token = generate_csrf()
    # 将 csrf_token 设置到 cookie 中
    response = make_response(current_app.send_static_file(file_name))
    response.set_cookie("csrf_token", csrf_token)
    return response