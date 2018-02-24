# -*- coding:utf-8 -*-

# manager: 主要管理程序的启动, 以及db的操作
from flask import Flask
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')