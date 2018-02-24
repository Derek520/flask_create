# -*- coding:utf-8 -*-

# manager: 主要管理程序的启动, 以及db的操作
from flask import Flask
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
# from app import app,db
from app import create_app
from config import config_dict


app,db = create_app(config_dict['develop'])


# # 创建Flask实例对象
# app = Flask(__name__)
# 创建命令行Manager对象
manager = Manager(app)
# 创建数据库迁移对象
Migrate(app,db)
# 创建命令行数据库迁移指令
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    # app.run(debug=True,host='0.0.0.0')
    # 使用manger启动
    manager.run()